import discord
import requests
from bs4 import BeautifulSoup as BS
from discord.ext import commands
import random 

class Toys():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, diesize=6):
        """ 
        Roll some dice. Defaults to a d6. Add a numerical argument to change the
        size of the die. 
        Syntax: !roll, !roll 100, !roll 100000
        """
        dieroll = random.randint(1, diesize)
        await self.bot.say('You rolled a {}.'.format(dieroll))
        
def setup(bot):
    bot.add_cog(Toys(bot))
