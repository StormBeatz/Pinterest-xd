from ToXic.texts import start_msg
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("start"))
async def start(_, msg: Message) -> Message:
    return await msg.reply(start_msg)


@Client.on_edited_message(filters.command("start"))
async def start_edited(_, msg: Message) -> Message:
    return await msg.reply(start_msg)
