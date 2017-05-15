import discord
import time, sys
import requests
from bs4 import BeautifulSoup as BS
from discord.ext import commands

class Feedback():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def source(self):
        """ 
        The bots source code can be found here.
    
        Syntax: !source
        """
        url="https://www.github.com/luthes/dawgbot"
        await self.bot.say('Source code on Github: ' + url)
def setup(bot):
    bot.add_cog(Feedback(bot))
