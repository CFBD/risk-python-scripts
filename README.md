# Risk Python Scripts
This repo is intended to to be a library of generic Python scripts for College Football Risk. The primary purpose is to give leadership of teams appropriate resources to organize and recruit, particularly if the team has lacked much organization in the past.

## General Reddit Notification (general_reddit_notification.py)

This script can be used to send out a general notification via reddit PMs. The script requires a CSV files which it uses to read the list of players to message. The CSV file should contain at least one column of valid reddit usernames with a "player" header.

This script is fault tolerant and will continue to process the batch of players, even if one of the messages fails. The script will output two text files denoting which players were successfully messages and which failed.

Required fill ins:

* CLIENT_ID - Reddit client id obtained from the Reddit development console
* CLIENT_SECRET - Reddit client secret obtained from the Reddit development console
* APP_NAME - used in the user-agent string and must be unique
* APP_VERSION - used in the user-agent string
* USERNAME - Username of account used for sending PMs
* PASSWORD - Password of account used for sending PMs
* TEAM - Name of team
* PLACE_MESSAGE_HERE - Contents of message