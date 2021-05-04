import discord
from discord.ext import commands,tasks
from discord import Guild, guild
import random
import copy
import os
import requests
import bs4
import json

class Cog_Extention(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
