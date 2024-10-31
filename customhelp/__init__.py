from redbot.core.bot import Red

from .customhelp import CustomHelp

async def setup(bot: Red):
    await bot.add_cog(CustomHelp(bot))
