import discord
import discord.ext

def Embed(url,urls,page):
    embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=url)
    embed.set_footer(text="By Young#0001")
    embed.set_image(url=urls[page])
    return url,urls,page

def EmbedEnd():
    embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",description="The end.")
    embed.set_footer(text="By Young#0001")
    return 0