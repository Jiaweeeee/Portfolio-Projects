// ==UserScript==
// @name         Opsgenie Alert Sound
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Plays a sound when a new alert comes in on Opsgenie and logs ticket IDs in the console
// @updateURL    https://raw.githubusercontent.com/Jiaweeeee/Portfolio-Projects/main/Tampermonkey_Scripts/OpsgenieAlert.js
// @downloadURL  https://raw.githubusercontent.com/Jiaweeeee/Portfolio-Projects/main/Tampermonkey_Scripts/OpsgenieAlert.js
// @author       Sky
// @match        https://*.app.opsgenie.com/alert/list
// @grant        none
// @run-at       document-end
// ==/UserScript==

/*
Copyright (C) 2024 Low Jia Wee, Sky

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/

(function() {
    'use strict';

    // Function to play an alert sound
    function playAlertSound() {
        const audio = new Audio('https://cdn.pixabay.com/download/audio/2024/02/19/audio_e4043ea6be.mp3?filename=level-up-191997.mp3'); // Free sound from pixabay
        audio.play().then(() => {
            console.log("Alert sound played");
        }).catch(error => {
            console.error("Error playing alert sound:", error);
        });
    }

    // Function to get all alert ticket IDs
    function getAllAlertTicketIDs() {
        const alertElements = document.querySelectorAll('a > div > div > div > b');
        return Array.from(alertElements).map(alertElement => alertElement.textContent.trim());
    }

    // Store initial ticket IDs
    let storedTicketIDs = getAllAlertTicketIDs();
    console.log("Initial Ticket IDs:", storedTicketIDs);

    // Function to check for new alerts
    function checkForNewAlerts() {
        const currentTicketIDs = getAllAlertTicketIDs();
        const newAlerts = currentTicketIDs.filter(ticketID => !storedTicketIDs.includes(ticketID));

        if (newAlerts.length > 0) {
            playAlertSound();
            storedTicketIDs = currentTicketIDs; // Update stored ticket IDs
            console.log("Updated Ticket IDs:", storedTicketIDs);
        }
    }

    // Check for new alerts every second
    setInterval(checkForNewAlerts, 1000);
})();
