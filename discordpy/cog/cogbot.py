import discord
from discord.ext import commands,tasks
from discord import Guild, guild
import random
import copy
import os
import requests
import bs4
import json

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot=commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game("Discord")
    await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['WelcomeChannelID']))
    await channel.send(f'{member} Welcome to UwU!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['LeaveChannelID']))
    await channel.send(f'{member} leave')

@bot.command()
async def osumap(ctx,number=None):
    if number!=None:
        await ctx.send(f"https://osu.ppy.sh/beatmapsets/{number}#osu/")
    else :
        await ctx.send("please input numbers")

@bot.command()
@commands.is_owner()
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command()
@commands.is_owner()
async def delete(ctx:commands.Context,number:int):
    await ctx.channel.purge(limit=number+1)

cha=None
@bot.command()
@commands.is_owner()
async def come(ctx):
    global cha
    cha=await ctx.author.voice.channel.connect()

@bot.command()
@commands.is_owner()
async def bye(ctx):
    await cha.disconnect()
  
@bot.command()
@commands.is_owner()
async def reboot(ctx):
    await ctx.send("```\nreboot.............\n```")
    await bot.close()
@reboot.error
async def rebooterror(ctx,error):
    await ctx.send("你不是我男友別想命令我重啟")

class load():
    @bot.command()
    async def load(self,ctx,extension):
        bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'loaded {extension} done.')

    @bot.command()
    async def unload(self,ctx,extension):
        bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f'unloaded {extension} done.')

    @bot.command()
    async def reload(self,ctx,extension):
        bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'reloaded {extension} done.')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    pass
bot.run(jdata['TestBotTOKEN'])