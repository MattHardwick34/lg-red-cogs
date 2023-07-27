from redbot.core.bot import Red

from .custominvite import CustomInvite

async def setup(bot: Red):
    await bot.add_cog(CustomInvite(bot))
