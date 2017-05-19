import discord
from discord.ext import commands
import random

class Toys():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coin(self, flips=1):
        """ 
        Flip a coin! Defaults to one flip, add number to flip multiple times, with
        a maximum of 5 flips.
 
        Syntax: !coin, !coin 5
        """
        if flips > 5:
            await self.bot.say('Input too large.')
        else:
            for i in range(0,flips):
                flip = random.randint(1,2) 
                if flip == 1:
                    await self.bot.say('<:tracer:311966007746887683>')
                else:
                    await self.bot.say('<:widow:311966007935762432>')

def setup(bot):
    bot.add_cog(Toys(bot))
