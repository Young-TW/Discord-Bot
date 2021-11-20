
@bot.command()
async def n(ctx,number=None,page=0):
    c = ctx.channel.is_nsfw()
    if c is False:
        await ctx.send("This is not NSFW channel")
    else:
        urls = []
        def saveUrlIndex(index):
            urls.append(index)
        if number is not None:
            page = 0
            while 1:
                url = f"https://nhentai.net/g/{number}/{page+1}/"
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
                r = requests.get(url,headers=headers)
                Burl = BeautifulSoup(r.text, 'html.parser')
                img_tags = Burl.find_all('img')
                for tag in img_tags:
                    imgUrl = tag.get('src')
                saveUrlIndex(imgUrl)
                if imgUrl == "https://static.nhentai.net/img/logo.090da3be7b51.svg":
                    break
                page += 1
            page = 0
            embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=url)
            embed.set_footer(text="By Young#0001")
            embed.set_image(url=urls[0])
            message=await ctx.send(embed=embed)
            for i in ["◀","▶"]:
                await message.add_reaction(i)
            def check(reaction, user):
                return user == ctx.author and reaction.message == message
            while 1 :
                if(page + 1 > len(urls) - 1):
                    embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",description="The end.")
                    embed.set_footer(text="By Young#0001")
                    await message.edit(embed=embed)
                    break
                reaction, user = await bot.wait_for("reaction_add",timeout=60.0,check=check)
                if str(reaction) ==  "▶":
                    page+=1
                elif str(reaction) == "◀":
                    page-=1
                await message.remove_reaction(reaction,user)
                embed=discord.Embed(color=0x009dff,title="Nhentai Viewer",url=url)
                embed.set_footer(text="By Young#0001")
                embed.set_image(url=urls[page])
                await message.edit(embed=embed)
        else:
            await ctx.send(f"Please input number")
