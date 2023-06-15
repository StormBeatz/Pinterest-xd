from ToXic.texts import help_text
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("help"))
async def helper(client: Client, message: Message) -> Message:
    return await message.reply(help_text, disable_web_page_preview=True)


@Client.on_edited_message(filters.command("help"))
async def edited_helper(client: Client, message: Message) -> Message:
    return await message.reply(help_text, disable_web_page_preview=True)
