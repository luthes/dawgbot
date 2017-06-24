import asyncio
import discord
import time, sys
import requests
from discord.ext import commands

class Feedback():
    def __init__(self, bot):
        self.bot = bot
    author = ''
    @commands.command(pass_context=True)
    async def feature(self, ctx, *args):
        """ 
        Feature Requests are held server side. Thanks for the input! 
        File structure: (NUMBER)(DATE)(TIME) - Feature#: (string) \n
    
        Syntax !feature (string)
        """ 
        author = ctx.message.author
        featureCount = 0
        with open("/home/steven/bots/dawgbot/cogs/files/DawgFeedback.txt","r+") \
        as f:
            for i in f.readlines():
                featureCount += 1
            for i in args:
                featureArgs = " ".join(args)
            featureString = str(featureCount) + " " +  \
             str(time.strftime("%c")) \
    	     + " " + str(featureArgs) + " \n"
            f.write("[F] " + featureString)
        await self.bot.say(\
            'Thanks for the feedback {0}! We will look into it!'\
            .format(author.mention))

def setup(bot):
    bot.add_cog(Feedback(bot))
