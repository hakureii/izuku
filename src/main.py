import os, sys
import discord
import asyncio
import math
from discord.ext import commands


prefix = "?"
intents = discord.Intents.all()
activity = discord.Game(name='')
bot = commands.Bot(prefix, intents=intents, activity=None, status=None)
global calc_mode
calc_mode = False

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

@bot.command()
async def parrot(ctx):
  await ctx.channel.send("<a:congaparrot:1142004332502450268>")

@bot.command()
async def calc(ctx):
  global calc_mode
  if calc_mode:
    calc_mode = True
    await ctx.reply("calculator mode on")
  else:
    calc_mode = False
    await ctx.reply("calculator mode off")

@bot.tree.command(name="ping",description="pong pong")
async def ping(ctx):
  await ctx.response.pong()

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  global calc_mode
  if calc_mode:
    answer = math.calc(message.content)
    await message.reply(answer)


bot.run(os.environ["TOKEN"])
