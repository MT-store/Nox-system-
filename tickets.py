import discord
from discord.ext import commands

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def تكت(self, ctx):
        guild = ctx.guild
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            ctx.author: discord.PermissionOverwrite(view_channel=True, send_messages=True)
        }

        channel = await guild.create_text_channel(
            f"ticket-{ctx.author.name}",
            overwrites=overwrites
        )

        await channel.send(f"{ctx.author.mention} تم فتح التكت ✅")

async def setup(bot):
    await bot.add_cog(Ticket(bot))
