class Translation(object):
    
    START_TXT = """ <b> Hi {} ,
 I'm A Simple Rename Bot With Permanent Thumbnail And Custom Caption support!</b>
<b>Click help button to know more about me !</b>\n 
"""
    PROGRESS_BAR = """\n
╭───[**🔅Progress Bar🔅**]───⍟
│
├<b>📁 : {1} | {2}</b>
│
├<b>🚀 : {0}%</b>
│
├<b>⚡ : {3}/s</b>
│
├<b>⏱️ : {4}</b>
╰─────────────────⍟"""
    HELP_TXT = """
<b><i><u>✨ AVAILABLE COMMANDS:</u> 
➢ /rename - To rename a file or video or audio
➢ /settings - To configure your configs 
➢ /addcaption - To add a custom caption
➢ /showcaption - To show your custom caption
➢ /deletethumb - To remove your custom thumbnail 
➢ /showthumb - To show your custom thumbnail
<u>🔥 FEATURES:</u>
➻ support custom caption
➻ support custom thumbnail 
➻ Available three upload mode  
➻ support broadcast</i></b>
""" 
    ABOUT_TXT = """
╔════❰ RENAME BOT ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃ʙᴏᴛ : [{}](https://t.me/{})
║┣⪼👦ᴄʀᴇᴀᴛᴏʀ : [ᴍᴅᴀᴅᴍɪɴ](https://t.me/mdadmin2)
║┣⪼📡ʜᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ3
║┣⪼📚ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ ᴀsʏɴᴄɪᴏ 2.0.0 
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : 0.0.1
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
"""
    THUMBNAIL_TXT = """
<b>🖼️ CUSTOM THUMBNAIL</b>
you can add custom thumbnail simply by sending a photo to me 
"""
    CUSTOM_CAPTION_TXT = """
<b>📝 CUSTOM CAPTION</b>
➢ /addcaption <your caption> - To add your custom caption 
<b>AVAILABLE FILLINGS:</b>
- `{filename}` - new file name
- `{size}` - size of the media
- `{duration}` - duration of the media
"""
    
    SETTINGS_TXT = "<b><u>⚙️ SETTINGS</u>\nConfigure your settings using this buttons</b>"
    BANNED_TXT = "<b>Sorry dude, You would be banned from using me</b>"
    DOWNLOAD_START_TXT = "<b>Downloading To My server !!</b>"
    UPLOAD_START_TXT = "<b>Uploading into telegram</b>"
    UPLOAD_SUCCESS_TXT = "<b>Thank you for Using Me ❤️</b>"
    NEW_CUSTOM_THUMB_TXT = "✔️ Thumbnail Successfully Added"
    REMOVE_CUSTOM_THUMB_TXT = "🗑️ Thumbnail Successfully Removed"
    DOWNLOAD_SUCCESS_TXT = "<b>Media Downloded successfully 🎉</b>"
    THUMB_NOT_FOUND_TXT = "Didn't found any thumbnail yet"
    REPLY_MEDIA_TXT = "<b>Please Reply To An File or video or audio With filename & extension</b>"
