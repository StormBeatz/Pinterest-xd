from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType

from ToXic.texts import start_msg
from ToXic.db import add_served_user


@Client.on_message(filters.command("start"))
async def start(_, msg: Message):
    if msg.chat.type == ChatType.PRIVATE:
        await add_served_user(msg.from_user.id)
    return await msg.reply_text(start_msg)
