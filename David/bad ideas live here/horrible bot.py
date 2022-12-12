import discord
from discord import app_commands
import horrible_ideas as hi
import json
from tkinter.messagebox import showwarning

json = json.load(open('config.json'))

class app(discord.Client):
    def __init__(self):
        super().__init__(intents= discord.Intents.all())
        self.synced = False
        self.added = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        if not self.added:
            self.added = True
        print('Logged on as', self.user)

client = app()
tree = app_commands.CommandTree(client)

@tree.command(name='panic', description='Will make the computer beep and show a warning')
async def panic(interaction: discord.Interaction):
    await interaction.response.send_message('Panic!')
    print('Panic!')
    hi.panicPopUp()


client.run(json['token'])