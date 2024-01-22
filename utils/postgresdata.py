import asyncpg


DATABASE_URL = "postgres://gufsckxwaehtpv:86d93b93e6526ff7dc4bcc2a40cb6d1798f32811ffd5ceb6208fc011c8181e7d@ec2-54-234-13-16.compute-1.amazonaws.com:5432/dbjia233jsi6m2"


async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL, ssl='require')

async def close_db_connection(connection):
    await connection.close()

async def create_pool():
    return await asyncpg.create_pool(user='gufsckxwaehtpv',
                                    password='86d93b93e6526ff7dc4bcc2a40cb6d1798f32811ffd5ceb6208fc011c8181e7d',
                                    database='dbjia233jsi6m2', host='ec2-54-234-13-16.compute-1.amazonaws.com',
                                    port='5432',
                                    command_timeout=60, ssl='require')
