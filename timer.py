import discord
from discord.ext import commands,tasks
import time
import json

with open('./setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot=commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game("counting")
    await bot.change_presence(status=discord.Status.idle, activity=game)
#####################################################################################

@bot.command()
async def countdown(ctx, hour, minute):
    hour = int(hour)
    minute = int(minute)
    minute = minute + (hour*60)
    embed=discord.Embed(color=0x009dff,title=f"倒數計時開始 剩下 {minute} 分鐘")
    msg = await ctx.send(embed=embed)
    time.sleep(60)
    while 1:
        minute = minute - 1
        if minute == 0:
            embed=discord.Embed(color=0x009dff,title="時間到!")
            await msg.edit(embed=embed)
            break
        embed=discord.Embed(color=0x009dff,title=f"剩下 {minute} 分鐘")
        await msg.edit(embed=embed)
        time.sleep(60)

#####################################################################################
bot.run(jdata['HackathonTOKEN'])
#hackathon