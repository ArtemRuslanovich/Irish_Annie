import asyncpg


DATABASE_URL = "postgres://erxacamhbjmufg:6ce4d69f7829aee4e6513a4c04aa853028a1f854275fef318240931f0e823dd1@ec2-54-167-29-148.compute-1.amazonaws.com:5432/d6n9bql7d4iaim"

async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL, ssl='require')

async def close_db_connection(connection):
    await connection.close()

async def create_pool():
    return await asyncpg.create_pool(DATABASE_URL, ssl='require')
