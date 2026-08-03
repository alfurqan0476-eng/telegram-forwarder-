 import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

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

API_ID = 34889751
API_HASH = "3639049c90da5caae0e732619e7a54ee"
SESSION_STRING = os.environ.get("SESSION_STRING")

async def main():
    if not SESSION_STRING:
        print("❌ Error: SESSION_STRING পাওয়া যায়নি!")
        return

    client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

    @client.on(events.NewMessage)
    async def my_event_handler(event):
        pass

    print("🚀 টেলিগ্রাম ফরওয়ার্ডার বট সফলভাবে ব্যাকগ্রাউন্ডে চালু হয়েছে!")
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
