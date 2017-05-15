import discord
from discord.ext import commands
import random

class Toys():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coin(self):
        """ 
        Flip a coin!
 
        Syntax: !owpatch
        """
        flip = random.randint(1,2) 
        if flip == 1:
            await self.bot.say(':tracer:')
        else:
            await self.bot.say(':widow:')

def setup(bot):
    bot.add_cog(Toys(bot))
