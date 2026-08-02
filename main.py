import asyncio
from telethon import TelegramClient, events

# আপনার সঠিক API Credentials (API_HASH ফিক্স করা হয়েছে)
API_ID = 34889751
API_HASH = "3639049c90da5caa1e732619e7a54ee"

# চ্যানেল লিস্ট
SOURCE_CHANNELS = [
    'bnpbd_org',
    'bjiofficial',
    'albd1949'
]

TARGET_CHANNEL = 'BD_A_J_B'

async def main():
    print("Userbot চালু হচ্ছে...")
    
    # Render / Python 3.10+ Event Loop Fix
    async with TelegramClient('multi_forwarder_session', API_ID, API_HASH) as client:
        
        @client.on(events.NewMessage(chats=SOURCE_CHANNELS))
        async def forward_handler(event):
            try:
                await client.send_message(TARGET_CHANNEL, event.message)
                print("সফলভাবে নতুন পোস্ট আপনার চ্যানেলে ফরওয়ার্ড হয়েছে!")
            except Exception as e:
                print(f"ত্রুটি ঘটেছে: {e}")

        print("\n-------------------------------------------")
        print("🚀 ইউজারবট সম্পূর্ণ চালু এবং কাজ করছে!")
        print("-------------------------------------------\n")
        
        await client.run_until_disconnected()

if __name__ == '__main__':
    # আধুনিক Asyncio Runner
    asyncio.run(main())
