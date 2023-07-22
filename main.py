#import the shit
import discord
import time
#import nekos
from rule34Py import rule34Py
import os
import json
from discord.ext import commands
from memelist import otherfilememelist
import random
intents=discord.Intents.all()
#makes prefix g!
client = commands.Bot(command_prefix = 'g>', intents=intents )
r34 = rule34Py()
import json

#print dat shit when it online
@client.event
async def on_ready():
    print('Eltridch god in the ao')
    await client.change_presence(activity=discord.Game('g>help'))




@client.command(brief='sends a random meme')
async def maymay(ctx, amount, sleeptime): # b'\xfc'
    x = int(amount)
    sleeptime = int(sleeptime)
    memelist = otherfilememelist
    while x > 0:
        #credit:big boss troll face#9894/compressed ps1 snake#9894 
        randomnumber = random.randint(0, len(memelist)-1)
        await ctx.send(memelist[randomnumber])
        memelist.remove(memelist[randomnumber])
        time.sleep(sleeptime)
        x = x - 1

@client.command()
async def test(ctx):
    embed1 = discord.Embed(title="Congratulations!", description="You won!")
    embed1.add_field(name="", value="[View black crime statistics](https://www.ojjdp.gov/ojstatbb/crime/ucr.asp?table_in=2)", inline=False)
    embed1.set_image("https://pngimg.com/uploads/fish/fish_PNG10532.png")
    channel = await ctx.message.author.create_dm()
    await channel.send(embed=embed1)  

@client.command(brief='add the role that can use commands that require permissions')
async def adminrole(ctx, roleid, password):
    if password == 'supersexyfuntimeblacky' or password == None:
        serverid = ctx.guild.id
        todump = {roleid: serverid}
        with open('roles.json') as f:
            data = json.load(f)

        data.update(todump)

        with open('roles.json', 'w') as f:
            json.dump(data, f)
    else:
        await ctx.send("unfun mayor detected")


@client.command(brief='agony')
async def cheadle(ctx):
    await ctx.send('https://upload.wikimedia.org/wikipedia/commons/5/51/Don_Cheadle_UNEP_2011_%28cropped%29.jpg')


@client.command(brief='bo2 origins staff upgrade guide')
async def staffupgrade(ctx):
    await ctx.send('https://i.redd.it/xphtcyx2eg1z.jpg')


@client.command(brief='create embed')
async def embed(ctx, title1: str, body1: str, imgurl: str = None, thumbnail: str = None):
    await ctx.message.delete()
    
    embed1 = discord.Embed(title=title1, description=body1, colour=0xcf1204)
    if imgurl is not None:
        embed1.set_image(url=imgurl)
    if thumbnail is not None:
        embed1.set_thumbnail(url=thumbnail)
    await ctx.send(embed=embed1)

@client.command(aliases=['MWWT'],brief='ME WHEN WHEN THE')
async def mwwt(ctx):
    await ctx.send('https://media.discordapp.net/attachments/568600040537325568/758335492105699390/XsarjeOA38DzeGwzofC1jAAAAAASUVORK5CYII.png')

@client.command(brief='message spammer')
async def spammer(ctx, spam : int, *, message : str):
    while spam >= 1:
        await ctx.send(message)
        spam = spam - 1

#@client.command()
#async def gcb(ctx, amount : int):
#    BALDRY = await ctx.guild.get_member(user_id = 813532636248932373)
#    while amount >= 1:
#        await BALDRY.send("https://niggafart.com")
#        amount = amount - 1


@client.command(hidden=True)
async def webhookspammer(ctx, name, message,amount: int, messagetimes: int):
    messagetimes = messagetimes * amount
    for x in range(0, amount):
        channel1 = await ctx.guild.create_text_channel(name=name + str(x))
        webhook1 = await channel1.create_webhook(name=name + str(x))
        
        while messagetimes >= 1:
            await webhook1.send(message)
            messagetimes =- 1

@client.command()
async def bait(ctx, minoritytype):
    with open('blacklist.json') as r:
        data = json.load(r)
    
@client.command()
async def rule34(ctx, page, limit, *, tags):
    tagssplit = tags.split()
    searchlist = r34.search(tags=tagssplit, page_id=int(page), limit=int(limit))
    post = random.choice(searchlist)
    await ctx.send(post.image)

@client.command()
async def niggaamunch(ctx):
    await ctx.send('https://api-cdn.rule34.xxx/images/6228/e38338b63b7373c0f88288fec12bcb2c.png')

@client.command()
async def baitban(ctx):
    with open('blacklist.json') as r:
        data = json.load(r)
    

@client.command(brief='too old for sex')
async def old(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/819059284246528033/819331999041847347/82DE368344B6F7CA83C9971EA2E7AB8E52AB1821.png")

@client.command(brief='nukes an amount of messages, if you have perms')
async def nuke(ctx, msgAmount):
    serverid = ctx.guild.id
    rolelist=[]
    with open('roles.json') as r:
        data = json.load(r)
    
    keys=list(data.keys())
    vals=list(data.values())

    for x in range(0, len(ctx.author.roles)):
        rolelist.append(ctx.author.roles[x].id)
    if int(keys[vals.index(serverid)]) in rolelist:
        await ctx.message.channel.purge(limit = int(msgAmount) + 1)
    else:
        await ctx.send("You have NO SEX")

@client.command(brief='recreates a channel, if you have perms')
async def channelnuke(ctx):
    rolelist=[]
    serverid = ctx.guild.id
    with open('roles.json') as r:
        data = json.load(r)
    
    keys=list(data.keys())
    vals=list(data.values())
    for x in range(0, len(ctx.author.roles)):
        rolelist.append(ctx.author.roles[x].id)
    if int(keys[vals.index(serverid)]) in rolelist:
        channel2 = await ctx.channel.clone()
        await ctx.channel.delete()
        await channel2.send("Channel deleted, start sending sex")
    else:
        await ctx.send("You have NO SEX")

#@client.command(aliases=['horny', 'sex'],brief='sends le epic sex')
#async def porn(ctx, ptype = None):
#    if ctx.channel.is_nsfw() == True:
#        if ptype == None:
#            embed1 = discord.Embed(title="Porn Types", description="wallpaper ngif tickle lewd feed gecg gasm slap avatar lizard waifu pat 8ball kiss neko spank cuddle fox_girl hug smug goosewoof", colour=0xcf1204)
#            await ctx.send(embed=embed1)
#        else:
#            porn = nekos.img(ptype)
#            embed2 = discord.Embed(title="HOT SEX EPIC", colour=0xcf1204)
#            embed2.set_image(url=porn)
#            await ctx.send(embed=embed2)
#    else:
#        await ctx.send("Not an NSFW channel!")

@client.command(brief='bot ping')
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)} ms')

#client.run(os.environ['DISCORD_TOKEN'])
t = open('token.json')
data = json.load(t)
client.run(data.get('token'))