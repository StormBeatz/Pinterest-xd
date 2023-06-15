from ToXic.pin import download
from ToXic.texts import caption, error_msg, waiting_text
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(
    filters.regex(r"(pinterest\.com/pin/[^/]+|pin\.it/[^/]+)(/$|$)")
)
async def pin_dl(client, msg: Message) -> Message:
    url = f"https://{msg.matches[0].group(1)}"
    msg_tmp: Message = await msg.reply(waiting_text, quote=True)
    
    dl = download(url)
    if dl:
        send_type, url = dl
        await msg_tmp.edit("ᴜᴘʟᴏᴀᴅɪɴɢ....")
        buttons = InlineKeyboardMarkup(
            [
                 [
                    InlineKeyboardButton(text="❄ ᴄʜᴀɴɴᴇʟ ❄", url="https://NOOBSHEAVEN.t.me"),
                    InlineKeyboardButton(text="✨ sᴜᴩᴩᴏʀᴛ ✨", url="https://ChatHuB_x_D.t.me"),
                ],
                [
                    InlineKeyboardButton("🥀ᴅᴇᴠᴇʟᴏᴘᴇʀ🥀", user_id=1057412250)
                ]
            ]
        )

        if send_type == "gif":
            await msg.reply_animation(url, caption=caption, reply_to_message_id=msg.id, reply_markup=buttons)
        
        elif send_type == "video":
            await msg.reply_video(url, caption=caption, reply_to_message_id=msg.id, reply_markup=buttons)
        
        elif send_type == "image":
            await msg.reply_photo(url, caption=caption, reply_to_message_id=msg.id, reply_markup=buttons)
        
        return await msg_tmp.delete()
            
    else:
        return await msg.reply_text(error_msg)
