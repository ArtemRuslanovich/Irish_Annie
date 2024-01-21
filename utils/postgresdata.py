import asyncpg


DATABASE_URL = "postgres://uutzeepoeiudrz:b1f9e4066b489e6aa6d432634ce5f9df1305fb54a88c6a2356925b70773d5cf4@ec2-54-234-13-16.compute-1.amazonaws.com:5432/da7qujukih0gqg"


async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

async def close_db_connection(connection):
    await connection.close()

async def create_pool():
    return await asyncpg.create_pool(user='uutzeepoeiudrz',
                                    password='b1f9e4066b489e6aa6d432634ce5f9df1305fb54a88c6a2356925b70773d5cf4',
                                    database='da7qujukih0gqg', host='ec2-54-234-13-16.compute-1.amazonaws.com',
                                    port='5432',
                                    command_timeout=60)
