import time, sys
import discord
import requests
from bs4 import BeautifulSoup as BS
from discord.ext import commands

class Feedback():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bug(self, *args):
        """ 
        Bug reports are held server side. Please provide as much info as possible.
        Thanks for the help! 
        Syntax !bug (string)
        """ 
        bugCount = 0
        with open("/home/steven/bots/dawgbot/cogs/files/DawgFeedback.txt","r+") \
        as f:
            for i in f.readlines():
                bugCount += 1
            for i in args:
                bugArgs = " ".join(args)
            bugString = str(bugCount) + " " +  str(time.strftime("%c")) \
    	     + " " + str(bugArgs) + " \n"
            f.write("[B] " + bugString)
        await self.bot.say('Thanks for the bug report! We will work on getting it fixed!')

def setup(bot):
    bot.add_cog(Feedback(bot))
