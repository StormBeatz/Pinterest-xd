from pyrogram import Client

import config


app = Client(
    "Pinterest-DL",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins={"root": "ToXic"},
)

app.run()
