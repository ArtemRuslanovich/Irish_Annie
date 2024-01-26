import asyncpg


DATABASE_URL = "postgres://rbbftznippvgcs:a63f60adbeff86b64a857cef8250178a45a34aa81337f7a6d0f6d49c3258dcb5@ec2-54-83-138-228.compute-1.amazonaws.com:5432/dembn1uh43k4l3"

async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL, ssl='require')

async def close_db_connection(connection):
    await connection.close()

async def create_pool():
    return await asyncpg.create_pool(DATABASE_URL, ssl='require')
