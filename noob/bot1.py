import discord
from discord.ext import commands

intents = discord.Intents.all()
bot=commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def n(ctx,number=None):
    if number!=None:
        await ctx.send(f"https://nhentai.net/g/{number}/")
    else :
        await ctx.send("請輸入參數")

@bot.command()
async def w(ctx,number=None):
    if number!=None:
        await ctx.send(f"https://wnacg.org/photos-index-aid-{number}.html/")
    else :
        await ctx.send("請輸入參數")

@bot.command()
async def p(ctx,number=None):
    if number!=None:
        await ctx.send(f"https://www.pixiv.net/artworks/{number}")
    else :
        await ctx.send("請輸入參數")

@bot.command()
async def osu(ctx,nameid=None):
    if nameid!=None:
        await ctx.send(f"https://osu.ppy.sh/users/{nameid}")
    else :
        await ctx.send("請輸入參數")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author}")
cha=None

@bot.command()
async def come(ctx):
    global cha
    cha=await ctx.author.voice.channel.connect()

@bot.command()
async def bye(ctx):
    await cha.disconnect()


@bot.command()
async def music(ctx:commands.Context):
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
async def osumap(ctx,number=None):
    if number!=None:
        await ctx.send(f"https://osu.ppy.sh/beatmapsets/1224414#osu/{number}")
    else :
        await ctx.send("請輸入參數")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(754283081694969866)
    await channel.send(f'{member}join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(772290523481243648)
    await channel.send(f'{member}leave')

@bot.command()
async def ping(ctx):
    await ctx.send(F'{round(bot.latency*1000)}ms')

bot.run("NzcwOTA4MTUzNjEzMTIzNTg0.X5kaKg.29HnPAIeAeV919mCC8QriKSCnQs")