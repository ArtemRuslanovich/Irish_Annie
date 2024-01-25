import asyncpg

class Request:
    def __init__(self, connector: asyncpg.pool.Pool) -> None:
        self.connector = connector

    async def add_data(self, user_id, user_name):
        query = f"INSERT INTO userscredits (user_id, user_name) VALUES ({user_id}, '{user_name}')" \
             f" ON CONFLICT (user_id) DO UPDATE SET user_name='{user_name}'" 
        await self.connector.execute(query)

    async def get_credits_and_id(self, user_id):
        query = f"SELECT credits FROM userscredits WHERE user_id = {user_id}"
        result = await self.connector.fetchrow(query)
        credits = result['credits'] if result else 0

        return credits, user_id
    
    async def add_bonus_credits(self, user_id: int, bonus_credits: int) -> None:
        query = (
            'UPDATE userscredits '
            'SET credits = credits + $1 '
            'WHERE user_id = $2'
        )
        await self.connector.execute(query, bonus_credits, user_id)
    
    async def add_credits(self, user_id: int, credits: int):
        query = (
            'INSERT INTO userscredits (user_id, user_name, credits) '
            'VALUES ($1, (SELECT user_name FROM userscredits WHERE user_id = $1), $2) '
            'ON CONFLICT (user_id) DO UPDATE SET credits = userscredits.credits + EXCLUDED.credits'
        )

        await self.connector.execute(query, user_id, credits)

    async def add_name(self, user_id, user_name):
        query = f"INSERT INTO userscredits (user_id, user_name) VALUES ({user_id}, '{user_name}')" \
             f" ON CONFLICT (user_id) DO UPDATE SET user_name='{user_name}'"
        await self.connector.execute(query)

    async def set_gender(self, user_id, gender):
        query = f"INSERT INTO userscredits (user_id, gender) VALUES ({user_id}, '{gender}')" \
             f" ON CONFLICT (user_id) DO UPDATE SET gender='{gender}'"
        await self.connector.execute(query)

    @classmethod
    async def check_credits(cls, user_id, connector: asyncpg.pool.Pool):
        query = "SELECT credits FROM userscredits WHERE user_id = $1"
        result = await connector.fetchrow(query, user_id)
        credits = result['credits'] if result else 0

        enough_credits = credits >= 1  # Check if at least one credit is available

        return enough_credits
    
    @staticmethod
    async def subtract_credits(user_id: int, connection: asyncpg.Connection):
        try:
            query = """
                UPDATE userscredits
                SET credits = credits - 1  # Deduct one credit
                WHERE user_id = $1
                RETURNING credits;
            """
            result = await connection.fetchrow(query, user_id)
            
            if result:
                new_credits = result['credits']
                print(f"User {user_id} now has {new_credits} credits.")
        except Exception as e:
            print(f"Error subtracting credits: {e}")

    