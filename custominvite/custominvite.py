from redbot.core import commands

class CustomInvite(commands.Cog):
    """Custom invite text"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        """Sends message with an invite to the server"""
        # Your code will go here
        await ctx.send("Invite your friends here? https://discord.gg/LondonGaymers")
