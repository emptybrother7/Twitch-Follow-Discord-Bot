import os
import discord
import json
import requests
from discord.ext import tasks

# Your Twitch Dev API IDs
twitch_client_id = '<Client ID>'
twitch_client_secret = '<Client Secret ID>'

def get_twitch_access_token():
    url = "https://id.twitch.tv/oauth2/token"
    payload = {
        "client_id": twitch_client_id,
        "client_secret": twitch_client_secret,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, params=payload)
    data = json.loads(response.text)
    return data["access_token"]

twitch_access_token = get_twitch_access_token()

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)

# Your Twitch user ID
twitch_user_id = '<Twitch User ID>'

# Your Discord bot token
discord_bot_token = '<Discord Bot Token>'

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    update_status.start()

def get_follower_count():
    url = f"https://api.twitch.tv/helix/users/follows?to_id={twitch_user_id}"
    headers = {
        "Client-ID": twitch_client_id,
        "Authorization": f"Bearer {twitch_access_token}"
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data["total"]

@tasks.loop(minutes=20)
async def update_status():
    followers = get_follower_count()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{followers} followers"))

update_status.before_loop(client.wait_until_ready)
client.run(discord_bot_token)