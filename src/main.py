import os, sys
import discord
from discord.ext import commands


prefix = "?"
intents = discord.Intents.all()
activity = discord.Game(name='')
bot = commands.Bot(prefix, intents=intents, activity=None, status=None)

@bot.event
async def on_ready():
  os.system("clear")
  print(bot.user)

@bot.command()
async def bye(ctx):
  await ctx.channel.typing()
  os.remove("BOTCONDITION")
  sys.exit(0)

bot.run(os.environ["TOKEN"])
