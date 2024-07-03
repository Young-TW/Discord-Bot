import discord
from discord.ext import commands
import asyncio
import requests
from bs4 import BeautifulSoup
import json
import time

with open('setting.json', mode = 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot=commands.Bot(command_prefix = ".", intents = intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game("Discord")
    await bot.change_presence(status = discord.Status.idle, activity = game)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['WelcomeChannelID']))
    await channel.send(f'{member} Welcome to Young\'s server!')

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
    embed = discord.Embed(color = 0x009dff, title = f"倒數計時開始 剩下 {minute} 分鐘")
    msg = await ctx.send(embed = embed)
    time.sleep(60)
    while 1:
        minute = minute - 1
        if minute == 0:
            embed = discord.Embed(color = 0x009dff, title = "時間到!")
            await msg.edit(embed = embed)
            break
        embed = discord.Embed(color = 0x009dff, title = f"剩下 {minute} 分鐘")
        await msg.edit(embed = embed)
        time.sleep(60)

@bot.command()
async def p(ctx, number = None):
    if number is not None:
        await ctx.send(f"https://www.pixiv.net/artworks/{number}")
    else :
        await ctx.send("please input numbers")

async def get_img(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url,headers = headers)
    Burl = BeautifulSoup(r.text, 'html.parser')
    img_tags = Burl.find_all('img')
    for tag in img_tags:
        img_url = tag.get('src')
    return img_url

@bot.command()
async def n(ctx,number = None):
    c = ctx.channel.is_nsfw()
    if c is False:
        await ctx.send("This is not NSFW channel")
        return 1
    if number is None:
        await ctx.send("Please input number")
        return 1

    main_req = requests.get(f"https://nhentai.net/g/{number}/")
    pages_amount = BeautifulSoup(main_req.text, 'html.parser').find_all('span', class_ = "name")
    urls = []
    if number is not None:
        urls = await asyncio.gather(*[get_img(f"https://nhentai.net/g/{number}/{i}/") for i in range(1, int(pages_amount[-1].text)+1)])

    page = 0
    embed = discord.Embed(color = 0x009dff, title = "nhentai viewer", url = urls[0]).set_footer(text = "By young_tw").set_image(url = urls[0])
    message = await ctx.send(embed = embed)
    for i in ["◀", "▶"]:
        await message.add_reaction(i)
    def check(reaction, user):
        return user == ctx.author and reaction.message == message
    while 1:
        if(page + 1 > len(urls) - 1):
            embed = discord.Embed(color = 0x009dff, title = "nhentai viewer", description = "The end.").set_footer(text = "By young_tw")
            await message.edit(embed = embed)
            break

        reaction, user = await bot.wait_for("reaction_add", timeout = 60.0, check = check)
        if str(reaction) == "▶":
            page += 1
        elif str(reaction) == "◀":
            page -= 1

        await message.remove_reaction(reaction, user)
        embed = discord.Embed(color = 0x009dff, title = "nhentai viewer", url = urls[page]).set_footer(text = "By young_tw").set_image(url = urls[page])
        await message.edit(embed = embed)

@bot.command()
@commands.is_owner()
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command()
@commands.is_owner()
async def delete(ctx:commands.Context, number:int):
    await ctx.channel.purge(limit = number+1)

cha = None
@bot.command()
@commands.is_owner()
async def come(ctx):
    global cha
    cha = await ctx.author.voice.channel.connect()

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
async def rebooterror(ctx, error):
    await ctx.send("reboot failed")

bot.run(jdata['YoungBotTOKEN'])
