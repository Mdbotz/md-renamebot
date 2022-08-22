import datetime
import motor.motor_asyncio
from config import Config


class Database:
    def __init__(self, uri, name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[name]
        self.col = self.db.users

    def new_user(self, id):
        return dict(
            id=id,
            join_date=datetime.date.today().isoformat(),
            caption=None,
            thumbnail=None,
            upload_mode=None,
            ban_status=dict(
                banned=False,
                reason=None
            )
        )

    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return bool(user)

    async def total_users_count(self):
        count = await self.col.count_documents({})
        banned = await self.col.count_documents({'ban_status.banned': True})
        return count, banned

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})
 
    async def set_thumbnail(self, id, thumbnail):
        await self.col.update_one({'id': id}, {'$set': {'thumbnail': thumbnail}})

    async def get_thumbnail(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('thumbnail', None)

    async def set_caption(self, id, caption):
        await self.col.update_one({'id': id}, {'$set': {'caption': caption}})

    async def get_caption(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('caption', None)

    async def get_user_data(self, id) -> dict:
        user = await self.col.find_one({'id': int(id)})
        return user or None
    
    async def ban_user(self, id, reason):
        ban_status = {'banned': True, 'reason': reason}
        await self.col.update_one({'id': int(id)}, {'$set': {'ban_status': ban_status}})
    
    async def unban_user(self, id):
        ban_status = {'banned': False, 'reason': None}
        await self.col.update_one({'id': int(id)}, {'$set': {'ban_status': ban_status}})
        
    async def get_banned_users(self):
        users = self.col.find({'ban_status.banned': True})
        return [user['id'] async for user in users]
    
    async def change_uploadmode(self, id, mode):
        await self.col.update_one({'id': id}, {'$set': {'upload_mode': mode}})

    async def get_uploadmode(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('upload_mode', None)
    
db = Database(Config.DATABASE_URI, "md-Rename-Bot")
