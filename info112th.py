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

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}ms')

@bot.command()
async def p(ctx,number=None):
    if number!=None:
        await ctx.send(f"https://www.pixiv.net/artworks/{number}")
    else :
        await ctx.send("please input numbers")

@bot.command()
async def n(ctx,number=None,page=0):
    if number!=None:
        text = f"https://nhentai.net/g/{number}/"
        hentai = requests.get(text)
        data = bs4.BeautifulSoup(hentai.text, "lxml").select("#thumbnail-container img")
        urls = [i["src"] for i in data if not i["src"].startswith("data")]
        embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=urls[0])
        embed.set_footer(text=" By Young#0001")
        embed.set_image(url=urls[0])
        message=await ctx.send(embed=embed)
        for i in ["◀","▶"]:
            await message.add_reaction(i)
        def check(reaction, user):
            return user == ctx.author and reaction.message == message
        while 1 :
            if(page + 1 > len(urls) - 1):
                embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",description="The end.")
                embed.set_footer(text="By Young#0001")
                await message.edit(embed=embed)
                break
            reaction, user = await bot.wait_for("reaction_add",timeout=60.0,check=check)
            if str(reaction) ==  "▶":
                page+=1
            elif str(reaction) == "◀":
                page-=1
            await message.remove_reaction(reaction,user)
            embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=f"{urls[page]}")
            embed.set_footer(text="By Young#0001")
            embed.set_image(url=f"{urls[page]}")
            await message.edit(embed=embed)
    else:
        await ctx.send(f"please input numbers")

@bot.command()
async def w(ctx,number=None):
    if number!=None:
        await ctx.send(f"https://www.wnacg.org/photos-index-aid-{number}.html")
    else :
        await ctx.send("please input numbers")

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
async def delele(ctx:commands.Context,number:int):
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
    await ctx.send("重啟錯誤")

bot.run(jdata['info112thTOKEN'])