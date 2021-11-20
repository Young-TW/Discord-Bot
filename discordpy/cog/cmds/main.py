import discord
from discord.ext import commands,tasks
from discord import Guild, guild
import random
import copy
import os
import requests
import bs4
import json
from core.classes import Cog_Extention

class main(Cog_Extention):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}ms')

def setup(bot):
    bot.add_cog(main(bot))