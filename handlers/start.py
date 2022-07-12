import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
💔 ʜᴇʏ {message.from_user.mention()} !

        ᴛʜɪs ɪs [{bn}](t.me/{bu}), ʜᴇʏ ʙᴀʙʏ ᴛʜɪs ɪs ꜰᴀsᴛᴇsᴛ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ @STEFFEN999 ᴛᴏ sᴛʀᴇᴀᴍ ᴍᴜsɪᴄ & ᴠɪᴅᴇᴏ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴡɪᴛʜ 0% ʟᴀɢ & 4ᴋ ǫᴜᴀʟɪᴛʏ 😍


┏━━━━━━━━━━━━━━┓
┣★
┣★👑Ⓒⓡⓔⓐⓣⓔⓓ ⓑⓨ: [@STEFFEN999](t.me/{me})
┣★
┗━━━━━━━━━━━━━━┛

💞 ꜰᴏʀ ᴀɴʏ ǫᴜᴇʀɪᴇs ᴅᴍ @STEFFEN999
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥺 ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ​ 🥺", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "👑 ᴏᴡɴᴇʀ 👑", url="https://t.me/STEFFEN999"
                    ),
                    InlineKeyboardButton(
                        "🍒 sᴜᴘᴘᴏʀᴛ 🍒", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        "🔎 ɪɴʟɪɴᴇ 🔎", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "🤯 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ​ 🤯", url="https://github.com/Pkginstallsteffen/Alexia-X-Steffen"
                    )]
            ]
       ),
    )

