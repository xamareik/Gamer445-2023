import discord
from discord.ext import commands
from rule34Py import rule34Py
import json
import os
import random
import time

#vaeriables

v = open('storedvariables.json')
storedvariables = json.load(v)


intents=discord.Intents.all()
client = commands.Bot(command_prefix = 'g>', intents=intents )
r34 = rule34Py()

#TODO add more on_ready messages

@client.event
async def on_ready():
    print('Eltridch god in the ao')
    await client.change_presence(activity=discord.Game('g>help'))



#TODO revamp admin system, using however you store shit server wise i forgot

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

#TODO sort random meme code

@client.command(brief='agony')
async def cheadle(ctx):
    await ctx.send('https://upload.wikimedia.org/wikipedia/commons/5/51/Don_Cheadle_UNEP_2011_%28cropped%29.jpg')

@client.command(brief='bo2 origins staff upgrade guide')
async def staffupgrade(ctx):
    await ctx.send('https://i.redd.it/xphtcyx2eg1z.jpg')

@client.command(aliases=['MWWT'],brief='ME WHEN WHEN THE')
async def mwwt(ctx):
    await ctx.send('https://media.discordapp.net/attachments/568600040537325568/758335492105699390/XsarjeOA38DzeGwzofC1jAAAAAASUVORK5CYII.png')

@client.command(brief='too old for sex')
async def old(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/819059284246528033/819331999041847347/82DE368344B6F7CA83C9971EA2E7AB8E52AB1821.png")



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

#TODO what the fuck
@client.command()
async def bait(ctx, minoritytype):
    with open('blacklist.json') as r:
        data = json.load(r)




#TODO colorlist based on score, funny things, maybe redo page/limit system to use button react things, embed34.set_thumbnail(url=thumbnail) PHOTOSHOP CRYING 445
@client.command()
async def rule34(ctx, page, limit, *, tags):
    r34quotes = storedvariables.get('r34quotes')
    
    tagssplit = tags.split()
    searchlist = r34.search(tags=tagssplit, page_id=int(page), limit=int(limit))
    post = random.choice(searchlist)
    
    embed34=discord.Embed(title=post.id, description=post.tags)
    embed34.add_field(name="",value=f"Score: {post.score}", inline=False)
    embed34.add_field(name="",value=f"Owner: {post.owner}", inline=False)
    embed34.set_image(url=post.image)
    embed34.set_footer(text=random.choice(r34quotes))
    

    await ctx.send(embed=embed34)

@client.command()
async def grabtags(ctx, id):
    post = r34.get_post(id)
    
    await ctx.send(post.tags)

@client.command()
async def niggaamunch(ctx):
    await ctx.send('https://api-cdn.rule34.xxx/images/6228/e38338b63b7373c0f88288fec12bcb2c.png')

#TODO REDO OR REMOVE PERMS
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


t = open('token.json')
data = json.load(t)
client.run(data.get('token'))