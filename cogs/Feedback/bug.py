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
        bugFile = open('bugReport.txt', 'r+')
        for i in bugFile.readlines():
            bugCount += 1
        for i in args:
            bugArgs = " ".join(args)
        bugString = str(bugCount) + " " +  str(time.strftime("%c")) \
    	 + " " + str(bugArgs) + " \n"
        bugFile.write(bugString)
        bugFile.close()
        await self.bot.say('Thanks for the bug report! We will work on getting it fixed!')

def setup(bot):
    bot.add_cog(Feedback(bot))
