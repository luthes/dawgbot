import discord
from discord.ext import commands
import sys
import time

class Reminders():
    """ Set Reminders """
    def __init__(self, bot):
        self.bot = bot
        self.reminders = open("reminders.txt","r+")
        self.units = {
                  "minutes" : 60, 
                  "hours" : 3600, 
                  "days" : 86400,
                  "weeks" : 604800, 
                  "month" : 2592000, 
                 }

    @commands.command()
    async def remindme(self, message : str, duration : int, *, text : str):
        """ 
        Add a reminder. 
        Syntax: !remindme <time> <message>
        Return: I'll remind you of <message> on <time from now>
        """
        duration = duration.lower()
        author = ctx.message.author
        s = ""

    @commands.command()
    async def forgetme(self):
        """ 
        This will show patch notes for Overwatch. I'd hoped I could just put them in chat, but Discord only allows
        2000 characters, so for now it provides a link.
    
        Syntax: !remindme <time> <message>
        """

    @commands.command()
    async def (self):
        """ 
        This will show patch notes for Overwatch. I'd hoped I could just put them in chat, but Discord only allows
        2000 characters, so for now it provides a link.
    
        Syntax: !remindme <time> <message>
        """
def setup(bot):
    bot.add_cog(Reminders(bot))
