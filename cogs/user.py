import discord
from discord.ext import commands
import aiosqlite
from config import DATABASE

class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx):
        user_id = ctx.author.id
        async with aiosqlite.connect(DATABASE) as db:
            async with db.execute('SELECT coins FROM users WHERE user_id = ?', (user_id,)) as cursor:
                row = await cursor.fetchone()
                if row is None:
                    await db.execute('INSERT INTO users (user_id) VALUES (?)', (user_id,))
                    await db.commit()
                    coins = 1000
                else:
                    coins = row[0]
        await ctx.send(f"{ctx.author.mention}, you have {coins} coins.")

    @commands.command()
    async def connect_wallet(self, ctx, wallet_address: str):
        user_id = ctx.author.id
        if not wallet_address.startswith("0x") or len(wallet_address) != 42:
            await ctx.send("Invalid wallet address.")
            return
        async with aiosqlite.connect(DATABASE) as db:
            await db.execute('UPDATE users SET wallet_address = ? WHERE user_id = ?', (wallet_address, user_id))
            await db.commit()
        await ctx.send("Wallet connected successfully.")

async def setup(bot):
    await bot.add_cog(User(bot))