import discord
from discord.ext import commands, tasks  #這裡是discord.ext
import wmi
from discord import Guild, guild  #Guild定義在discord底下
import random
import copy

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

def mc_server_info():
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_infos = w.Sensor()
    data = {}
    for sensor in temperature_infos:
        if sensor.SensorType == u'Load':
            data[sensor.Name] = sensor.Value
    return data["CPU Total"], data["Memory"]

#######################################################################

@tasks.loop(minutes=1)  #每一分鐘執行一次
async def cpu():  #(剛剛那ㄍ程式要開著他用那個抓ㄉ)
    await bot.get_channel(777229420330352640).purge(limit=3)
    try:
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        data = {}
        for sensor in temperature_infos:
            if sensor.SensorType == u'Temperature':
                data[sensor.Name] = sensor.Value
        x = list(data.values())
        y = list(data.keys())
        del x[3]
        del y[3]
        channel = bot.get_channel(777229420330352640)
        cpu, ram = mc_server_info()
        embed = discord.Embed(
            title="電腦狀態",
            description=f"總RAM使用率:{int(ram)}%\n總CPU使用率:{int(cpu)}%")
        for i in range(len(x)):
            embed.add_field(name=y[i], value=str(x[i]) + "℃", inline=False)
        await channel.send(embed=embed)  #該function回傳你要的資料
    except:
        print("未開啟監控程式")

#######################################################################################
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game("Minecraft")
    await bot.change_presence(dnstatus=discord.Status.idle, activity=game)
    cpu.start()

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(754283081694969866)
    await channel.send(f'{member} join!')
x = 0
@bot.event
async def on_message(message) : 
    global x
    if (message.author.id in [429639993007538178, 613729851500658688, 434364344424464385, 498505540612259840] 
        and message.channel.id == 754283081694969866) :
        print(f"{message.author}佬的話:{message.content}")
        x+=1
        if x > 4 :
            await message.add_reaction(await message.guild.fetch_emoji(800230681660751872))
            x = 0

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(772290523481243648)
    await channel.send(f'{member} leave')

@bot.command()
async def n(ctx, number=None):
    if number != None:
        await ctx.send(f"https://nhentai.net/g/{number}/")
    else:
        await ctx.send("請輸入參數")

@bot.command()
async def w(ctx, number=None):
    if number != None:
        await ctx.send(f"https://wnacg.org/photos-index-aid-{number}.html/")
    else:
        await ctx.send("請輸入參數")

@bot.command()
async def p(ctx, number=None):
    if number != None:
        await ctx.send(f"https://www.pixiv.net/artworks/{number}")
    else:
        await ctx.send("請輸入參數")

@bot.command()
async def osu(ctx, *, nameid=None):
    if nameid != None:
        await ctx.send(f"https://osu.ppy.sh/users/{nameid}")
    else:
        await ctx.send("請輸入參數")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author}")

@bot.command()
async def osumap(ctx, number=None):
    if number != None:
        await ctx.send(f"https://osu.ppy.sh/beatmapsets/{number}#osu/")
    else:
        await ctx.send("請輸入參數")

@bot.command()
@commands.is_owner()
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command()
@commands.is_owner()
async def delete(ctx: commands.Context, number: int):
    await ctx.channel.purge(limit=number + 1)

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
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)}ms')

@bot.command()
async def music(ctx: commands.Context):
    w = await ctx.author.voice.channel.connect()
    w.play(
        discord.PCMVolumeTransformer(
            discord.FFmpegPCMAudio(
                "D:\\雲と幽霊.mp3",
                executable=
                "D:\\ffmpeg-N-99803-gbb6edf618a-win64-gpl-shared-vulkan\\bin\\ffmpeg.exe"
            ), 0.5))

@bot.command()
@commands.is_owner()
async def reboot(ctx):
    await ctx.send("```\n重啟.............\n```")
    await bot.close()

@reboot.error
async def rebooterror(ctx, error):
    await ctx.send("你不是我男友別想命令我重啟")

bot.run('NzcwOTA4MTUzNjEzMTIzNTg0.X5kaKg.29HnPAIeAeV919mCC8QriKSCnQs')
