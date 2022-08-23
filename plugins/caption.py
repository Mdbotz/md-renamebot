from .database import db 
from pyrogram import Client, filters 

@Client.on_message(filters.command('addcaption'))
async def add_caption(bot, message):
    text = message.text.split(" ", 1)
    user_id = message.from_user.id
    if len(text) == 1:
       return await message.reply_text("please provide your custom caption\neg: `/addcaption <caption>`")
    await db.set_caption(user_id, text[1])
    await message.reply_text("<b>caption added successfully</b>")
    
@Client.on_message(filters.command('showcaption'))
async def show_caption(bot, message):
    user_id = message.from_user.id
    caption = await db.get_caption(user_id)
    if not caption:
       return await message.reply_text("You didn't added any custom caption")
    await message.reply_text(f"<b>Your Custom Caption:</b>\n\n`{caption}`")
