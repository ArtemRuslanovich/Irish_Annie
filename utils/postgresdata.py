import asyncpg


DATABASE_URL = "postgres://ranabctqvbuyhf:1a93ae9750e400cd45ad57c44fb48d43cdac667e08e59877bbf0ebaea46ddc77@ec2-3-232-218-211.compute-1.amazonaws.com:5432/d5eqr00dsh0g6"

async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL, ssl='require')

async def close_db_connection(connection):
    await connection.close()

async def create_pool():
    return await asyncpg.create_pool(DATABASE_URL, ssl='require')
