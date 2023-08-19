import os, sys
import discord
import asyncio
import calmath
import json, swear
import random, aiohttp
from discord.ext import commands


prefix = "?"
intents = discord.Intents.all()
activity = discord.Game(name='')
bot = commands.Bot(prefix, intents=intents, activity=None, status=None)
global calc_mode, calc_chan
calc_mode = False
calc_chan = False

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
async def parrot(ctx, cols:int=None):
  if cols:
    await ctx.channel.send(content=str("<a:congaparrot:1142004332502450268>" * 5 * cols))
  else:
    await ctx.channel.send(content=str("<a:congaparrot:1142004332502450268>" * 5 ))
  await ctx.message.delete()

@bot.command()
async def waifu(ctx):
  url = 'https://api.waifu.im/search'
  params = {
      'included_tags': ['maid'],
      'height': '>=2000'
  }
  async with aiohttp.ClientSession() as session:
    async with session.get(url, params=params) as r:
      if r.status == 200:
        js = await r.json()
        await ctx.channel.send(js['images'][0]['url'])

@bot.command()
async def coocoolator(ctx):
  global calc_mode, calc_chan
  if calc_mode:
    calc_mode = False
    await ctx.reply("calculator mode off")
  else:
    calc_mode = True
    calc_chan = ctx.channel
    await ctx.reply("calculator mode on")

@bot.tree.command(name="ping",description="pong pong")
async def ping(ctx):
  await ctx.response.pong()

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  global calc_mode, calc_chan
  if calc_mode and message.channel == calc_chan:
    try:
      answer = calmath.coocoo(message.content)
      await message.reply(answer)
    except:
      pass
  if all(w in message.content.lower() for w in ["ni", "a", "gg"]):
    await message.delete()
  await bot.process_commands(message)

bot.run(os.environ["TOKEN"])
