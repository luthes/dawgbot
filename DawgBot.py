import sys, time
import asyncio
import requests
from bs4 import BeautifulSoup as BS
import discord
from discord.ext import commands

# Global Variables

DESCRIPTION= '''
Thanks for checking out DawgBot! If you need any help with commands, type !help.
For help with a specific command, type !command help. 

Send any feature requests to zer0, or write them yourself and submit a pull 
request on GitHub (use !source).
'''

# Get from file
with open('DawgBot.key', 'r') as file:
    key=file.read().replace('\n','')
bot = commands.Bot(command_prefix='!', description=DESCRIPTION)
client = discord.Client()
    
@bot.command()
async def hello(member : discord.Member):
    """ 
    Hello World.

    Syntax: !hello zer0
    """
    for i in args:
         member += " ".join(args) 
    print(member)
    await bot.say('Hello, {0.name}, welcome!'.format(member))

@bot.command()
async def feature(*args):
    """ Feature Requests are held server side. Thanks for the input! 
        File structure: (NUMBER)(DATE)(TIME) - Feature#: (string) \n

        Syntax !feature (string)
    """ 
    featureCount = 0
    featureFile = open('featureRequests.txt', 'r+')
    for i in featureFile.readlines():
        featureCount += 1
    for i in args:
        featureArgs = " ".join(args)
    featureString = str(featureCount) + " " +  str(time.strftime("%c")) \
	 + " " + str(featureArgs) + " \n"
    featureFile.write(featureString)
    featureFile.close()

@bot.command()
async def bug(*args):
    """ Bug reports are held server side. Thanks for the help!

        Syntax !bug (string)
    """ 
    bugCount = 0
    bugFile = open('bugReport.txt', 'r+')
    for i in bugFile.readlines():
        bugCount += 1
    for i in args:
        bugArgs = " ".join(args)
    bugString = str(bugCount) + " " +  str(time.strftime("%c")) \
	 + " " + str(bugArgs) + " \n"
    bugFile.write(bugString)
    bugFile.close()

# @bot.command()
# async def google(args):
#     """ 
#     Google doesn't like when you scrape their front page, so this stops working, if it works at all.
#     I'll look into usign the Google API to make this work, soon(tm).
# 
#     Syntax: !google search for something
#     """
#     query = args.replace(" ", "+")
#     #replaces whitespace with a plus sign for Google compatibility purposes
#     url = ('https://www.google.com/search?q=' + args) 
#     r = requests.get(url.format(query))
#     soup = BS(r.text, "html.parser")
#     links = []
#     for item in soup.find_all('h3', attrs={'class' : 'r'}):
#         links.append(item.a['href'][7:]) # [7:] strips the /url?q= prefix
#         print(links)
#     await bot.say(links)

@bot.command()
async def joined(member : discord.Member):
    """ 
    Display when a member joined the server
    
    Syntax: !joined zer0
    """
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def owpatch():
    """ 
    This will show patch notes for Overwatch. I'd hoped I could just put them in chat, but Discord only allows
    2000 characters, so for now it provides a link.

    Syntax: !owpatch
    """
    url="https://playoverwatch.com/en-us/game/patch-notes/pc/"
    await bot.say('Patch notes are too long for Discord, but you can find them here: ' + url)

@bot.command()
async def source():
    """ 
    The bots source code can be found here.

    Syntax: !source
    """
    url="https://www.github.com/luthes/dawgbot"
    await bot.say('Source code on Github: ' + url)

@bot.command()
async def yt(*args):
    """ 
    Search YouTube for a video and disply the first result in chat
    
    Syntax: !yt overwatch video
    """
    for i in args:
        argstring = "+".join(args)
    yt = 'https://youtube.com'
    r = requests.get(yt + '/results?search_query=' + argstring)
    soup = BS(r.text, "html.parser")
    main_d = soup.find('div', id='results')
    items = main_d.find_all("div", class_='yt-lockup-content')
    for container in items:
        href = container.find('a', class_='yt-uix-sessionlink')['href']
        if href.startswith('/watch'):
            return await bot.say(yt+href)

@client.event
async def on_member_join(member):
    """
    Welcomes a new member to the channel.

    Syntax: none.
    """
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

# Run the bot using the key.
bot.run(key)
