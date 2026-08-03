import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# -------------------------------------------------------------
# ১. Render-এর জন্য ডামি ওয়েব সার্ভার (Port Scan Timeout বন্ধ রাখার জন্য)
# -------------------------------------------------------------
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is Running Successfully!")

def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

# ব্যাকগ্রাউন্ডে সার্ভার থ্রেড চালু করা
threading.Thread(target=run_dummy_server, daemon=True).start()

# -------------------------------------------------------------
# ২. টেলিগ্রাম ফরওয়ার্ডার বটের কনফিগারেশন
# -------------------------------------------------------------
# আপনার দেওয়া তথ্যসমূহ
API_ID = 34889751
API_HASH = "3639049c90da5caae0e732619e7a54ee"

# সেশন স্ট্রিং Render-এর Environment Variable থেকে নেওয়া হবে
SESSION_STRING = os.environ.get("SESSION_STRING")

if not SESSION_STRING:
    print("❌ Error: SESSION_STRING পাওয়া যায়নি! Render-এ Environment Variable সেট করুন।")
    exit(1)

# Telethon ক্লায়েন্ট তৈরি
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage)
async def my_event_handler(event):
    # নতুন মেসেজ আসলে এখানে প্রসেস হবে
    pass

print("🚀 টেলিগ্রাম ফরওয়ার্ডার বট সফলভাবে ব্যাকগ্রাউন্ডে চালু হয়েছে!")

# বট কানেক্ট ও রান করা
client.start()
client.run_until_disconnected()
