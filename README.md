# picgame-notifier
Personal Reddit bot for subreddit /r/PictureGame to keep track of rounds and comments

The goal of this bot is to automatically notify users/players that a new round is up, as well as track comments from the most recent thread.
This saves you time from constantly refreshing the page and lets you do other things, both as a player and as a round host.


# Features

The bot refreshes every 20 seconds. (This is configurable.)

Notifications are sent both as a printout on the screen and as an auditory signal as a bell character (print('\a')).

In general, everything is printed out on the screen. The following is used to determine the sound:

* New round posted

* +correct messages

* If you are hosting the round, new comments as well. (You will need to configure the username to match yours, or else you will not receive audio notifications here.)

# Limitations 

Importantly, the scope of this project is NOT any of the following:

* answer open rounds

* automatically +correct correct answers

* post new rounds

* be an easy interface to otherwise look at the picture

Seriously, just load up /r/PictureGame if you need to do that. I don't want your login information, don't worry.

# Requirements
Python 3.x

PRAW
