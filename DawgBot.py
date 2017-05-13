import sys, time
from daemon import Daemon
import asyncio
import requests
from bs4 import BeautifulSoup as BS
import discord
from discord.ext import commands

description = '''
Thanks for checking out DawgBot! If you need any help with commands, type !help.
For help with a specific command, type !command help.
'''

# Get from file
with open('DawgBot.key', 'r') as file:
    key=file.read().replace('\n','')
bot = commands.Bot(command_prefix='!', description=description)
client = discord.Client()
    
@bot.command()
async def hello(member : discord.Member):
    """ 
    Hello World.

    Syntax: !hello zer0
    """
    await bot.say('Hello, {0.name}, welcome!'.format(member))

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
async def yt(args):
    """ 
    Search YouTube for a video and disply the first result in chat
    
    Syntax: !yt overwatch video
    """
    yt = 'https://youtube.com'
    r = requests.get(yt + '/results?search_query=' + args)
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
    Welcomes a new member to th channel.

    Syntax: none.
    """
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

# Run the bot using the key.
bot.run(key)
