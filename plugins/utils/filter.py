from config import Config 
from pyrogram.types import Message 
from pyrogram import filters, enums 
from pyrogram.errors import UserNotParticipant
 
async def is_subscribed(_, bot, message: Message):
    channel = Config.AUTH_CHANNEL
    if not channel:
       return False
    try:
       user = await bot.get_chat_member(int(channel), message.from_user.id)
    except UserNotParticipant:
       pass 
    except Exception as e:
       bot.log.exception(e)
       return False
    else:
       if user.status != enums.ChatMemberStatus.BANNED:
          return False 
    return True 
  
is_not_subscribed = filters.create(is_subscribed)
         
async def is_banned(_, __, message: Message):
    return message.from_user.id in Config.BANNED_USERS 
  
is_banned_user = filters.create(is_banned)
