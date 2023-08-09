import yt_dlp
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
from io import BytesIO
from bs4 import BeautifulSoup

@Client.on_message(filters.regex(r"(pinterest\.com/pin/[^/]+|pin\.it/[^/]+)(/$|$)"))
async def handle_pinterest_link(_, message: Message):
    await message.reply("🔍")
    pinterest_post_url = re.search(r"(https?://[^\s]+)", message.text)
    if pinterest_post_url:
        pinterest_post_url = pinterest_post_url.group(0)
        await download_pin_or_yt_media(message, Client, pinterest_post_url)
    else:
        await message.reply_text("Failed to extract Pinterest URL.")

async def download_pin_or_yt_media(message, bot, link, quality=720):
    chat_id = message.chat.id
    try:
        ydl_opts = {
            "format": f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "merge_output_format": "mp4",
            "multithreaded": True,
            "no-playlist": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(link, download=True)
                file_path = ydl.prepare_filename(info)
                await Client.send_video(chat_id, video=file_path,caption=f" • Video uploaded by ")
                os.remove(file_path)
                return
            except yt_dlp.DownloadError as e:
                print(f"Error downloading YouTube content: {e}")
                pass
        response = requests.get(link)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        image_url = soup.find('meta', attrs={'property': 'og:image'})['content']
        response = requests.get(image_url)
        response.raise_for_status()
        with open("temp_image.jpg", "wb") as f:
            f.write(response.content)
        with open("temp_image.jpg", "rb") as photo_file:
            await Client.send_photo(chat_id, photo=photo_file,caption=f"• Uploaded by huehue •")
        os.remove("temp_image.jpg")
        print("Removed temporary photo file.")
    except Exception as e:
        print(f"Error occurred: {e}")
        await message.reply_text("Failed to download media.")
