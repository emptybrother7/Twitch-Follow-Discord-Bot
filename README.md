# Twitch Follower Count Discord Bot

This repository contains a simple Python script that creates a Discord bot to display the number of Twitch followers of a specified user in the bot's status. The bot updates the follower count every 20 minutes.

## Features

- Get Twitch follower count of a specific user
- Update the bot's status with the current follower count every 20 minutes

## Requirements

- Python 3.6 or higher
- A Twitch Developer Application with Client ID and Client Secret
- A Discord bot with a bot token

## Installation

1. Clone this repository:  

```
https://github.com/emptybrother7/Twitch-Follow-Discord-Bot.git
```  

2. Install `discord.py` library:  

```
pip install discord.py
```  

3. Replace the following placeholders in the script with your own values:

- `<Client ID>`: Your Twitch Developer Application Client ID
- `<Client Secret ID>`: Your Twitch Developer Application Client Secret
- `<Twitch User ID>`: The Twitch user ID of the account you want to track followers for
- `<Discord Bot Token>`: Your Discord bot token

4. Run the script:  

```
python TFDB.py
```


