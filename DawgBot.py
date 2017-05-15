import sys, time
import asyncio
import requests
from bs4 import BeautifulSoup as BS
import discord
from discord.ext import commands
import logging

startup_extensions = [
    "cogs.Feedback.feature",
    "cogs.Feedback.bug",
    "cogs.Feedback.source",
    "cogs.Games.owpatch",
    "cogs.Media.youtube"
]

# Global Variables
DESCRIPTION= '''
Thanks for checking out DawgBot! If you need any help with commands, type !help.
For help with a specific command, type !command help. 

Send any feature requests to zer0, or write them yourself and submit a pull 
request on GitHub (use !source).
'''

# Get key from file
with open('DawgBot.key', 'r') as file:
    key=file.read().replace('\n','')
bot = commands.Bot(command_prefix='!', description=DESCRIPTION)
client = discord.Client()

# Error and Info Logging
# Valid options are typical, debug warn info notset for no logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('DawgBot')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='files.DawgBot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class General:
    """ General Bot Commands """
    
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
    
class Reactions:
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith('hello'):
            msg = '{0.author.mention} please leave me alone.'.format(message)
            await client.send_message(message.channel, msg)
    
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
if __name__ == "__main__":
    for extension in startup_extensions: 
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    bot.run(key)













