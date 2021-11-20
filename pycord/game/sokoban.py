
class Sokoban():
    def __init__(self,difficulty):
        if difficulty is None :
            high=10
            width=10
            number=1
        else :
            high=difficulty*10
            width=difficulty*10
            number=difficulty
        self.map1=[[]]*high
        self.box=[]
        repeat=[]
        for i in range(high):
            if i == 0 or i == high-1 : self.map1[i] = ["🔲"]*width
            else:
                self.map1[i]=[""]*width
                for x in range(width) :
                    if x == 0 or x == width-1 :self.map1[i][x] = "🔲"
                    else : self.map1[i][x]="⬛"
        while 1 :
            if [random.randint(1,high-2),random.randint(1,width-2)] not in repeat :
                repeat.append([random.randint(2,high-3),random.randint(2,width-3)])
            if len(repeat)==2+number:
                break

        for i in range(len(repeat)):
            if i == 0 :
                self.player=repeat[0]
            elif i == 1 :
                self.end=repeat[1]
            else :
                self.box.append(repeat[i])
    def userinput(self,x):
        y={"🔼":self.up,"🔽":self.down,"◀":self.left,"▶":self.right}
        y[x]()
    def up(self):
        if self.map1[self.player[0]-1][self.player[1]] != "🔲" :
            if ([self.player[0]-1,self.player[1]] !=self.end) and ([self.player[0]-1,self.player[1]] not in self.box):#自己移動
                self.player[0]-=1
            elif ([self.player[0]-1,self.player[1]] in self.box) :#推箱子
                box=self.box[self.box.index([self.player[0]-1,self.player[1]])]
                if self.map1[box[0]-1][box[1]] !="🔲" :
                    if [box[0]-1,box[1]] ==self.end:
                        del self.box[self.box.index([self.player[0]-1,self.player[1]])]
                    else :
                        self.box[self.box.index([self.player[0]-1,self.player[1]])][0]-=1
                    self.player[0]-=1

    def down(self):
        if self.map1[self.player[0]+1][self.player[1]] != "🔲" :
            if ([self.player[0]+1,self.player[1]] !=self.end) and ([self.player[0]+1,self.player[1]] not in self.box):#自己移動
                self.player[0]+=1
            elif ([self.player[0]+1,self.player[1]] in self.box) :#推箱子
                box=self.box[self.box.index([self.player[0]+1,self.player[1]])]
                if self.map1[box[0]+1][box[1]] !="🔲" :
                    if [box[0]+1,box[1]] ==self.end:
                        del self.box[self.box.index([self.player[0]+1,self.player[1]])]
                    else :
                        self.box[self.box.index([self.player[0]+1,self.player[1]])][0]+=1
                    self.player[0]+=1
    def left(self):
        if self.map1[self.player[0]][self.player[1]-1] != "🔲" :
            if ([self.player[0],self.player[1]-1] !=self.end) and ([self.player[0],self.player[1]-1] not in self.box):#自己移動
                self.player[1]-=1
            elif ([self.player[0],self.player[1]-1] in self.box) :#推箱子
                box=self.box[self.box.index([self.player[0],self.player[1]-1])]
                if self.map1[box[0]][box[1]-1] !="🔲" :
                    if [box[0],box[1]-1] ==self.end:
                        del self.box[self.box.index([self.player[0],self.player[1]-1])]
                    else :
                        self.box[self.box.index([self.player[0],self.player[1]-1])][1]-=1
                    self.player[1]-=1
    def right(self):
        if self.map1[self.player[0]][self.player[1]+1] != "🔲" :
            if ([self.player[0],self.player[1]+1] !=self.end) and ([self.player[0],self.player[1]+1] not in self.box):#自己移動
                self.player[1]+=1
            elif ([self.player[0],self.player[1]+1] in self.box) :#推箱子
                box=self.box[self.box.index([self.player[0],self.player[1]+1])]
                if self.map1[box[0]][box[1]+1] !="🔲" :
                    if [box[0],box[1]+1] ==self.end:
                        del self.box[self.box.index([self.player[0],self.player[1]+1])]
                    else :
                        self.box[self.box.index([self.player[0],self.player[1]+1])][1]+=1
                    self.player[1]+=1
    def mapprint(self):
        map2=copy.deepcopy(self.map1)
        map2[self.player[0]][self.player[1]]="🌝"#人物
        map2[self.end[0]][self.end[1]]="🟨"#終點
        for i in self.box :
            map2[i[0]][i[1]]="🔳"#箱子
        if not len(self.box):return ("\n".join(["".join(i) for i in map2]),True)
        else :return ("\n".join(["".join(i) for i in map2]),False)


class Game(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @commands.command()
    async def sokoban(self,ctx:commands.Context,level:int=None):
        ww=Sokoban(level)
        text,_=ww.mapprint()
        embed=discord.Embed(title="sokoban",description=f"```\n{text}\n```")
        message=await ctx.send(embed=embed)
        for i in ["◀","🔼","🔽","▶","⏹"]:
            await message.add_reaction(i)
        def check(reaction, user):
            return user == ctx.author and reaction.message == message 
        while 1 :
            reaction, user = await self.bot.wait_for("reaction_add",timeout=60.0,check=check)
            await message.remove_reaction(reaction,user)
            if str(reaction)=="⏹":break
            ww.userinput(str(reaction))
            text,t=ww.mapprint()
            embed=discord.Embed(title="sokoban",description=f"```\n{text}\n```")       
            await message.edit(embed=embed)
            if t :
                await ctx.send("過關")
                break
bot.add_cog(Game(bot))

