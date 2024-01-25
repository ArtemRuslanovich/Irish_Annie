import asyncpg


DATABASE_URL = "postgres://fylesvsuxnwlzy:d7c6eae8dc7d78689045cb4e59917d033f10af7992bf2b7851fb9582ba892ff6@ec2-34-238-201-192.compute-1.amazonaws.com:5432/dedbfa2fsjhcua"

async def connect_to_db():
    return await asyncpg.connect(DATABASE_URL)

async def close_db_connection(connection):
    await connection.close()

async def create_pool():
    return await asyncpg.create_pool(DATABASE_URL)
