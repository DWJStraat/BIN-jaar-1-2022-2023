import os
import discord
from dotenv import load_dotenv

load_dotenv
token = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    client.


client.run('MTA0OTk3NzA5ODUxODkzNzY4MA.G6HNDi.gKkbyzpI-DX87CQAoOjZ6LUrumLYdJ8v2BYptk')
