from .custominvite import CustomInvite


async def setup(bot):
    await bot.add_cog(CustomInvite(bot))
