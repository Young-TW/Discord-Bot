import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)

bot.run('Nzg2OTg2OTU0NDc4NTgzODU4.X9OYtw.5NdBWuahxDL-tBfrba2nQI-Q2ks')