from redbot.core.bot import Red

from .custominvite import CustomHelp

async def setup(bot: Red):
    await bot.add_cog(CustomHelp(bot))
