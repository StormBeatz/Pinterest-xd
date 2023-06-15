from pyrogram import Client

api_id = 2332973
api_hash = "157025425ad2637898b4710e019f809f"
bot_token = "5768890343:AAFKO0BPEPPzSJjJ2OFNRyhaZQtfASkMPss"

app = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    plugins={"root": "ToXic.api"},
)

app.run()
