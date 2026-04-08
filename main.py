from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

# Details Koyeb ke environment variables se aayengi
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
string_session = os.environ.get("SESSION")

client = TelegramClient(StringSession(string_session), api_id, api_hash)

@client.on(events.NewMessage(chats='realpapsc'))
async def handler(event):
    try:
        # Seedha text copy karke bhejne ke liye taaki 'Forwarded' tag na aaye
        await client.send_message('tiranga_prede', event.message)
    except Exception as e:
        print(f"Error: {e}")

print("Bot chalu ho gaya hai...")
client.start()
client.run_until_disconnected()
