import discord
import time, sys
import requests
from bs4 import BeautifulSoup as BS
from discord.ext import commands

class Feedback():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def feature(self, *args):
        """ 
        Feature Requests are held server side. Thanks for the input! 
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
        await self.bot.say('Thanks for the feature request! We will look into it!')

def setup(bot):
    bot.add_cog(Feedback(bot))
