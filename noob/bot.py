import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author}")


bot.run('NzcwOTA4MTUzNjEzMTIzNTg0.X5kaKg.29HnPAIeAeV919mCC8QriKSCnQs')
