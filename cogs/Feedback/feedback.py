import asyncio
import discord
import time, sys
import requests
from discord.ext import commands
import json

class Feedback():
    def __init__(self, bot):
        self.bot = bot
        issue_url = ''

    def make_issue(self, title, body=None, assignee=None, milestone=None, labels=None):
        #Read Github Info from file
        owner = 'luthes'
        name = 'dawgbot'
        with open('./cogs/Feedback/accInfo.txt', 'r') as f:
            user = f.readline().strip()
            passw = f.readline().strip()

        url = 'https://api.github.com/repos/{0}/{1}/issues'\
            .format(owner, name)        
        session = requests.Session()
        session.auth = (user, passw)
        issue = {'title': title,
                 'body' : body,
                 'assignee': assignee,
                 'milestone': milestone,
                 'labels': labels}
        r = session.post(url, json.dumps(issue))
        if r.status_code == 201:
        #    print('{0} added to GitHub issues.'.format(title))
        #    print('Response:', r.content)
            Feedback.issue_url = (r.json()["html_url"])
        else:
            print('Could not create issue {0}'.format(title))
            print('Response:', r.content)

    @commands.command(pass_context=True)
    async def feedback(self, ctx, *args):
        """ 
        Feature Requests are held server side. Thanks for the input! 
        File structure: (NUMBER)(DATE)(TIME) - Feature#: (string) \n
    
        Syntax !feature (string)
        """ 
        author = ctx.message.author
        featureCount = 0
        for i in args:
            featureArgs = " ".join(args)
        featureString = """
        Feedback Author: {0}\n 
        Date and Time: {1}\n 
        User Input: {2}\n
        """.format(str(author), str(time.strftime("%c")), str(featureArgs))

        Feedback.make_issue(self, featureArgs, body=featureString, assignee=None, \
                milestone=None, labels=["Bot Created Issues"])

        await self.bot.say("""
            Thanks for the feedback {0}, we appreciate it. You can view any 
            developer comments as well as the status of this issue at the following url: 
            {1}
            """
            .format(author.mention, Feedback.issue_url))
def setup(bot):
    bot.add_cog(Feedback(bot))
