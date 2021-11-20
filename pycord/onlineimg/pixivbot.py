@bot.command()
async def p(ctx,number=None):
    if number is not None:
        await ctx.send(f"https://www.pixiv.net/artworks/{number}")
    else :
        await ctx.send("please input numbers")
