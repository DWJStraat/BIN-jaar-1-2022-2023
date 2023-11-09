import discord
from discord import app_commands
import Afvinkopdracht5_class as a5
import json

json = json.load(open('config.json'))


class BinfFive(discord.Client):
    def __init__(self, intents=discord.Intents.all()):
        super().__init__(intents=intents)
        self.synced = False
        self.added = False

    async def on_ready(self):
        """
        This function is called when the bot is ready to be used.
        """
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        if not self.added:
            self.added = True
        print('Logged on as', self.user)

    async def on_message(self, message):
        """
        This function is called when a message is sent in a channel the bot has
        Parameters
        ----------
        message
            The message that was sent

        Returns
        -------
        None
        """
        if message.author == self.user:
            return
        if message.content == 'upload':
            await message.channel.send('Uploading next file...')
            await message.attachments[0].save('test.fasta')
            await message.channel.send('File uploaded')


client = BinfFive()
tree = app_commands.CommandTree(client)


@tree.command(name='analyze', description='Analyzes a fasta file')
async def analyze(interaction: discord.Interaction):
    objectlist = []
    list = a5.multiple_fna('test.fasta')
    for i in list:
        templist = i.split('|')
        tempobject = a5.fasta()
        print(templist)
        tempobject.setHeader(templist[0])
        tempobject.setSequence(templist[1])
        objectlist.append(tempobject)
    highestgc = 0
    print(objectlist)
    highestgcobject = None
    for j in objectlist:
        tempDNA = a5.sequence(j.getSequence())
        if tempDNA.getGcPercent() > highestgc:
            highestgc = tempDNA.getGcPercent()
            highestgcobject = j
    await interaction.response.send_message(
        f'The highest GC content is {highestgc * 100:.2f}% in '
        f'{highestgcobject.header}.')
    highestgcobjectdna = a5.DNA(highestgcobject.getSequence())
    print(f'Header: {highestgcobject.getHeader()}\nGC percentage: '
          f'{highestgc * 100:.2f}%\nTranscript: '
          f'{highestgcobjectdna.getTranscript()}\nLength: '
          f'{highestgcobjectdna.getLength()}')


client.run(
    json['token'])
