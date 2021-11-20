import discord
from discord.ext import commands
import json
import time

with open('../../setting.json', mode='r',encoding='utf8') as jfile:
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
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}ms')

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
  
# @bot.command()
# @commands.is_owner()
# async def reboot(ctx):
#     await ctx.send("```\nreboot.............\n```")
#     await bot.close()
# @reboot.error
# async def rebooterror(ctx,error):
#     await ctx.send("你不是我男友別想命令我重啟")

bot.run(jdata['YoungBotTOKEN'])