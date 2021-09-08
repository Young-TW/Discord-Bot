import discord
from discord.ext import commands,tasks#這裡是discord.ext
from discord import Guild, guild#Guild定義在discord底下
import random
import copy
import os
import requests
import bs4
from bs4 import BeautifulSoup
import json
import time

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
async def p(ctx,number=None):
    if number is not None:
        await ctx.send(f"https://www.pixiv.net/artworks/{number}")
    else :
        await ctx.send("please input numbers")

@bot.command()
async def n(ctx,number=None,page=0):
    c = ctx.channel.is_nsfw()
    if c is False:
        await ctx.send("This is not NSFW channel")
    else:
        urls = []
        def saveUrlIndex(index):
            urls.append(index)
        if number is not None:
            page = 0
            while 1:
                url = f"https://nhentai.net/g/{number}/{page+1}/"
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
                r = requests.get(url,headers=headers)
                Burl = BeautifulSoup(r.text, 'html.parser')
                img_tags = Burl.find_all('img')
                for tag in img_tags:
                    imgUrl = tag.get('src')
                saveUrlIndex(imgUrl)
                if imgUrl == "https://static.nhentai.net/img/logo.090da3be7b51.svg":
                    break
                page += 1
            page = 0
            embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=url)
            embed.set_footer(text="By Young#0001")
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
                embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=url)
                embed.set_footer(text="By Young#0001")
                embed.set_image(url=urls[page])
                await message.edit(embed=embed)
        else:
            await ctx.send(f"Please input number")

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

class Sokoban():
    def __init__(self,difficulty):
        if difficulty==None :
            high=10
            width=10
            number=1
        else :
            high=difficulty*10
            width=difficulty*10
            number=difficulty
        self.map1=[[]]*high
        self.box=[]
        repeat=[]
        for i in range(high):
            if i == 0 or i == high-1 : self.map1[i] = ["🔲"]*width
            else:
                self.map1[i]=[""]*width
                for x in range(width) :
                    if x == 0 or x == width-1 :self.map1[i][x] = "🔲"
                    else : self.map1[i][x]="⬛"
        while 1 :
            if [random.randint(1,high-2),random.randint(1,width-2)] not in repeat :
                repeat.append([random.randint(2,high-3),random.randint(2,width-3)])
            if len(repeat)==2+number:
                break

        for i in range(len(repeat)):
            if i == 0 :
                self.player=repeat[0]
            elif i == 1 :
                self.end=repeat[1]
            else :
                self.box.append(repeat[i])
    def userinput(self,x):
        y={"🔼":self.up,"🔽":self.down,"◀":self.left,"▶":self.right}
        y[x]()
    def up(self):
        if self.map1[self.player[0]-1][self.player[1]] != "🔲" :
            if ([self.player[0]-1,self.player[1]] !=self.end) and ([self.player[0]-1,self.player[1]] not in self.box):#自己移動
                self.player[0]-=1
            elif ([self.player[0]-1,self.player[1]] in self.box) :#推箱子
                box=self.box[self.box.index([self.player[0]-1,self.player[1]])]
                if self.map1[box[0]-1][box[1]] !="🔲" :
                    if [box[0]-1,box[1]] ==self.end:
                        del self.box[self.box.index([self.player[0]-1,self.player[1]])]
                    else :
                        self.box[self.box.index([self.player[0]-1,self.player[1]])][0]-=1
                    self.player[0]-=1

    def down(self):
        if self.map1[self.player[0]+1][self.player[1]] != "🔲" :
            if ([self.player[0]+1,self.player[1]] !=self.end) and ([self.player[0]+1,self.player[1]] not in self.box):#自己移動
                self.player[0]+=1
            elif ([self.player[0]+1,self.player[1]] in self.box) :#推箱子
                box=self.box[self.box.index([self.player[0]+1,self.player[1]])]
                if self.map1[box[0]+1][box[1]] !="🔲" :
                    if [box[0]+1,box[1]] ==self.end:
                        del self.box[self.box.index([self.player[0]+1,self.player[1]])]
                    else :
                        self.box[self.box.index([self.player[0]+1,self.player[1]])][0]+=1
                    self.player[0]+=1
    def left(self):
        if self.map1[self.player[0]][self.player[1]-1] != "🔲" :
            if ([self.player[0],self.player[1]-1] !=self.end) and ([self.player[0],self.player[1]-1] not in self.box):#自己移動
                self.player[1]-=1
            elif ([self.player[0],self.player[1]-1] in self.box) :#推箱子
                box=self.box[self.box.index([self.player[0],self.player[1]-1])]
                if self.map1[box[0]][box[1]-1] !="🔲" :
                    if [box[0],box[1]-1] ==self.end:
                        del self.box[self.box.index([self.player[0],self.player[1]-1])]
                    else :
                        self.box[self.box.index([self.player[0],self.player[1]-1])][1]-=1
                    self.player[1]-=1
    def right(self):
        if self.map1[self.player[0]][self.player[1]+1] != "🔲" :
            if ([self.player[0],self.player[1]+1] !=self.end) and ([self.player[0],self.player[1]+1] not in self.box):#自己移動
                self.player[1]+=1
            elif ([self.player[0],self.player[1]+1] in self.box) :#推箱子
                box=self.box[self.box.index([self.player[0],self.player[1]+1])]
                if self.map1[box[0]][box[1]+1] !="🔲" :
                    if [box[0],box[1]+1] ==self.end:
                        del self.box[self.box.index([self.player[0],self.player[1]+1])]
                    else :
                        self.box[self.box.index([self.player[0],self.player[1]+1])][1]+=1
                    self.player[1]+=1
    def mapprint(self):
        map2=copy.deepcopy(self.map1)
        map2[self.player[0]][self.player[1]]="🌝"#人物
        map2[self.end[0]][self.end[1]]="🟨"#終點
        for i in self.box :
            map2[i[0]][i[1]]="🔳"#箱子
        if not len(self.box):return ("\n".join(["".join(i) for i in map2]),True)
        else :return ("\n".join(["".join(i) for i in map2]),False)


class Game(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command()
    async def sokoban(self,ctx:commands.Context,level:int=None):
        ww=Sokoban(level)
        text,_=ww.mapprint()
        embed=discord.Embed(title="sokoban",description=f"```\n{text}\n```")
        message=await ctx.send(embed=embed)
        for i in ["◀","🔼","🔽","▶","⏹"]:
            await message.add_reaction(i)
        def check(reaction, user):
            return user == ctx.author and reaction.message == message 
        while 1 :
            reaction, user = await self.bot.wait_for("reaction_add",timeout=60.0,check=check)
            await message.remove_reaction(reaction,user)
            if str(reaction)=="⏹":break
            ww.userinput(str(reaction))
            text,t=ww.mapprint()
            embed=discord.Embed(title="sokoban",description=f"```\n{text}\n```")       
            await message.edit(embed=embed)
            if t :
                await ctx.send("過關")
                break
bot.add_cog(Game(bot))

bot.run(jdata['YoungBotTOKEN'])