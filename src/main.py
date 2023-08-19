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

@bot.event
async def on_message(message):
  if message.channel == discord.utils.get(bot.get_all_channels(), id=1137829767173910538):
    if message.author != bot.user:
      await message.delete()
  if 'gay' in message.content.lower():
    await message.add_reaction('\U0001f595')
  await bot.process_commands(message)


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

@bot.tree.command(name="emoji", description="send animated emotes without nitro!")
async def emoji(ctx: discord.Interaction, name:str):
  webhook = await ctx.channel.create_webhook(name=ctx.user.display_name)
  await webhook.send(str(name), username=ctx.user.display_name, avatar_url=ctx.user.avatar)
  webhooks = await ctx.channel.webhooks()
  for webhook in webhooks:
    await webhook.delete()
    await ctx.response.send_message("done.!", ephemeral=True)

bot.run(os.environ["TOKEN"])
