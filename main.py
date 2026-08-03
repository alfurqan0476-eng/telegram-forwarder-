import os, asyncio, threading
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from http.server import HTTPServer, BaseHTTPRequestHandler

# --- ডামি ওয়েব সার্ভার (Render ও UptimeRobot-এর জন্য) ---
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is Running Successfully!")

def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

# --- টেলিগ্রাম বট কনফিগারেশন ---
API_ID = 34889751
API_HASH = "3639049c90da5caae0e732619e7a54ee"
SESSION_STRING = os.environ.get("SESSION_STRING")

# 🎯 আপনার টার্গেট চ্যানেল
TARGET_CHANNEL = "@BD_A_J_B"

# 📌 ৩টি দলের অরিজিনাল ইউজারনেম ও মেসেজের নিচের লেখা
SOURCE_CHANNELS = {
    "albd1949": "\n\n🏛️ **উৎস:** বাংলাদেশ আওয়ামী লীগ (#AwamiLeague)",
    "bnpbd_org": "\n\n🏛️ **উৎস:** বাংলাদেশ জাতীয়তাবাদী দল - বিএনপি (#BNP)",
    "bjiofficial": "\n\n🏛️ **উৎস:** বাংলাদেশ জামায়াতে ইসলামী (#JamaatEIslami)"
}

async def main():
    if not SESSION_STRING:
        print("❌ SESSION_STRING পাওয়া যায়নি!")
        return
        
    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
    
    @client.on(events.NewMessage)
    async def my_event_handler(event):
        chat = await event.get_chat()
        chat_username = getattr(chat, 'username', None)
        
        # মেসেজটি এই ৩টি দলের কোনো একটি চ্যানেল থেকে আসলে
        if chat_username and chat_username.lower() in [u.lower() for u in SOURCE_CHANNELS.keys()]:
            # অরিজিনাল কী (key) খুঁজে বের করা
            matched_key = next(k for k in SOURCE_CHANNELS if k.lower() == chat_username.lower())
            footer_text = SOURCE_CHANNELS[matched_key]
            
            original_text = event.text or ""
            new_text = original_text + footer_text

            # ফটো/ভিডিও বা সাধারণ মেসেজ অনুযায়ী ফরওয়ার্ড করা
            if event.media:
                await client.send_file(TARGET_CHANNEL, event.media, caption=new_text)
            else:
                await client.send_message(TARGET_CHANNEL, new_text)

    print("🚀 টেলিগ্রাম ফরওয়ার্ডার বট চালু হয়েছে!")
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
