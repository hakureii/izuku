#!/usr/bin/env python3

# import modules
import os, sys
import discord
import asyncio
import calmath
import requests
import json, swear
import random, aiohttp
from discord.ext import commands


# setup vars and alias
prefix = ["?", "izu"]
intents = discord.Intents.all()
activity = discord.Game(name='Snake and Ladders')
bot = commands.Bot(prefix, intents=intents, activity=activity, status=None)
global calc_mode, calc_chan
calc_mode = False
calc_chan = False



# on ready event [ triggers on bot login ]
@bot.event
async def on_ready():
  os.system("clear")
  print(bot.user)



# on message event [ triggers when someone sends any message
@bot.event
async def on_message(message):
  if message.channel == discord.utils.get(bot.get_all_channels(), id=1137829767173910538) and message.author != bot.user:
    await message.delete()
  if 'gay' in message.content.lower():
    await message.add_reaction('\U0001f595')
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



# bot commands [ commands works with prefix ]
@bot.command()
async def bye(ctx):
  await ctx.channel.typing()
  os.remove("BOTCONDITION")
  sys.exit(0)

@bot.command()
async def update(ctx):
  await ctx.channel.send("initializing update and reboot...")
  sys.exit(0)

@bot.command()
async def applist(ctx):
  await ctx.channel.typing()
  try:
    await bot.tree.sync()
    await ctx.channel.send(content='i think it\'s done !')
  except:
    await ctx.channel.send(content='feels like it failed zzZ')

@bot.command()
async def parrot(ctx, cols:int=None):
  if cols:
    await ctx.channel.send(content=str("<a:congaparrot:1142004332502450268>" * cols))
  else:
    await ctx.channel.send(content=str("<a:congaparrot:1142004332502450268>" * 5 ))
  await ctx.message.delete()

@bot.command()
async def search(ctx, tgs:str = None):
  if tgs == None:
    return 0
  else:
    res = requests.get(url=f"https://yande.re/post.json?tags={tgs}")
    if res.status_code == 200:
      data = res.json()
      n = int(random.choice(range(len(data))))
      await ctx.channel.send(content=data[n]["file_url"])
    else:
      await ctx.channel.send(content="no content found")

@bot.command()
async def hunt(ctx, category:str = None):
  cat_list = ["waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry", "hug", "awoo", "kiss", "lick", "pat", "smug", "bonk", "yeet", "blush", "smile", "wave", "highfive", "handhold", "nom", "bite", "glomp", "slap", "kill", "kick", "happy", "wink", "poke", "dance", "cringe"]
  if category:
    if category in cat_list:
      req = requests.get(url=f"https://api.waifu.pics/sfw/{category}").json()
      await ctx.channel.send(content=req["url"])
    else:
      helper = ""
      for cat in cat_list:
        helper += cat + " "
      await ctx.channel.send(content=helper)
  else:
    category = random.choice(cat_list)
    req = requests.get(url=f"https://api.waifu.pics/sfw/{category}").json()
    await ctx.channel.send(content=req["url"])

@bot.command()
async def waifu(ctx):
  url = 'https://api.waifu.im/search'
  params = {
      'included_tags': ['maid']
  }
  async with aiohttp.ClientSession() as session:
    async with session.get(url, params=params) as r:
      if r.status == 200:
        data = await r.json()
        tags = ""
        for n in range(len(data['images'][0]['tags'])):
          tags += data['images'][0]['tags'][n]['name'] + " "
        embed = discord.Embed(title='', description=f'{tags}', color=None)
        embed.set_image(url=f"{data['images'][0]['url']}")
        await ctx.channel.send(embed=embed)

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

@bot.event
async def on_command_error(ctx, error):
	chan = discord.utils.get(bot.get_all_channels(), id=1137829767173910538)
	embed = discord.Embed(title=f'{ctx.command}',
                          description=f'{error}',
                          color=0xecce8b)
	await chan.send(embed=embed)



# slash commands aka application commands
@bot.tree.command(name="ping",description="pong pong")
async def ping(ctx):
  await ctx.response.pong()

@bot.tree.command(name="emoji", description="send animated emotes without nitro!")
async def emoji(ctx: discord.Interaction, name:str):
  webhook = await ctx.channel.create_webhook(name=ctx.user.display_name)
  await webhook.send(str(name), username=ctx.user.display_name, avatar_url=ctx.user.avatar)
  webhooks = await ctx.channel.webhooks()
  for webhook in webhooks:
    await webhook.delete()
    await ctx.response.send_message("done.!", ephemeral=True)



# starting up the bot ....
bot.run(os.environ["TOKEN"])
