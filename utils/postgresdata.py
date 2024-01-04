import asyncpg


DATABASE_URL = "postgresql://postgres:80156120189fap@localhost/Ai_bot"


async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

async def close_db_connection(connection):
    await connection.close()

async def create_pool():
    return await asyncpg.create_pool(user='postgres',
                                    password='80156120189fap',
                                    database='Ai_bot', host='localhost',
                                    port='5432',
                                    command_timeout=60)
