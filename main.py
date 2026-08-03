import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# Environment Variables থেকে সিকিউরভাবে ডাটা নিবে
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")

SOURCE_CHANNELS = ['bnpbd_org', 'bjiofficial', 'albd1949']
TARGET_CHANNEL = 'BD_A_J_B'

async def main():
    print("ইউজারবট কানেক্ট হচ্ছে...")
    async with TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH) as client:
        
        @client.on(events.NewMessage(chats=SOURCE_CHANNELS))
        async def forward_handler(event):
            try:
                await client.send_message(TARGET_CHANNEL, event.message)
                print("সফলভাবে নতুন পোস্ট আপনার চ্যানেলে ফরওয়ার্ড হয়েছে!")
            except Exception as e:
                print(f"ত্রুটি ঘটেছে: {e}")

        print("---------------------------------------")
        print("🚀 ইউজারবট সম্পূর্ণ চালু এবং কাজ করছে!")
        print("---------------------------------------")
        
        await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
