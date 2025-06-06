import aiosqlite

async def setup_db():
    async with aiosqlite.connect("db/database.db") as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                coins INTEGER DEFAULT 1000,
                wallet_address TEXT
            )
        ''')
        await db.commit()