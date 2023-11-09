import discord
from discord import app_commands
from BingoClass import Bingo


class BingoClient(discord.Client):
    def __init__(self, intents=discord.Intents.all()):
        super().__init__(intents=intents)
        self.synced = False
        self.added = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        if not self.added:
            self.added = True
        print(f'{client.user} has connected to Discord!')


client = BingoClient()
tree = app_commands.CommandTree(client)


@tree.command(name='bingobuild', description='Creates a bingo game')
@discord.app_commands.describe(ids='The id of the game')
async def bingobuild(interaction: discord.Interaction, ids: str):
    game = Bingo(ids)
    game.createGame()
    game.save()
    await interaction.response.send_message(
        f'Created a bingo game for {interaction.user.name}')


@tree.command(name='bingodraw',
              description='Draws a number from the list of numbers')
@discord.app_commands.describe(numbers='Numbers to be drawn',
                               ids='ID of the bingo game')
async def bingodraw(interaction: discord.Interaction, ids: str, numbers: int):
    game = Bingo(ids)
    game.load()
    number = game.drawNumbers(numbers)
    game.save()
    await interaction.response.send_message(
        f'The numbers {number} have been drawn')


@tree.command(name='bingoadd',
              description='Adds a number to the list of numbers')
@discord.app_commands.describe(numbers='Numbers to be added',
                               ids='ID of the bingo game')
async def bingoadd(interaction: discord.Interaction, ids: str, numbers: int):
    game = Bingo(ids)
    game.load()
    game.addNumbers(numbers)
    game.save()
    await interaction.response.send_message(
        f'The numbers {numbers} have been added')


@tree.command(name='bingoremove',
              description='Removes a number from the list of numbers')
@discord.app_commands.describe(numbers='Numbers to be removed',
                               ids='ID of the bingo game')
async def bingoremove(interaction: discord.Interaction, ids: str,
                      numbers: int):
    game = Bingo(ids)
    game.load()
    game.removeNumbers(numbers)
    game.save()
    await interaction.response.send_message(
        f'The numbers {numbers} have been removed')


@tree.command(name='bingoprint',
              description='Prints the list of numbers')
@discord.app_commands.describe(ids='ID of the bingo game')
async def bingoprint(interaction: discord.Interaction, ids: str):
    game = Bingo(ids)
    game.load()

    await interaction.response.send_message(
        f'The numbers are {game.printNumbers()}')


@tree.command(name='createcard',
              description='Creates a bingo card')
@discord.app_commands.describe(ids='ID of the bingo game')
async def createcard(interaction: discord.Interaction, ids: str):
    game = Bingo(ids)
    game.load()
    card, seed = game.generateCard()
    game.save()
    await interaction.response.send_message(
        file=discord.File(fp=f'card_{game.name}opdracht_2{seed}.jpg'))
    await interaction.response.send_message(
        f'Created a bingo card for {interaction.user.name}')


@tree.command(name='showcard',
              description='Shows a bingo card')
@discord.app_commands.describe(ids='ID of the bingo game', seed='Seed')
async def showcard(interaction: discord.Interaction, ids: str, seed: int):
    await interaction.response.send_message(
        file=discord.File(fp=f'card_{ids}opdracht_2{seed}.jpg'))


client.run(
    'MTA0OTk3NzA5ODUxODkzNzY4MA.G6HNDi.gKkbyzpI-DX87CQAoOjZ6LUrumLYdJ8v2BYptk')
