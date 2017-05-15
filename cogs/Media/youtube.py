import discord
import requests
from bs4 import BeautifulSoup as BS
from discord.ext import commands

class Media():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def yt(self, *args):
        """ 
        Search YouTube for a video and disply the first result in chat
        
        Syntax: !yt overwatch video
        """
        for i in args:
            argstring = "+".join(args)
        yt = 'https://youtube.com'
        r = requests.get(yt + '/results?search_query=' + argstring)
        soup = BS(r.text, "html.parser")
        main_d = soup.find('div', id='results')
        items = main_d.find_all("div", class_='yt-lockup-content')
        for container in items:
            href = container.find('a', class_='yt-uix-sessionlink')['href']
            if href.startswith('/watch'):
                return await self.bot.say(yt+href)

def setup(bot):
    bot.add_cog(Media(bot))
