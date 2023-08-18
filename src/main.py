import os, sys
import discord
import asyncio
from discord.ext import commands


prefix = "?"
intents = discord.Intents.all()
activity = discord.Game(name='')
bot = commands.Bot(prefix, intents=intents, activity=None, status=None)

@bot.event
async def on_ready():
  os.system("clear")
  print(bot.user)
  await asyncio.sleep(10)
  await bot.tree.sync()

@bot.command()
async def bye(ctx):
  await ctx.channel.typing()
  os.remove("BOTCONDITION")
  sys.exit(0)

@bot.command()
async def update(ctx):
  await ctx.channel.send('booting up....')
  sys.exit(0)

@bot.tree.command(name="ping",description="pong pong")
async def ping(ctx):
  await ctx.response.pong()

bot.run(os.environ["TOKEN"])
