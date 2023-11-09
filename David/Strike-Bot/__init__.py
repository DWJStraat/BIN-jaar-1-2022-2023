import disnake
from disnake.ext import commands
import json

command_sync_flags = commands.CommandSyncFlags.default()

config = json.load(open("config.json"))

bot = commands.Bot(
    command_prefix=config["prefix"],
    intents=disnake.Intents.all()
)


@bot.slash_command(description="Strike")
async def strike(ctx, member: disnake.Member, reason: str):
    with open("strike.json", "r") as f:
        filedata = f.read()
    filedata = filedata.replace(',', ',\n')
    with open("strike.json", "w") as f:
        f.write(filedata)
    strikes = json.load(open("strike.json"))
    try:
        await ctx.send(f"Striked {member.mention} for {reason}")
        await member.send(f"You have been striked for {reason}")
        await member.send(f"You have been striked for {reason}")
        try:
            person_strikes = strikes[str(member.id)]
        except KeyError:
            strikes[str(member.id)] = {'total_strikes': 0}
            person_strikes = strikes[str(member.id)]
        strike_count = person_strikes["total_strikes"]
        strike_count += 1
        strikes[str(member.id)]["total_strikes"] = strike_count
        strikes[str(member.id)][str(strike_count)] = reason
    except Exception:
        sender = bot.get_user(216450866993954817)
        await ctx.send(f"Nice try. No. Striked {sender.mention} for {reason} x 999")
        member = sender
        hits = 999
        for _ in range(hits):
            try:
                person_strikes = strikes[str(member.id)]
            except KeyError:
                strikes[str(member.id)] = {'total_strikes': 0}
                person_strikes = strikes[str(member.id)]
            strike_count = person_strikes["total_strikes"]
            strike_count += 1
            strikes[str(member.id)]["total_strikes"] = strike_count
            strikes[str(member.id)][str(strike_count)] = reason
            json.dump(strikes, open("strike.json", "w"))





@bot.slash_command(description="get strikes")
async def get_strikes(ctx):
    strikes = json.load(open("strike.json"))
    output = ""
    for person in strikes:
        username = bot.get_user(int(person))
        output += f"{username} has {strikes[person]['total_strikes']} strikes\n"
    await ctx.send(output)

@bot.slash_command(description="show strikes")
async def show_strikes(ctx, member: disnake.Member):
    strikes = json.load(open("strike.json"))
    output = ""
    try:
        person_strikes = strikes[str(member.id)]
    except KeyError:
        strikes[str(member.id)] = {'total_strikes': 0}
        person_strikes = strikes[str(member.id)]
    strike_count = person_strikes["total_strikes"]
    output += f"{member} has {strike_count} strikes\n"
    for strike in person_strikes:
        if strike != "total_strikes":
            output += f"Strike {strike}: {person_strikes[strike]}\n"
    await ctx.send(output)

@bot.slash_command(description="give strikes")
async def give_strikes(member, reason):
    strikes = json.load(open("strike.json"))
    try:
        person_strikes = strikes[str(member.id)]
    except KeyError:
        strikes[str(member.id)] = {'total_strikes': 0}
        person_strikes = strikes[str(member.id)]
    strike_count = person_strikes["total_strikes"]
    strike_count += 1
    strikes[str(member.id)]["total_strikes"] = strike_count
    strikes[str(member.id)][str(strike_count)] = reason
    json.dump(strikes, open("strike.json", "w"))

@bot.slash_command(description="admin_strike")
async def admin_strike(ctx, member: disnake.Member, reason: str, strikes:int
= 0):
    strikes = json.load(open())

bot.run(config["token"])
