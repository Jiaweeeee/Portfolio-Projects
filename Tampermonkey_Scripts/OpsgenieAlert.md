```markdown
# Opsgenie Alert Sound Tampermonkey Script

## Description
The Opsgenie Alert Sound Tampermonkey script enhances the Opsgenie alerting system by playing a notification sound whenever a new alert is detected on the Opsgenie alerts page. It also logs the ticket IDs of the alerts to the console, providing a clear and audible indication of new alerts to ensure that they are not missed. This script is particularly useful for users who need to be promptly informed of any new issues or incidents requiring their attention.

## Features
- **Sound Notification**: Plays a distinct alert sound whenever a new alert appears on the Opsgenie alerts list.
- **Console Logging**: Logs the ticket IDs of the alerts to the console for easy tracking and debugging.
- **Real-time Monitoring**: Checks for new alerts every second to provide immediate notifications.

## How It Works
1. The script defines a function to play a sound using the HTML5 Audio API.
2. It retrieves all current alert ticket IDs from the page and stores them.
3. It periodically checks for new alerts by comparing the current ticket IDs with the stored ones.
4. If new alerts are detected, the sound is played, and the list of ticket IDs is updated.

## Note
Due to Chrome's autoplay policy, users need to interact with the site at least once before the sound can be played.
```
