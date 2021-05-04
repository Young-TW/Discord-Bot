import discord
from discord.ext import commands,tasks
import time
import json

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot=commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game("testing")
    await bot.change_presence(status=discord.Status.idle, activity=game)
#####################################################################################
@bot.command()
async def say(ctx, *, msg):
    userid = discord.user_id()
    if userid == (int(jfile['Young_ID']) or int(jfile['Rou_ID'])):
        await ctx.message.delete()
        await ctx.send(msg)
    else:
        await ctx.send("Authority Error")

#####################################################################################
bot.run(jdata['TestBotTOKEN'])

