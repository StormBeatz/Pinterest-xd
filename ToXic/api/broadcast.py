import asyncio

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message

from ToXic.database import get_served_chats, get_served_users
from TelegraphBot import OWNER, app

@Client.on_message(filters.command("stats") & filters.user(OWNER))
async def stats(_, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_text(
        f"""ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {app.me.mention} :

➻ <b>ᴄʜᴀᴛs :</b> {chats}
➻ <b>ᴜsᴇʀs :</b> {users}"""
    )


@Client.on_message(filters.command("broadcast") & filters.user(OWNER))
async def broadcast(client: Client, message: Message):
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "<b>ᴇxᴀᴍᴘʟᴇ </b>:\n/broadcast [ᴍᴇssᴀɢᴇ] ᴏʀ [ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]"
            )
        query = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            await client.copy_message(
                chat_id=i,
                from_chat_id=y,
                message_id=x,
            ) if message.reply_to_message else await client.send_message(i, text=query)
            sent += 1
            await asyncio.sleep(0.2)
        except FloodWait as e:
            flood_time = int(e.value)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except:
            continue

    try:
        await message.reply_text(f"<b>ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ᴛᴏ {sent} ᴄʜᴀᴛs.</b>")
    except:
        pass

    susr = 0
    served_users = []
    susers = await get_served_users()
    for user in susers:
        served_users.append(int(user["user_id"]))
    for i in served_users:
        try:
            m = (
                await client.copy_message(chat_id=i, from_chat_id=y, message_id=x)
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
