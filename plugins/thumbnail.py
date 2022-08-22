from .database import db
from config import Config 
from translation import Translation 
from pyrogram import Client, filters 

@Client.on_message(filters.private & filters.photo)
async def save_photo(bot, message):
    photo = message.photo.file_id
    await db.set_thumbnail(message.from_user.id, photo)
    await message.reply_text(
            text=Translation.NEW_CUSTOM_THUMB_TXT,
            quote=True
        )


@Client.on_message(filters.command("deletethumb"))
async def delete_thumbnail(bot, message):
    user_id = message.from_user.id
    if await db.get_thumbnail(user_id):
       await db.set_thumbnail(user_id, None)
       return await message.reply_text(Translation.REMOVE_CUSTOM_THUMB_TXT)
    await message.reply_text(Translation.THUMB_NOT_FOUND_TXT)
    
@Client.on_message(filters.command("showthumb"))
async def show_thumb(bot, message):
    user_id = message.from_user.id
    thumbnail = await db.get_thumbnail(user_id)
    if not thumbnail:
       return await message.reply_text(Translation.THUMB_NOT_FOUND_TXT)
    try:
      await message.reply_photo(thumbnail)
    except Exception as e:
      await message.reply_text("Error: `{e}`")
