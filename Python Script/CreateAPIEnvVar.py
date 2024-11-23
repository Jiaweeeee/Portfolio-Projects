import os
import platform
import subprocess
import re
from colorama import Fore, Style, init

init(autoreset=True)

def open_regedit():
    if platform.system() == "Windows":
        print(Fore.YELLOW + "\nOpening the Registry Editor to the Environment page...\n")
        try:
            subprocess.run("regedit.exe", shell=True)
            print(Fore.GREEN + "Navigate to HKEY_CURRENT_USER\\Environment in the Registry Editor.")
        except Exception as e:
            print(Fore.RED + f"Failed to open the Registry Editor: {e}")
    else:
        print(Fore.RED + "This feature is only supported on Windows.")

def show_api_keys():
    print(Fore.YELLOW + "\nScanning for API keys in environment variables...\n")
    api_keys = []
    for key, value in os.environ.items():
        if re.search(r'(API_KEY|TOKEN|SECRET|KEY)', key, re.IGNORECASE) and len(value) > 20:
            if re.match(r'^[A-Za-z0-9-_]+$', value):
                api_keys.append((key, value))
    if api_keys:
        print(Fore.GREEN + "Likely API Keys Found:\n")
        for key, value in api_keys:
            print(Fore.CYAN + f"{key}: {value}")
    else:
        print(Fore.RED + "No API keys detected.\n")

def is_valid_env_var_name(name):
    return name.isidentifier()

def add_or_update_env_var():
    env_var_name = input(Fore.CYAN + "Enter the name for the environment variable (e.g., OPENAI_API_KEY): ").strip()
    if not is_valid_env_var_name(env_var_name):
        print(Fore.RED + "Invalid environment variable name. It should be alphanumeric and may include underscores.")
        return
    value = input(Fore.CYAN + f"Enter the value for {env_var_name}: ").strip()
    if not value:
        print(Fore.RED + "The value cannot be empty.")
        return
    existing_value = os.environ.get(env_var_name)
    if existing_value:
        print(Fore.YELLOW + f"\nThe environment variable '{env_var_name}' already exists with value: {existing_value}")
        overwrite = input(Fore.CYAN + "Do you want to overwrite it? (yes/no): ").strip().lower()
        if overwrite not in ['yes', 'y']:
            print(Fore.YELLOW + "No changes made.")
            return
    set_env_var(env_var_name, value)
    print(Fore.GREEN + f"\nEnvironment variable '{env_var_name}' has been set.")
    prompt_restart_cmd()

def delete_env_var():
    env_var_name = input(Fore.CYAN + "Enter the name of the environment variable to delete: ").strip()
    existing_value = os.environ.get(env_var_name)
    if not existing_value:
        print(Fore.RED + f"The environment variable '{env_var_name}' does not exist.")
        return
    confirm = input(Fore.CYAN + f"Are you sure you want to delete '{env_var_name}'? (yes/no): ").strip().lower()
    if confirm in ['yes', 'y']:
        if platform.system() == "Windows":
            os.system(f"setx {env_var_name} \"\"")
        print(Fore.GREEN + f"Environment variable '{env_var_name}' has been deleted.")
        os.environ.pop(env_var_name, None)
        prompt_restart_cmd()
    else:
        print(Fore.YELLOW + "No changes made.")

def set_env_var(name, value):
    if platform.system() == "Windows":
        try:
            subprocess.run(f'setx {name} "{value}"', shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f"Failed to set the variable: {e}")
            print(Fore.RED + "Try running the script with admin rights.")

def prompt_restart_cmd():
    print(Fore.YELLOW + "\nNOTE: Restart CMD or open a new session to fully apply changes.")
    print(Fore.YELLOW + "You can also open the Registry Editor to verify changes (Option 4 in the menu).")

def main_menu():
    while True:
        print(Fore.MAGENTA + "\nEnvironment Variable Manager")
        print(Fore.CYAN + "1. Show all API keys (environment variables)")
        print(Fore.CYAN + "2. Add or update an environment variable")
        print(Fore.CYAN + "3. Delete an environment variable")
        print(Fore.CYAN + "4. Open Registry Editor to Environment page")
        print(Fore.CYAN + "5. Exit")
        choice = input(Fore.CYAN + "Choose an option (1-5): ").strip()
        if choice == '1':
            show_api_keys()
        elif choice == '2':
            add_or_update_env_var()
        elif choice == '3':
            delete_env_var()
        elif choice == '4':
            open_regedit()
        elif choice == '5':
            print(Fore.GREEN + "Exiting the program.")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
