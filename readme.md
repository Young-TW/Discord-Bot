### Discord Bots

<!-->
#########################################################################
#@bot.event
#async def on_member_connect(member, channel):
#    channel = bot.get_channel()
#    #2
#    await guild.create_voice_channel(name= "{author}休息室",overwrites=None, reason=None)
#    #3

#18.58

#773161691729887252
#await move_to(channel)

#1.偵測成員進入［開個人房］
#2.在［開個人房］底下新增一個語音頻道
#名稱=(“｛author}休息室”)
#3.將成員從［開個人房］移動到［(“｛author}休息室”)］
#4.當頻道無人連接時刪除該頻道

#cha=None
#@bot.command()
#async def come(ctx):
#    global cha
#    cha=await ctx.author.voice.channel.connect()

#@bot.command()
#async def bye(ctx):
#    await cha.disconnect()

#channel = bot.get_channel()
#await channel.clone(name = "{author}休息室")

#    pass#python不允許縮排底下沒東西沒要執行就打pass

#########################################################################
#@bot.loop(minutes=20)
#async def dcserver(ctx):
#    await bot.get_channel(777229420330352640)
#    await ctx.send(f"discord.gg/H4jJFZb")
#########################################################################
