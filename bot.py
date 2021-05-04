import discord
from discord.ext import commands,tasks#這裡是discord.ext
import wmi
from discord import Guild, guild#Guild定義在discord底下
import psutil
import random
import copy
import os
import json

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot=commands.Bot(command_prefix=".",intents=intents)

def mc_server_info():
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_infos = w.Sensor()
    data={}
    for sensor in temperature_infos:
        if sensor.SensorType==u'Load':
            data[sensor.Name]=sensor.Value
    return data["CPU Total"],data["Memory"]

@tasks.loop(minutes=1)#每一分鐘執行一次
async def cpu():#(溫度監控程式要開)
    await bot.get_channel(777229420330352640).purge(limit=3)
    try:
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        data={}
        for sensor in temperature_infos:
            if sensor.SensorType==u'Temperature':
                data[sensor.Name]=sensor.Value
        x=list(data.values()) 
        y=list(data.keys())
        del x[3]
        del y[3]
        channel = bot.get_channel(777229420330352640)
        cpu,ram=mc_server_info()
        embed=discord.Embed(title="電腦狀態",description=
        f"總RAM使用率:{int(ram)}%\n總CPU使用率:{int(cpu)}%")
        for i in range(len(x)) :
            embed.add_field(name=y[i],value=str(x[i])+"℃",inline=False)
        await channel.send(embed=embed)#該function回傳你要的資料
    except :
        print("未開啟監控程序")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game("Discord")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    cpu.start()

class Main():

    @bot.event
    async def on_member_join(self,member):
        channel = bot.get_channel(754283081694969866)
        await channel.send(f'{member} Wellcome to UwU!')

    @bot.event
    async def on_member_remove(self,member):
        channel = bot.get_channel(772290523481243648)
        await channel.send(f'{member} leave')

    @bot.command()
    async def ping(self,ctx):
        await ctx.send(F'{round(bot.latency*1000)}ms')

    @bot.command()
    async def osumap(self,ctx,number=None):
        if number!=None:
            await ctx.send(f"https://osu.ppy.sh/beatmapsets/{number}#osu/")
        else :
            await ctx.send("請輸入參數")

    @bot.command()
    @commands.is_owner()
    async def say(self,ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @bot.command()
    @commands.is_owner()
    async def delete(self,ctx:commands.Context,number:int):
        await ctx.channel.purge(limit=number+1)

    cha=None
    @bot.command()
    @commands.is_owner()
    async def come(self,ctx):
        global cha
        cha=await ctx.author.voice.channel.connect()

    @bot.command()
    @commands.is_owner()
    async def bye(self,ctx):
        await cha.disconnect()

    @bot.command()
    async def music(self,ctx:commands.Context):
        w=await ctx.author.voice.channel.connect()
        w.play  (discord.PCMVolumeTransformer
                    (
                    discord.FFmpegPCMAudio
                        ("D:\\雲と幽霊.mp3",
                            executable="D:\\ffmpeg-N-99803-gbb6edf618a-win64-gpl-shared-vulkan\\bin\\ffmpeg.exe"
                        ),0.5
                    )
                )
            
    @bot.command()
    @commands.is_owner()
    async def reboot(self,ctx):
        await ctx.send("```\n重啟.............\n```")
        await bot.close()
    @reboot.error
    async def rebooterror(self,ctx,error):
        await ctx.send("非bot擁有者")

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

        for i in range(len(repeat)) :
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

class botload():
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

bot.run(jdata['YoungBotTOKEN'])
