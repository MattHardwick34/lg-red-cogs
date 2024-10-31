from redbot.core import commands

class CustomInvite(commands.Cog):
    """Custom invite text"""

    def __init__(self, bot):
        self.bot = bot
        self._invite_command: Optional[commands.Command] = self.bot.remove_command("help")

    async def cog_unload(self) -> None:
        self.bot.remove_command("help"), self.bot.add_command(  # type:ignore
            self._invite_command
        ) if self._invite_command else None

    @commands.command()
    async def help(self, ctx):
        """Sends message with help info for server"""
        # Your code will go here
        await ctx.send("https://lg1.me/bot-commands")
