import discord
from discord.ext import commands
import os
from db.database import setup_db

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await setup_db()
    print(f"Logged in as {bot.user}")

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

if __name__ == "__main__":
    import asyncio
    async def main():
        await load_cogs()
        await bot.start("YOUR_BOT_TOKEN")
    asyncio.run(main())