import discord
from discord.ext import commands
import asyncio
import os
import sys
import time
import random
import datetime as dt
import datetime
import json, asyncio
import copy
import logging
import traceback
import aiohttp
from collections                import Counter


command_prefix = "s" #CHANGE IT TO WHAT YOU WANT
description = "PrestiG's own BOT" #ALSO CHANGE THIS
bot = commands.Bot(command_prefix, description = description)
bot.remove_command('help')
tu = datetime.datetime.now()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#  @bot.event
#async def on_command_error(ctx, error):
#    if isinstance(error, commands.CommandNotFound):
#        pass

#https://discordapp.com/oauth2/authorize/?permissions=2138569983&scope=bot&client_id=390481566666588161

@bot.event
async def on_guild_join(server):
    print("New Server Joined: {.name}!\n\n".format(server))
    owner=bot.get_user(219881141551759360)
    servername= server.name
    serverreg= server.region
    serverinv= str(server)
    serverid= server.id
    serverowner= server.owner
    ownerid= server.owner_id
    icon1 = server.icon_url
    joinedguild = discord.Embed(colour = discord.Colour(0xA522B3))
    joinedguild.set_author(name = '[SERVER JOINED]')
    joinedguild.description = f"I just joined a **new server**! <:happy:392104480239255554>"
    joinedguild.set_thumbnail(url= icon1)
    joinedguild.add_field(name="Server Name", value= f"**{servername}**", inline=False)
    joinedguild.add_field(name="Server IDㅤㅤㅤㅤㅤㅤㅤ", value= f"**{serverid}**", inline=True)
    joinedguild.add_field(name="Server Regionㅤㅤㅤㅤ", value= f"**{serverreg}**", inline=True)
    joinedguild.add_field(name="Server Owner", value= f"**{serverowner}**", inline=True)
    joinedguild.add_field(name="Owner ID", value= f"**{ownerid}**", inline=True)
    joinedguild.set_footer(text = time.strftime("%d/%m/%Y - %I:%M:%S %p"))
    await owner.send(embed = joinedguild)

#async def msgdev(ctx, user: discord.Member, *, message: str):
#    embed = discord.Embed(color = 0xffffff, title = "Message from {}".format(user.name), description = "Message: {}".format(message))
#    embed.add_field(name = "Server", value = ctx.message.server.name)
#    embed.add_field(name = "Server ID", value = ctx.message.server.id)
#    embed.add_field(name = "Server User Count", value = ctx.message.server.member_count)
#    embed.add_field(name = "Server Owner", value = ctx.message.server.owner)
#    embed.add_field(name = "User Name", value = user.name)
#    embed.add_field(name = "User ID", value = user.id)
#    embed.add_field(name = "User Discr.", value = user.discriminator)
#    embed.set_thumbnail(url = ctx.message.server.icon_url)
#    await bot.send_message(bot.get_user('371001497342836737', embed = embed))
#    await bot.say("**☑  |  Message sent to Rapid**")

@bot.command(aliases = ['support', 'serv'])
async def server(ctx):

    invite2 = bot.get_user(390478999828037632)
    invite1 = discord.Embed(colour = discord.Colour(0xA522B3))

    if invite2.avatar_url[54:].startswith('a_'):
        avi2 = 'https://cdn.discordapp.com/avatars/' + invite2.avatar_url[35:-10]
    else:
        avi2 = invite2.avatar_url

    invite1.set_thumbnail(url = avi2)

    invite1.description = f"<:yamaiyuzuru1:391525066304782336> Need some help with **Spirit | 精霊** <:bot:389862148395761664>? Here is a link you can use to Support Server! <:yamaikaguya1:391525065608658945>\n\nhttps://discord.gg/efF93Gz"

    await ctx.send(embed = invite1)

@bot.command(aliases = ['cmds', 'commands'], description = 'Sends a message with commands in DM')
async def help(ctx):

    developer = bot.get_user(219881141551759360) # commands.get_user(commands.owner_id)

    if developer.avatar_url[54:].startswith('a_'):
        avi = 'https://cdn.discordapp.com/avatars/' + developer.avatar_url[35:-10]
    else:
        avi = developer.avatar_url

    embed = discord.Embed(colour = discord.Colour(0xA522B3))
    embed.set_thumbnail(url = avi)
    embed.set_author(name = developer, url = "https://discord.gg/efF93Gz", icon_url = avi)
    embed.description = f"Hi everyone!~♡ I'm **{developer.name}**, the creator of **Spirit | 精霊** <:bot:389862148395761664> \nI'm started making the bot in <:pythonbot:392172368023388160> and I'm also a web designer & designer. \nI wanted to make a BOT to know about how we do them \nbut also because my dream is to become **Discord Partner**."
    embed.add_field(name="Having Issues/Problems?", value="If you have any problems with **Spirit | 精霊** <:bot:389862148395761664>,\nthen you can join us in our **[support server](https://discord.gg/efF93Gz)**, or visit our **[website](https://prestig-web.wixsite.com/spirit-bot)**!", inline=False)

    help1 = discord.Embed(colour = discord.Colour(0xA522B3))
    help1.title = f"Spirit | 精霊  Commands List~♡"
    help1.description = f"**Spirit | 精霊** <:bot:389862148395761664>'s prefix is **s**.\nNeed more informations about a command? `shelp [command]`\n\n"
    help1.add_field(name="Core Commands", value="`shelpme` **|** `sshutdown` **|** `scommands` **|** `scmds` **|** `skill` **|** `ssd` **|** `ssetgame`", inline=False)
    help1.add_field(name="Utility Commands", value="`sping` **|** `sms` **|** `sctime` **|** `sprofile` **|** `sabout` **|** `sinfo` **|** `sstats`", inline=False)
    help1.add_field(name="Fun Commands", value="`ssnowball` **|** `ssb`", inline=False)
    help1.add_field(name="Kawaii Commands", value="`shug` **|** `sblush` **|** `sscared` **|** `sdance` **|** `skiss` **|** `slewd` **|** `slick` **|** `spet` **|** `ssmug` **|** `scry` **|** `shappy` **|** `sfun` **|** `ssing` **|** `sattack` **|** `seat` **|** `skms` **|** `swink` **|** `snom`", inline=False)
    help1.add_field(name="Extra Commands", value="`ssupport` **|** `sdiscord` **|** `sweb` **|** `swebsite` **|** `sinvite` **|** `sinv`", inline=False)
    help1.set_footer(text = "Have fun using Spirit | 精霊~♡")
    #help1.description = f"**Spirit | 精霊** <:bot:389862148395761664>'s prefix is **s**. If the Server Owner changed it, \nYou can use `@Spirit | 精霊 prefix` to get the prefixes list! \nNeed more informations about a command? `shelp [command]`\n\n"

    await ctx.send(embed = embed)
    await ctx.send(embed = help1)

@bot.command(aliases=["xmas"])
async def christmas(ctx):
    now=datetime.datetime.utcnow()
    xmas=datetime.datetime(now.year, 12, 25)
    if xmas<now:
        xmas=xmas.replace(year=now.year+1)
    delta=xmas-now
    weeks, remainder=divmod(int(delta.total_seconds()), 604800)
    days, remainder2=divmod(remainder, 86400)
    hours, remainder3=divmod(remainder2, 3600)
    minutes, seconds=divmod(remainder3, 60)
    embed=discord.Embed(colour = discord.Colour(0xA522B3))
    embed.add_field(name=":gift::christmas_tree::santa:Time left until Christmas:santa::christmas_tree::gift:",
        value=f"{weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")
    await ctx.send(embed=embed)

@bot.command(aliases=["devbday"])
async def ownerbday(ctx):
    now=datetime.datetime.utcnow()
    bday1 = now.year + 1
    bday=datetime.datetime(bday1, 11, 15)
    if bday<now:
        bday=bday.replace(year=now.year+1)
    delta=bday-now
    y, remainder4=divmod(int(delta.total_seconds()), 31536025)
    months, remainder5=divmod(remainder4, 2592000)
    weeks, remainder=divmod(remainder5, 604800)
    days, remainder2=divmod(remainder, 86400)
    hours, remainder3=divmod(remainder2, 3600)
    minutes, seconds=divmod(remainder3, 60)

    embed=discord.Embed(colour = discord.Colour(0xA522B3))
    embed.add_field(name=":gift:<:Maintenance:391999920229318668>:gift:Time left until Bot Owner's Birthday:gift:<:Maintenance:391999920229318668>:gift:",
        value=f"{y} year, {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes.")
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def roles(ctx):
    roles = ctx.message.guild.roles
    result = "All of the servers roles are "
    for role in roles:
        embed = discord.Embed(timestamp = datetime.datetime.utcnow(), color = ctx.message.author.color, description = "" + role.name + "  =  " + role.id + "\n")
        embed.set_author(name = "All the server roles")
    await bot.say(embed = embed)

@bot.command(hidden=True, aliases=['kill', 'sd'])
async def shutdown(ctx):
    '''Fallback if mod cog couldn't load'''
    if await ctx.bot.is_owner(ctx.author):

            developer = bot.get_user(219881141551759360) # commands.get_user(commands.owner_id)
            shutdown1 = discord.Embed(colour = discord.Colour(0xA522B3))
            shutdown1.set_author(name='[SHUTDOWN]', url = "https://prestig-web.wixsite.com/spirit-bot")
            shutdown1.description = f"**Spirit | 精霊** has been **Shutdown For Maintenance** by ***{developer.name}*** ! <:Maintenance:391999920229318668>"
            shutdown1.set_footer(text = time.strftime("%d/%m/%Y - %I:%M:%S %p"))

            await ctx.send(embed = shutdown1)
            bot.logout()
            sys.exit(0)
    else:
            developer = bot.get_user(219881141551759360) # commands.get_user(commands.owner_id)
            shutdown2 = discord.Embed(colour = discord.Colour(0xA522B3))
            list17 = [
            ":speech_left:⠀**|⠀*Kurumi Tokisaki***\n```You were ready to kill another creature, yet you are scared to be killed. Dont you think that is weird? When you point a gun at another life... This is what happens.```",
            ":speech_left:⠀**|⠀*Tohka Yatogami***\n```Just killing and killing and killing. You deserve to die and to die and to die.```",
            ]
            choice17 = random.choice(list17)
            shutdown2.description = choice17
            shutdown2.set_footer(text = "You dont have permissions to use this command")

            await ctx.send(embed = shutdown2)

@bot.command(aliases = ['creator', 'dev', 'developer'], description = 'Who is my creator?')
async def owner(ctx):

    developer = bot.get_user(219881141551759360) # commands.get_user(commands.owner_id)

    if developer.avatar_url[54:].startswith('a_'):
        avi = 'https://cdn.discordapp.com/avatars/' + developer.avatar_url[35:-10]
    else:
        avi = developer.avatar_url

    embed = discord.Embed(colour = discord.Colour(0xA522B3))

    embed.set_thumbnail(url = avi)
    embed.set_author(name = developer, url = "https://discord.gg/efF93Gz", icon_url = avi)

    embed.description = f"Hi everyone!~♡ I'm **{developer.name}**, the creator of **Spirit | 精霊** <:bot:389862148395761664> \nI'm started making the bot in <:pythonbot:392172368023388160> and I'm also a web designer & designer. \nI wanted to make a BOT to know about how we do them \nbut also because my dream is to become **Discord Partner**."
#        embed.add_field(value = "Hi everyone!~♡ I'm Mitohku, the creator of Kurumi BOT")
#        embed.add_field(value = "I'm starting in Python development but I'm also a web designer.")
#        embed.add_field(value = "I wanted to make a BOT to know about how we do them")
#        embed.add_field(value = "but also because I would like my community to get bigger.")

    await ctx.send(embed = embed)

@bot.command()
async def ctime(ctx):

        thetime = time.strftime("%I:%M:%S %p")
        list2 = [
            ":clock1:",
            ":clock10:",
            ":clock1030:",
            ":clock11:",
            ":clock1130:",
            ":clock12:",
            ":clock1230:",
            ":clock130:"
            ]
        choice2 = random.choice(list2)
        clocktime = choice2
        time1 = discord.Embed(colour = discord.Colour(0xA522B3))
        time1.description = f"{clocktime} **| {ctx.author.name}**, it is currently **{thetime}**"
        list1 = [
            "https://i.imgur.com/oX1eFiZ.jpg",
            "https://i.imgur.com/q9T8SaQ.jpg",
            "https://i.imgur.com/LWEKNjn.gif",
            "https://i.imgur.com/iBjWUYE.jpg",
            "https://i.imgur.com/4j4Wju0.gif",
            "https://i.imgur.com/4D4wKBx.gif",
            "https://i.imgur.com/JXCwRZR.gif",
            "https://i.imgur.com/zSEyljV.gif",
            "https://i.imgur.com/6NiwZNZ.gif",
            "https://i.imgur.com/6yREP9J.gif",
            "https://i.imgur.com/g744fbZ.jpg"
            ]
        choice = random.choice(list1)
        time1.set_image(url = choice)
        await ctx.send(embed = time1)

@bot.command(aliases = ['ms'])
async def ping(ctx):
        pingms = "{}".format(int(bot.latency * 1000)) #MS
        pings = "{}".format(int(bot.latency * 1)) #S

        ping1 = discord.Embed(colour = discord.Colour(0xA522B3))
        ping1.description = f"My latency is actually **{pings}s** | **{pingms}ms**."
        ping1.set_footer(text = time.strftime("%d/%m/%Y - %I:%M:%S %p"))
        await ctx.send(embed = ping1)


@bot.command(aliases = ['inv'])
async def invite(ctx):

    invite2 = bot.get_user(390478999828037632)
    invite1 = discord.Embed(colour = discord.Colour(0xA522B3))

    if invite2.avatar_url[54:].startswith('a_'):
        avi2 = 'https://cdn.discordapp.com/avatars/' + invite2.avatar_url[35:-10]
    else:
        avi2 = invite2.avatar_url

    invite1.set_thumbnail(url = avi2)

    invite1.description = f"<:yamaiyuzuru1:391525066304782336> Want to invite **Spirit | 精霊** <:bot:389862148395761664> to your Server? <:yamaikaguya1:391525065608658945>\n\nhttps://discordapp.com/oauth2/authorize/?permissions=2138569983&scope=bot&client_id=390478999828037632"

    await ctx.send(embed = invite1)

@bot.group()
async def game(self):

	if game == None:
		await self.send(f"Please use one of the following settings: `default`, `playing`, `streaming`, `watching`, `listenning` or `clear`")

@game.command(name = 'playing')
async def game_playing(self, *, game = None):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		await self.bot.change_presence(game=discord.Game(name = game))
		await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Playing **{game}**'")

@game.command(name = 'streaming')
async def game_streaming(self, *, game = None):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		await self.bot.change_presence(game=discord.Game(name = game, url = "https://www.twitch.tv/spiritprod", type = 1))
		await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Streaming **{game}**'")

@game.command(name = 'listenning')
async def game_listning(self, *, game = None):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		await self.bot.change_presence(game=discord.Game(name = game, type = 2))
		await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Listenning to **{game}**'")

@game.command(name = 'watching')
async def game_watching(self, *, game = None):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		await self.bot.change_presence(game=discord.Game(name = game, type = 3))
		await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Watching **{game}**'")

@game.command(name = 'default')
async def game_default(self):

	bot_prefix = "s"
	server = self.guild

	await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Default'")

	games = [f"Use {bot_prefix}help for help!", f"{sum(1 for _ in self.bot.get_all_members())} users | {len(self.bot.guilds)} servers", f"Wanna invite {self.bot.user.name}? Use: {bot_prefix}inv", f"Give us feedback? Use: {bot_prefix}feedback [message]"]
	current_number = 0
	while True:
		if current_number == len(games):
			current_number = 0
		await self.bot.change_presence(game=discord.Game(name = games[current_number], url = "https://www.twitch.tv/spiritprod", type = 1))
		await asyncio.sleep(20)
		current_number += 1

@game.command(name = 'clear')
async def game_clear(self, *, game = None):

	await self.bot.change_presence(game=discord.Game(name = None))
	await self.send(f"Cleared the status of **{self.bot.user.name}**")

#@bot.command()
#async def test(ctx, *, member : discord.Member=None):
#    if member is None:
#        await ctx.send("{} has been tested! 💘".format(ctx.message.author.mention))
#    elif member.id == ctx.message.author.id:
#        await ctx.send("{} tested themselves because they are a loner 🤦".format(ctx.message.author.mention))
#    else:
#        await ctx.send("{} was tested by {} 💝".format(member.mention, ctx.message.author.mention))

@bot.command()
async def hug(ctx, *, member : discord.Member=None):
    if not member:
        await ctx.send(f"Please **mention** the person you want to ***hug*** !")
    elif member == ctx.author:
        author = ctx.message.author.mention
        hug1 = discord.Embed(colour = discord.Colour(0xA522B3))
        hug1.description = f"{author} hugged themselves.... Sad..."
        list3 = [
            "https://media.giphy.com/media/sisfaf8ZIdSAU/giphy.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460592-miku-cuddling-yoshino.gif",
            ]
        choice3 = random.choice(list3)
        hug1.set_image(url = choice3)
        await ctx.send(embed = hug1)

    else:
        author = ctx.message.author.mention
        mention = member.mention
        hug2 = discord.Embed(colour = discord.Colour(0xA522B3))
        hug2.description = f"{author} has hugged {mention}. Awwwww~~ 💝"
        list3 = [
            "https://media.giphy.com/media/sisfaf8ZIdSAU/giphy.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460592-miku-cuddling-yoshino.gif",
            ]
        choice3 = random.choice(list3)
        hug2.set_image(url = choice3)
        await ctx.send(embed = hug2)

@bot.command()
async def kiss(ctx, *, member : discord.Member=None):
    if not member:
        await ctx.send(f"Please **mention** the person you want to ***kiss*** !")
    else:
        author = ctx.message.author.mention
        mention = member.mention
        kiss2 = discord.Embed(colour = discord.Colour(0xA522B3))
        kiss2.description = f"{author} is kissing {mention}. LOVE IS IN THE AIRRR~ 💝"
        list4 = [
            "https://media.giphy.com/media/11xP7QUQl8d02c/giphy.gif",
            "https://media.giphy.com/media/HSgkuMRab3fK8/giphy.gif",
            ]
        choice4 = random.choice(list4)
        kiss2.set_image(url = choice4)
        await ctx.send(embed = kiss2)

@bot.command()
async def blush(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        blush1 = discord.Embed(colour = discord.Colour(0xA522B3))
        blush1.description = f"{author} is blushing! I wonder why hehe~"
        list5 = [
            "https://media.giphy.com/media/LIAoqLFnAvm6c/giphy.gif",
            "https://media.giphy.com/media/13aCm6Gp5bCsec/giphy.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460561-tumblr-n3ih37wl1v1sc9og8o1-500.gif",
            ]
        choice5 = random.choice(list5)
        blush1.set_image(url = choice5)
        await ctx.send(embed = blush1)
    else:
        author = ctx.message.author.mention
        mention = member.mention
        blush2 = discord.Embed(colour = discord.Colour(0xA522B3))
        blush2.description = f"{mention} made {author} blush! Awwwww, cute~~ 💝"
        list5 = [
            "https://media.giphy.com/media/LIAoqLFnAvm6c/giphy.gif",
            "https://media.giphy.com/media/13aCm6Gp5bCsec/giphy.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460561-tumblr-n3ih37wl1v1sc9og8o1-500.gif",
            ]
        choice5 = random.choice(list5)
        blush2.set_image(url = choice5)
        await ctx.send(embed = blush2)

@bot.command()
async def scared(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        scared1 = discord.Embed(colour = discord.Colour(0xA522B3))
        scared1.description = f"{author} is scared.... Let's help them"
        scared1.set_image(url = "https://media.giphy.com/media/NHNyT2CUTkjuw/giphy.gif")
        await ctx.send(embed = scared1)
    else:
        author = ctx.message.author.mention
        mention = member.mention
        scared2 = discord.Embed(colour = discord.Colour(0xA522B3))
        scared2.description = f"{mention} scared {author}! What a mean person!"
        scared2.set_image(url = "https://media.giphy.com/media/NHNyT2CUTkjuw/giphy.gif")
        await ctx.send(embed = scared2)

@bot.command()
async def dance(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        dance1 = discord.Embed(colour = discord.Colour(0xA522B3))
        dance1.description = f"{author} is dancing! What a professionnal!"
        list6 = [
            "https://media.giphy.com/media/ipfO8nyNQSVnq/giphy.gif",
            "https://media.giphy.com/media/100AQ5GepqTP3O/giphy.gif",
            "https://media.giphy.com/media/yEx3Lwfqx6Ap2/giphy.gif",
            "https://media.giphy.com/media/vWVfsA3VOhYMU/giphy.gif",
            ]
        choice6 = random.choice(list6)
        dance1.set_image(url = choice6)
        await ctx.send(embed = dance1)

@bot.command()
async def lick(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        lick1 = discord.Embed(colour = discord.Colour(0xA522B3))
        lick1.description = f"{author} licked themselves, Uhhhh.."
        list7 = [
            "http://upload.inven.co.kr/upload/2013/05/23/bbs/i3871970273.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460656-kurumi-licks-shido-s-wound.gif",
            ]
        choice7 = random.choice(list7)
        lick1.set_image(url = choice7)
        await ctx.send(embed = lick1)
    else:
        author = ctx.message.author.mention
        mention = member.mention
        lick2 = discord.Embed(colour = discord.Colour(0xA522B3))
        lick2.description = f"{author} is licking {mention}. W-Whut?"
        list7 = [
            "http://upload.inven.co.kr/upload/2013/05/23/bbs/i3871970273.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460656-kurumi-licks-shido-s-wound.gif",
            ]
        choice7 = random.choice(list7)
        lick2.set_image(url = choice7)
        await ctx.send(embed = lick2)

@bot.command()
async def pet(ctx, *, member : discord.Member=None):
    if not member:
        await ctx.send(f"Please **mention** the person you want to ***pet*** !")

    else:
        author = ctx.message.author.mention
        mention = member.mention
        pat2 = discord.Embed(colour = discord.Colour(0xA522B3))
        pat2.description = f"{author} pets {mention}. Looks cute."
        list8 = [
            "https://media.giphy.com/media/q35hchQDS8ro4/giphy.gif",
            "https://cdn.discordapp.com/attachments/391697918106796032/391700185836945418/Shido_patting_kurumi.gif",
            ]
        choice8 = random.choice(list8)
        pat2.set_image(url = choice8)
        await ctx.send(embed = pat2)

@bot.command()
async def smug(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        smug1 = discord.Embed(colour = discord.Colour(0xA522B3))
        smug1.description = f"{author} smugs. Uhm.. Okay?"
        smug1.set_image(url = "https://media.giphy.com/media/V6RBCgBmaGLXG/giphy.gif")
        await ctx.send(embed = smug1)

@bot.command()
async def cry(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        cry1 = discord.Embed(colour = discord.Colour(0xA522B3))
        cry1.description = f"{author} is crying... ;~;"
        list8 = [
            "https://media.giphy.com/media/lHFzaDCFmbWWA/giphy.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460675-yoshino-crying-and-effect.gif",
            ]
        choice8 = random.choice(list8)
        cry1.set_image(url = choice8)
        await ctx.send(embed = cry1)
    else:
        author = ctx.message.author.mention
        mention = member.mention
        cry2 = discord.Embed(colour = discord.Colour(0xA522B3))
        cry2.description = f"{mention} made {author} cry! Kill that boi!"
        list8 = [
            "https://media.giphy.com/media/lHFzaDCFmbWWA/giphy.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460675-yoshino-crying-and-effect.gif",
            ]
        choice8 = random.choice(list8)
        cry2.set_image(url = choice8)
        await ctx.send(embed = cry2)

@bot.command()
async def happy(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        happy1 = discord.Embed(colour = discord.Colour(0xA522B3))
        happy1.description = f"{author} is happy! Their smile looks so nice~"
        list9 = [
            "https://media.giphy.com/media/TLJtXsSxLgisw/giphy.gif",
            "https://media.giphy.com/media/bwiimA1Qjw7Ru/giphy.gif",
            "https://i.pinimg.com/originals/d9/e6/d8/d9e6d8957a600ad7196e499097a89c86.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460575-02eb9c0a203a4f25972f42dbc3ac95093bc599c1-hq.gif",
            "https://cdn.discordapp.com/attachments/391697918106796032/391698034255331351/1450669692-d2d7880efb2193a206c9f1ceb9d4cec2.gif",
            ]
        choice9 = random.choice(list9)
        happy1.set_image(url = choice9)
        await ctx.send(embed = happy1)
    else:
        author = ctx.message.author.mention
        mention = member.mention
        happy2 = discord.Embed(colour = discord.Colour(0xA522B3))
        happy2.description = f"{mention} made {author} happy! How did they do?!"
        list9 = [
            "https://media.giphy.com/media/TLJtXsSxLgisw/giphy.gif",
            "https://media.giphy.com/media/bwiimA1Qjw7Ru/giphy.gif",
            "https://i.pinimg.com/originals/d9/e6/d8/d9e6d8957a600ad7196e499097a89c86.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460575-02eb9c0a203a4f25972f42dbc3ac95093bc599c1-hq.gif",
            "https://cdn.discordapp.com/attachments/391697918106796032/391698034255331351/1450669692-d2d7880efb2193a206c9f1ceb9d4cec2.gif",
            ]
        choice9 = random.choice(list9)
        happy2.set_image(url = choice9)
        await ctx.send(embed = happy2)

@bot.command()
async def fun(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        fun1 = discord.Embed(colour = discord.Colour(0xA522B3))
        fun1.description = f"{author} is having fun! YAAAS!"
        list10 = [
            "https://media.giphy.com/media/R6TwgUiaKINLq/giphy.gif",
            "https://media.giphy.com/media/G4FXmolmlyCzK/giphy.gif",
            ]
        choice10 = random.choice(list10)
        fun1.set_image(url = choice10)
        await ctx.send(embed = fun1)

@bot.command()
async def sing(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        sing1 = discord.Embed(colour = discord.Colour(0xA522B3))
        sing1.description = f"{author} is singing! I'm crying of joy.. It's beautiful.."
        list11 = [
            "https://media.giphy.com/media/ipfO8nyNQSVnq/giphy.gif",
            "https://78.media.tumblr.com/ee4a0b429ef702595028100f8eb35202/tumblr_nrj1vvijQW1sz04cbo1_500.gif",
            "https://78.media.tumblr.com/e7fb4fb0110e125d5e30102d8754196e/tumblr_nf004blkOX1r3z16po1_500.gif",
            ]
        choice11 = random.choice(list11)
        sing1.set_image(url = choice11)
        await ctx.send(embed = sing1)

@bot.command()
async def attack(ctx, *, member : discord.Member=None):
    if not member:
        await ctx.send(f"Please **mention** the person you want to ***attack*** !")
    else:
        author = ctx.message.author.mention
        mention = member.mention
        att2 = discord.Embed(colour = discord.Colour(0xA522B3))
        att2.description = f"{author} is fighting with {mention}! RUN FOR YOUR LIIIIIFE!"
        list12 = [
            "https://media.giphy.com/media/oSA0F3aL22xGw/giphy.gif",
            "https://media.giphy.com/media/OWK5xYGK0ynNm/giphy.gif",
            "https://cdn.discordapp.com/attachments/391697918106796032/391698034175508480/Tohkas_multiple_punches.gif",
            "https://media.giphy.com/media/KXqBJPZyLjeVy/giphy.gif",
            ]
        choice12 = random.choice(list12)
        att2.set_image(url = choice12)
        await ctx.send(embed = att2)

@bot.command(aliases = ['nom'])
async def eat(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        eat1 = discord.Embed(colour = discord.Colour(0xA522B3))
        eat1.description = f"{author} is eating.. Can I have some too please?"
        list13 = [
            "https://media.giphy.com/media/hhZUIO4Yvux44/giphy.gif",
            ]
        choice13 = random.choice(list13)
        eat1.set_image(url = choice13)
        await ctx.send(embed = eat1)

@bot.command()
async def kms(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        kms1 = discord.Embed(colour = discord.Colour(0xA522B3))
        kms1.description = f"{author} is killing themselves! STOP THEM BEFORE IT'S TOO LATE!!!"
        list14 = [
            "https://media.giphy.com/media/nzU8Fc5eSybx6/giphy.gif",
            "https://media.giphy.com/media/57aSQAl3FNjwc/giphy.gif",
            ]
        choice14 = random.choice(list14)
        kms1.set_image(url = choice14)
        await ctx.send(embed = kms1)

@bot.command()
async def wink(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        wink1 = discord.Embed(colour = discord.Colour(0xA522B3))
        wink1.description = f"{author} is winking. I wonder to who~"
        list15 = [
            "https://media.giphy.com/media/viYADNUVlGSUU/giphy.gif",
            "https://78.media.tumblr.com/ee4a0b429ef702595028100f8eb35202/tumblr_nrj1vvijQW1sz04cbo1_500.gif",
            ]
        choice15 = random.choice(list15)
        wink1.set_image(url = choice15)
        await ctx.send(embed = wink1)

    else:
        author = ctx.message.author.mention
        mention = member.mention
        wink2 = discord.Embed(colour = discord.Colour(0xA522B3))
        wink2.description = f"{author} winked to {mention}! I wanna know their secret!"
        list15 = [
            "https://media.giphy.com/media/viYADNUVlGSUU/giphy.gif",
            "https://78.media.tumblr.com/ee4a0b429ef702595028100f8eb35202/tumblr_nrj1vvijQW1sz04cbo1_500.gif",
            ]
        choice15 = random.choice(list15)
        wink2.set_image(url = choice15)
        await ctx.send(embed = wink2)

@bot.command()
async def lewd(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        lewd1 = discord.Embed(colour = discord.Colour(0xA522B3))
        lewd1.description = f"{author} is being lewd! Hide your eyes!"
        list16 = [
            "https://media.giphy.com/media/k3T8QjpJ4Z2TK/giphy.gif",
            "https://media.giphy.com/media/X3blcgNZBPD8s/giphy.gif",
            "http://pa1.narvii.com/5819/7acae4a641987e2c3c002a91d8bb738f4f2aaa2b_hq.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460587-tohka-asking-shido-a-favor.gif",
            ]
        choice16 = random.choice(list16)
        lewd1.set_image(url = choice16)
        await ctx.send(embed = lewd1)

@bot.command(aliases = ['stats'])
async def about(self):
    stat1 = discord.Embed(colour = discord.Colour(0xA522B3))
    servers = len(bot.guilds)
    members=0
    for guild in bot.guilds:
        members+=len(guild.members)
    total_online = len({m.id for m in self.bot.get_all_members() if m.status is not discord.Status.offline})
    total_unique = len(self.bot.users)
    total_bots = len([m.id for m in self.bot.get_all_members() if m.bot])
    categories=0
    for guild in bot.guilds:
        categories+=len(guild.categories)
    channels=0
    for guild in bot.guilds:
        channels+=len(guild.channels)
    texts=0
    for guild in bot.guilds:
        texts+=len(guild.text_channels)
    voices=0
    for guild in bot.guilds:
        voices+=len(guild.voice_channels)

    stat2 = bot.get_user(390478999828037632)
    if stat2.avatar_url[54:].startswith('a_'):
        avi3 = 'https://cdn.discordapp.com/avatars/' + stat2.avatar_url[35:-10]
    else:
        avi3 = stat2.avatar_url

    stat1.set_thumbnail(url = avi3)
    stat1.set_author(name= stat2, icon_url= avi3)
    stat1.description= f"**[Official Spirit | 精霊 <:bot:389862148395761664> Support Server](https://discord.gg/efF93Gz)**"
    stat1.add_field(name= "Members in all Serversㅤ", value=f"Total Servers: **{servers}** \nTotal Users: **{members}** \nTotal Uniques: **{total_unique}** \nTotal Online: **{total_online}** \nTotal BOTS: **{total_bots}**", inline=True)
    stat1.add_field(name= "Channels in all Servers", value=f"Total Categories: **{categories}** \nTotal Channels: **{channels}** \nText Channels: **{texts}** \nVoice Channels: **{voices}**", inline=True)
    stat1.add_field(name= "Program Informations", value=f"Program Language: **<:pythonbot:392172368023388160> 3.6.3** \nDiscord Program: **Discord.py** \nProgram Version: **1.0.0a**", inline=True)
    stat1.add_field(name= "ㅤRun/Bot Informations", value=f"ㅤRunning on: **Heroku** <:heroku:404015867559542804> \nㅤEdited with: **Sublime Text** <:sublime:404015867416936458>\n\nㅤ*More with `shelp` command*", inline=True)
    stat1.set_footer(text=f"Spirit | 精霊 is active in {servers} servers, containing {members} members.", icon_url=avi3)
    stat1.description= f"\n"
    await self.send(embed = stat1)


@bot.command(aliases = ['sb'])
async def snowball(ctx, *, member : discord.Member = None):

    number = random.randint(1, 5)

    if not member:
        await ctx.send(f"**{ctx.author.name}**, maybe an option to throw it at someone!")
    elif member is ctx.author:
        await ctx.send(f"**{ctx.author.name}**, maybe an option to throw it at someone else!")
    else:
        if number == 1:
            snowball_hit = [
                f":snowflake: **| {ctx.author.name}**, throws a snowball in **{member.name}**'s face! *ouchh*",
                f":snowflake: **| {ctx.author.name}**, throws a snowball in **{member.name}**'s face! *ouchh*",
                f":snowflake: **| {ctx.author.name}**, throws a snowball in **{member.name}**'s face! *ouchh*",
                f":snowflake: **| {ctx.author.name}**, throws a __iceball__ in **{member.name}**'s face! *ouchh... these ones hurt...*",
                ]

            choice_hit = random.choice(snowball_hit)
            hit = discord.Embed(colour = discord.Colour(0xA522B3))
            hit.description = f"{choice_hit}"
            kawaii = bot.get_user(139191103625625600)
            hit.set_footer(text=f"| ©  {kawaii.name} |", icon_url= kawaii.avatar_url)
            await ctx.send(embed = hit)
        else:
            snowball_miss = [
                f":snowflake: **| {member.name}** dodged the snowball thrown by **{ctx.author.name}**!",
                f":snowflake: **| {ctx.author.name}**, tried to throw a snowball at **{member.name}** and missed!",
                f":snowflake: **| {ctx.author.name}**, missed and threw the snowball through a window! *Oops*",
                f":snowflake: **| {member.name}** laughed at **{ctx.author.name}**, how can you miss me?",
                f":snowflake: **| {ctx.author.name}** tries to use all their energy, and fell on the ground! *definitely a miss*",
                f":snowflake: **| {ctx.author.name}**, tried to throw a __iceball__ at **{member.name}** and missed! Lucky you, **{member.name}**!",
                ]

            choice_miss = random.choice(snowball_miss)
            miss = discord.Embed(colour = discord.Colour(0xA522B3))
            miss.description = f"{choice_miss}"
            kawaii = bot.get_user(139191103625625600)
            miss.set_footer(text=f"| ©  {kawaii.name} |", icon_url= kawaii.avatar_url)
            await ctx.send(embed = miss)

@bot.command(aliases =  ['info', 'uinfo', 'user', 'profile'])
async def userinfo(ctx, *, member: discord.Member = None):

    if member is None:
        member = ctx.author

    if member.game is None or member.game.url is None:
        if str(member.status) == "online":
            status_colour = 0x43B581
            status_name = "<:On:391999921055727618> Online"
        elif str(member.status) == "idle":
            status_colour = 0xFAA61A
            status_name = "<:Idle:391999920422387714> Away / Idle"
        elif str(member.status) == "dnd":
            status_colour = 0xF04747
            status_name = "<:DoNotDisturb:391999920292233216> Do Not Disturb"
        elif str(member.status) == "offline":
            status_colour = 0x000000
            status_name = "<:Off:391999920812589057> Offline"
        elif str(member.status) == "invisible":
            status_colour = 0x000000
            status_name = "<:Invisible:392119161343705088> Invisible"
        else:
            status_colour = member.colour
            status_name = "N/A"
    else:
        status_colour = 0x593695
        status_name = "<:Stream:391999918996193281> Streaming"

    if member.game is None:
        activity = f"**Doing**: Completely nothing!"
    elif member.game.url is None:
        activity = f"**Playing**: {member.game}"
    else:
        activity = f"**Streaming**: [{member.game}]({member.game.url})"

    e = discord.Embed(description = f"**Nickname**: {member.nick}\n{activity}", colour = status_colour)
    roles = [role.name.replace('@', '@\u200b') for role in member.roles]
    shared = sum(1 for m in ctx.bot.get_all_members() if m.id == member.id)

    highrole = member.top_role.name
    if highrole == "@everyone":
        role = "N/A"

    if member.avatar_url[54:].startswith('a_'):
        avi = 'https://cdn.discordapp.com/avatars/' + member.avatar_url[35:-10]
    else:
        avi = member.avatar_url

    if avi:
        e.set_thumbnail(url = avi)
        e.set_author(name = str(member), icon_url = avi)
    else:
        e.set_thumbnail(url = member.default_avatar_url)
        e.set_author(name = str(member), icon_url = member.default_avatar_url)

    bowner = [219881141551759360]
    developer = [282088833082720256, 371001497342836737]
    helper = [139191103625625600]
    partnered = [166723819074093056]
    youtube = [219881141551759360, 365811841810825216]
    twitch = []
    event = [164902308042375169, 318044181056716800, 304422446621130765]
    frite = [219881141551759360, 340115321207783424, 290897913431719936]

    if not member.voice:
        mute1 = ":question:"
    else:
        if ctx.author.voice.self_mute == False:
            if ctx.author.voice.mute == True:
                mute1 = "<:mute1:392144721260052490><:mute2:392144721545265172><:mute3:392144721599791105>"
            else:
                mute1 = ":sound:"
        elif ctx.author.voice.self_mute == True:
            if ctx.author.voice.mute == True:
                mute1 = "<:mute1:392144721260052490><:mute2:392144721545265172><:mute3:392144721599791105>"
            else:
                mute1 = ":mute:"

    if not member.voice:
        deaf1 = ":question:"
    else:
        if ctx.author.voice.self_deaf == False:
            if ctx.author.voice.deaf == True:
                deaf1 = "<:mute1:392144721260052490><:mute2:392144721545265172><:mute3:392144721599791105>"
            else:
                deaf1 = ":sound:"
        elif ctx.author.voice.self_deaf == True:
            if ctx.author.voice.deaf == True:
                deaf1 = "<:mute1:392144721260052490><:mute2:392144721545265172><:mute3:392144721599791105>"
            else:
                deaf1 = ":mute:"


    if not member.voice:
        voice = "Not Connected"
    else:
        voice = ctx.author.voice.channel

    if member.id in bowner:
        if member.id in youtube:
            features = "<:SpecialRole:391999921349197824> **Bot Owner/Creator**"
            features1 = "<:youtube1:391994295223189524> **Partnered Youtuber**"
            if member.id in frite:
                features = "<:SpecialRole:391999921349197824> **Bot Owner/Creator**"
                features1 = "<:youtube1:391994295223189524> **Partnered Youtuber**"
                features2 = "<:FRITEUH:403987790410547202> **Team Frite**"
        elif member.id in frite:
            features = "<:SpecialRole:391999921349197824> **Bot Owner/Creator**"
            features1 = "<:FRITEUH:403987790410547202> **Team Frite**"
        elif member.id in twitch:
            features = "<:SpecialRole:391999921349197824> **Bot Owner/Creator**"
            features1 = "<:twitch1:392000837750226945> **Partnered Streamer**"
            if member.id in frite:
                features = "<:SpecialRole:391999921349197824> **Bot Owner/Creator**"
                features1 = "<:twitch1:392000837750226945> **Partnered Streamer**"
                features2 = "<:FRITEUH:403987790410547202> **Team Frite**"
        else:
            features = "<:SpecialRole:391999921349197824> **Bot Owner/Creator**"
            features1 = "ㅤ"
    elif member.id in developer:
        if member.id in youtube:
            features = ":tools: **Bot Developer**"
            features1 = "<:youtube1:391994295223189524> **Partnered Youtuber**"
            features1 = "ㅤ"
        elif member.id in twitch:
            features = ":tools: **Bot Developer**"
            features1 = "<:twitch1:392000837750226945> **Partnered Streamer**"
            features1 = "ㅤ"
        elif member.id in partnered:
            features = ":tools: **Bot Developer**"
            features1 = "<:SpecialRole:391999921349197824> **Partnered Servers***"
        else:
            features = ":tools: **Bot Developer**"
            features1 = "ㅤ"
    elif member.id in helper:
        if member.id in youtube:
            features = "<:SpecialRole:391999921349197824> **Helper**"
            features1 = "<:youtube1:391994295223189524> **Partnered Youtuber**"
            features2 = "ㅤ"
        elif member.id in twitch:
            features = "<:SpecialRole:391999921349197824> **Helper**"
            features1 = "<:twitch1:392000837750226945> **Partnered Streamer**"
            features2 = "ㅤ"
        elif member.id in partnered:
            features = "<:SpecialRole:391999921349197824> **Helper**"
            features1 = "<:SpecialRole:391999921349197824> **Partnered Servers***"
            features2 = "ㅤ"
        else:
            features = "<:SpecialRole:391999921349197824> **Helper**"
            features1 = "ㅤ"
            features2 = "ㅤ"
    elif member.id in partnered:
        features = "<:SpecialRole:391999921349197824> **Partnered Servers**"
        features1 = "ㅤ"
        features2 = "ㅤ"
    elif member.id in youtube:
        features = "<:youtube1:391994295223189524> **Partnered Youtuber**"
        features1 = "ㅤ"
        features2 = "ㅤ"
    elif member.id in twitch:
        features = "<:twitch1:392000837750226945> **Partnered Streamer**"
        features1 = "ㅤ"
        features2 = "ㅤ"
    elif member.id in event:
        features = ":sparkles: **Special Event Winner**"
        features1 = "ㅤ"
        features2 = "ㅤ"
    elif member.id in frite:
        if member.id in bowner:
            features = "<:SpecialRole:391999921349197824> **Bot Owner/Creator**"
            features1 = "<:FRITEUH:403987790410547202> **Team Frite**"
            features2 = "ㅤ"
        else:
            features = "<:FRITEUH:403987790410547202> **Team Frite**"
            features1 = "ㅤ"
            features2 = "ㅤ"

    else:
        features = "None"
        features1 = "ㅤ"
        features2 = "ㅤ"

    e.set_footer(text = f"Member since: {member.joined_at.__format__('%d %b %Y at %H:%M:%S')}")#.timestamp = member.joined_at
    e.add_field(name = 'User ID', value = member.id)
    e.add_field(name = 'Servers', value = f'{shared} shared')
    e.add_field(name = 'Voice Status', value = f"Connected to: **{voice}**\nMicrophone: {mute1}\nSound: {deaf1}")
    e.add_field(name = 'Client Status', value = status_name)
    e.add_field(name = 'Account created at', value = member.created_at.__format__('Date: **%d %b %Y**\nTime: **%H:%M:%S**'))
    e.add_field(name = 'Highest Role', value = highrole)
    e.add_field(name = 'Spirit | 精霊 Special Roles', value = f"{features}\n{features1}\n{features2}")
    e.add_field(name = 'Roles', value = ' **|** '.join(roles) if len(roles) < 15 else f'{len(roles)} roles')

    await ctx.send(embed=e)

@bot.command(pass_context = True, aliases = ['feedback', 'fb', 'msgdev'])
async def ctdev(ctx, *, pmessage : str = None):
    invite = await ctx.channel.create_invite(max_uses = 1, xkcd = True)
    bot_owner = 219881141551759360
    dev = bot.get_user(bot_owner)

    if pmessage == None:
        embed = discord.Embed(description = ""+ ctx.author.name +" my developers need to know something right? Type a feedback!", color = 0xA522B3)
        await ctx.send(embed = embed)
        await ctx.message.delete()
    else:
            msg = "User: {}\nServer: {}\nFeedBack: {}\nServer Invite: {}".format(ctx.author, ctx.guild, pmessage, invite.url)
            embed = discord.Embed(title = "Invite to {} discord server!".format(ctx.guild), colour = 0xA522B3, url = "{}".format(invite.url), description = "Feedback: {}".format(pmessage), timestamp = datetime.datetime.utcfromtimestamp(1507439238))
            embed.set_thumbnail(url = "{}".format(ctx.author.avatar_url))
            embed.set_author(name = "{} sent:".format(ctx.author), icon_url = "{}".format(ctx.author.avatar_url))
            await dev.send(embed = embed)
#            await dev.send(msg)
            embed = discord.Embed(description = "I have PMed **{}#{}** with your feedback! Thank you for your help!".format(dev.name, dev.discriminator), color = 0xA522B3)
            await ctx.send(embed = embed)
            await ctx.message.delete()
#            return await ctx.send(ctx.author.mention + " I have PMed my creator your feedback! Thank you for the help!")

@bot.command()
async def partner(ctx, *, pmessage : str = None):

    if pmessage == None:
        embed = discord.Embed(colour = 0xA522B3)
        embed.set_author(name = "[PARTNERS LIST]", icon_url = "https://cdn.discordapp.com/emojis/391999921349197824.png")
        embed.description = "Please choose one of the following options:\nㅤ\nㅤ"
        embed.add_field(name = "ㅤspartner yt", value = "ㅤShows the full list of our Partnered Youtubers <:youtube1:391994295223189524>\nㅤ", inline=True)
        embed.add_field(name = "ㅤspartner twitch", value = "ㅤShows the full list of our Partnered Streamers <:twitch1:392000837750226945>\nㅤ", inline=True)
        embed.add_field(name = "ㅤspartner server", value = "ㅤShows the full list of our Partnered Servers <:discord:390659518658379776>", inline=True)
        await ctx.send(embed = embed)
    elif pmessage == "yt":
        embed = discord.Embed(colour = 0xA522B3)
        embed.set_author(name = "[PARTNERS LIST]", icon_url = "https://cdn.discordapp.com/emojis/391999921349197824.png")
        embed.description = "*These lists use a long time to be updated, if you not on after 1h:  `sfeedback`*"
        embed.add_field(name = "ㅤ¤ Partnered Youtubers <:youtube1:391994295223189524>", value = "*PrestiG*  **⇨** [No Link Available](https://www.google.com/)\n\n*INCONNU*  **⇨** [https://www.youtube.com/channel/UCazB2im7mKdGzdKZouDGfRg](https://www.youtube.com/channel/UCazB2im7mKdGzdKZouDGfRg)", inline=False)
        await ctx.send(embed = embed)
    elif pmessage == "twitch":
        embed = discord.Embed(colour = 0xA522B3)
        embed.set_author(name = "[PARTNERS LIST]", icon_url = "https://cdn.discordapp.com/emojis/391999921349197824.png")
        embed.description = "*These lists use a long time to be updated, if you not on after 1h:  `sfeedback`*"
        embed.add_field(name = "ㅤ¤ Partnered Streamers <:twitch1:392000837750226945>", value = "*None*  **⇨** [???](https://www.google.com/)", inline=False)
        await ctx.send(embed = embed)
    elif pmessage == "server":
        embed = discord.Embed(colour = 0xA522B3)
        embed.set_author(name = "[PARTNERS LIST]", icon_url = "https://cdn.discordapp.com/emojis/391999921349197824.png")
        embed.description = "*These lists use a long time to be updated, if you not on after 1h:  `sfeedback`*"
        embed.add_field(name = f"ㅤ¤ Partnered Servers <:discord:390659518658379776>", value = "*Spirit | 精霊  [Bot Support Server]*  **⇨** [https://discord.gg/efF93Gz](https://discord.gg/efF93Gz)\n\n*OtakuAnimeGamerzGuild*  **⇨** [https://discord.gg/vX9yGxa](https://discord.gg/vX9yGxa)\n\n*DiViSiOn | Structure Officiel*  **⇨** [https://discord.gg/vT3xFC8](https://discord.gg/vT3xFC8)", inline=False)
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(colour = 0xA522B3)
        embed.set_author(name = "[PARTNERS LIST]", icon_url = "https://cdn.discordapp.com/emojis/391999921349197824.png")
        embed.description = "Please choose one of the following options:\nㅤ\nㅤ"
        embed.add_field(name = "ㅤspartner yt", value = "ㅤShows the full list of our Partnered Youtubers <:youtube1:391994295223189524>\nㅤ", inline=True)
        embed.add_field(name = "ㅤspartner twitch", value = "ㅤShows the full list of our Partnered Streamers <:twitch1:392000837750226945>\nㅤ", inline=True)
        embed.add_field(name = "ㅤspartner server", value = "ㅤShows the full list of our Partnered Servers <:discord:390659518658379776>", inline=True)
        await ctx.send(embed = embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 3600, commands.BucketType.user)
async def advert(ctx):
    await ctx.send("I'll be asking a series of questions...")
    await asyncio.sleep(5.0)
    await ctx.send("What is your server name?")
    name = await bot.wait_for_message(timeout = 30.0, author = ctx.message.author)
    await ctx.send("How many **humans** are in your server?")
    humans = await bot.wait_for_message(timeout = 30.0, author = ctx.message.author)
    await ctx.send("Provide a **detailed** description of your server.")
    desc = await bot.wait_for_message(timeout = 30.0, author = ctx.message.author)
    await ctx.send("Finally, provide a **permanent** invite link.")
    inv = await bot.wait_for_message(timeout = 30.0, author = ctx.message.author)
    await bot.purge_from(ctx.message.channel, limit = 8)
    await ctx.send("**✅ | Your advertisement has been entered!**")
    embed = discord.Embed(title = "New Advert!", color = ctx.message.author.color, description = "**" + ctx.message.author.name + "#" + ctx.message.author.discriminator + " ID: " + ctx.message.author.id + "**", timestamp = datetime.datetime.utcnow())
    embed.add_field(name = "Server Name", value = name.content)
    embed.add_field(name = "Humans", value = humans.content)
    embed.add_field(name = "Description", value = desc.content)
    embed.add_field(name = "Invite", value = inv.content)
    embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
    embed.set_footer(text = "Advert")
    adv1 = bot.get_channel("391876763069972480")
    await adv1.send(embed = embed)
    await ctx.send(ctx.message.author, "Thanks for your advertisement!")

@bot.command(aliases = ['changelogs'])
async def cl(self):

    if await self.bot.is_owner(self.author):

            developer = bot.get_user(219881141551759360) # commands.get_user(commands.owner_id)
            bot1 = bot.get_user(390478999828037632)

            if developer.avatar_url[54:].startswith('a_'):
                avi = 'https://cdn.discordapp.com/avatars/' + developer.avatar_url[35:-10]
            else:
                avi = developer.avatar_url

            if bot1.avatar_url[54:].startswith('a_'):
                avi1 = 'https://cdn.discordapp.com/avatars/' + bot1.avatar_url[35:-10]
            else:
                avi1 = bot1.avatar_url

            date = "December, 23th 2017"

            embed = discord.Embed(colour = 0xA522B3)
            embed.set_thumbnail(url = avi1)
            embed.set_author(name = f"Changelog: {date}.", icon_url = avi1)
            embed.set_footer(text = f"Created by {developer} on {date}", icon_url = avi)
            embed.add_field(name = "Added:", value = f"- Support Command (**ssupport**)\n*Gives link to Support Server*", inline=False)
            embed.add_field(name = "Removed: ", value = f"ㅤ", inline=False)
            embed.add_field(name = "Changed: ", value = f"ㅤ", inline=False)
            embed.add_field(name = "Fixed: ", value = f"- Corrected **Changelogs Command**", inline=False)
            embed.add_field(name = "Extra Information: ", value = f"ㅤ", inline=False)

            await self.message.delete()
            channel = discord.utils.get(bot.get_all_channels(), guild__name='Spirit | 精霊  [Bot Support Server]', name='changelogs')
            await channel.send(f"@everyone, heyy there is a new update!")
            await channel.send(embed=embed)
    else:
            developer = bot.get_user(219881141551759360) # commands.get_user(commands.owner_id)
            embed = discord.Embed(colour = discord.Colour(0xA522B3))
            embed.set_author(name = f"[CHANGELOGS]")
            embed.set_footer(text = "You dont have permissions to use this command")

            await self.send(embed = embed)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if not os.environ.get('TOKEN'):
        print("No token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
