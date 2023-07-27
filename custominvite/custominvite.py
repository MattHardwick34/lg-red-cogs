from redbot.core import commands

class CustomInvite(commands.Cog):
    """Custom invite text"""

    def __init__(self, bot):
        self.bot = bot
        self._invite_command: Optional[commands.Command] = self.bot.remove_command("invite")

    async def cog_unload(self) -> None:
        self.bot.remove_command("invite"), self.bot.add_command(  # type:ignore
            self._invite_command
        ) if self._invite_command else None

    @commands.command()
    async def invite(self, ctx):
        """Sends message with an invite to the server"""
        # Your code will go here
        await ctx.send("Invite your friends here? https://discord.gg/LondonGaymers")
