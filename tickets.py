import discord
from discord.ext import commands

class Ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="تكت")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ticket(self, ctx):
        guild = ctx.guild

        # يمنع فتح أكثر من تكت لنفس الشخص
        for channel in guild.text_channels:
            if channel.name == f"ticket-{ctx.author.name}":
                await ctx.send("عندك تكت مفتوح بالفعل ✅")
                return

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            ctx.author: discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True
            )
        }

        channel = await guild.create_text_channel(
            f"ticket-{ctx.author.name}",
            overwrites=overwrites
        )

        await channel.send(f"{ctx.author.mention} تم فتح التكت ✅")


async def setup(bot):
    await bot.add_cog(Ticket(bot))
