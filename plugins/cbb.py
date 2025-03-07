#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝐎ᴡɴᴇʀ : <a href='t.me/Adult_Flux'>𝐓ʀᴀғᴀʟɢᴀʀ 𝐃. 𝐋ᴀᴡ🍅</a>\n○ 𝐀ɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href='https://t.me/Anime_Flux'>𝐀ɴɪᴍᴇ 𝐅ʟᴜx</a>\n○ 𝐇ᴇɴᴛᴀɪ 𝐂ʜᴀɴɴᴇʟ : <a href='t.me/adult_flux'>𝐀ᴅᴜʟᴛ 𝐅ʟᴜx</a>\n○ 𝐃ᴇᴠʟᴏᴘᴇʀ : <a href='https://t.me/adult_flux'>𝐒ᴀɴJɪ 𝐒αᴍᴀ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("• ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('ᴅᴇᴠᴇʟᴏᴘᴇʀ •', url='https://t.me/anime_flux')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
