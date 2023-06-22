import asyncio

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from ToXic.db import get_served_users
from config import OWNER_ID


@Client.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats(c: Client, message: Message):
    users = len(await get_served_users())
    await message.reply_text(
        f"""ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {c.me.mention} :

➻ <b>ᴜsᴇʀs :</b> {users}"""
    )


@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(client: Client, message: Message):
    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "<b>ᴇxᴀᴍᴘʟᴇ </b>:\n/broadcast [ᴍᴇssᴀɢᴇ] ᴏʀ [ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]"
            )
        query = message.text.split(None, 1)[1]
    susr = 0
    served_users = []
    susers = await get_served_users()
    for user in susers:
        served_users.append(int(user["user_id"]))
    for i in served_users:
        try:
            m = (
                await client.forward_messages(chat_id=i, from_chat_id=y, message_ids=x)
                if message.reply_to_message
                else await client.send_message(i, text=query)
            )
            susr += 1
            await asyncio.sleep(0.2)
        except FloodWait as e:
            flood_time = int(e.value)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except:
            continue

    try:
        await message.reply_text(f"<b>ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ᴛᴏ {susr} ᴜsᴇʀs.</b>")
    except:
        pass
