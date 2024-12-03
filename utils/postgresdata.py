import asyncpg


DATABASE_URL = "postgresql://postgres:azQkTLMtBdSoWJEUkrbeRRFDBuRBagNo@junction.proxy.rlwy.net:28579/railway"

async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL, ssl='require')

async def close_db_connection(connection):
    await connection.close()

async def create_pool():
    return await asyncpg.create_pool(DATABASE_URL, ssl='require')
