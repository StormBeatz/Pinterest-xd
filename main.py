from pyrogram import Client

api_id = 
api_hash = ""
bot_token = ""

app = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    in_memory=True,
    plugins={"root": "ToXic"},
)

app.run()
