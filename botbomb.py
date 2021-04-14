import discord
from discord.ext import commands, tasks  #這裡是discord.ext
from discord import Guild, channel, guild  #Guild定義在discord底下
import random
import copy

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event()
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    channellist = bot.get_all_channels
    print(channellist)
#    return 

@bot.command()
async def b(ctx,cha,msg):
    channel = bot.get_channel(783704087740809266,783704065849688154)#channel = channellist
    while 1:
        await channel.send("@everyone")

@bot.command()
@commands.is_owner()
async def reboot(ctx):
    await ctx.send("```\n重啟\n```")
    await bot.close()
@reboot.error
async def rebooterror(ctx, error):
    await ctx.send("錯誤 非bot擁有者")

bot.run("ODAyMDU2NzM4ODMyMjUyOTQw.YAprjA.04G7D_FwlwSY9AQlmtZZuWzAiHU")