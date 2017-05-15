import discord
import requests
from bs4 import BeautifulSoup as BS
from discord.ext import commands

class OverWatch():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def owpatch(self):
        """ 
        This will show patch notes for Overwatch. I'd hoped I could just put them in chat, but Discord only allows
        2000 characters, so for now it provides a link.
    
        Syntax: !owpatch
        """
        url="https://playoverwatch.com/en-us/game/patch-notes/pc/"
        await selfbot.say('Patch notes are too long for Discord, but you can find them here: ' + url)

def setup(bot):
    bot.add_cog(OverWatch(bot))
