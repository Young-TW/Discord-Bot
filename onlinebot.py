import discord
from discord.ext import commands, tasks
from discord import Guild, channel, guild
import random
import copy

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
#    game = discord.Game("game")
    await bot.change_presence(status=discord.Status.idle)#, activity=game

#user's id = {userid} #young's id = 434364344424464385

user = bot.get_user(434364344424464385)#指定使用者:
@bot.event
async def on_user_update(ctx,status):#當使用者上線
    status == user.status.idle
    ctx = bot.get_channel(802939773101670430)#指定訊息傳送頻道
    await ctx.send(f'user is online!')#傳送使用者上線訊息

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author}!')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)}ms')

@bot.command()
@commands.is_owner()
async def reboot(ctx):
    await ctx.send("```\n重啟\n```")
    await bot.close()
@reboot.error
async def rebooterror(ctx, error):
    await ctx.send("騙人的吧")

bot.run("ODAyOTM3MjgwMjMwNDU3Mzc1.YA2fnQ.Wa38G0gjdVifYKFAHGlXpKauJ9s")