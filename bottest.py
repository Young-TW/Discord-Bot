import discord
from discord.ext import commands,tasks#這裡是discord.ext
from discord import Guild, guild#Guild定義在discord底下

intents = discord.Intents.all()
bot=commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    game = discord.Game("testing")
    await bot.change_presence(status=discord.Status.idle, activity=game)
#####################################################################################

@bot.command()
@commands.is_owner()
async def say(ctx,channel, *, msg):
    channel = bot.get_channel(channel)
    await ctx.send(msg)

#####################################################################################
bot.run('')

