
import disnake
from disnake.ext import commands
import json
import time

command_sync_flags = commands.CommandSyncFlags.default()

config = json.load(open("config.json"))

bot = commands.Bot(
    command_prefix=config["prefix"],
    intents=disnake.Intents.all()
)


@bot.slash_command(description="Spam")
async def spam(ctx, runs: int, sleep: int):
    for _ in range(runs):
        await ctx.send('sup')
        time.sleep(sleep)
    await ctx.send("Done")


bot.run(config["token"])
