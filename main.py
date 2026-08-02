import asyncio
from telethon import TelegramClient, events

# আপনার একদম সঠিক Telegram API Credentials
API_ID  34889751
API_HASH "3639049c90da5caaele732619e7a54ee"

# যে ৩টি চ্যানেল থেকে পোস্ট কপি হবে
SOURCE_CHANNELS = [
    'bnpbd_org',
    'bjiofficial',
    'albd1949'
]

# আপনার নিজস্ব চ্যানেল
TARGET_CHANNEL = 'BD_A_J_B'

client = TelegramClient('multi_forwarder_session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def forward_handler(event):
    try:
        await client.send_message(TARGET_CHANNEL, event.message)
        print("সফলভাবে নতুন পোস্ট আপনার চ্যানেলে ফরওয়ার্ড হয়েছে!")
    except Exception as e:
        print(f"ত্রুটি ঘটেছে: {e}")

async def main():
    print("Userbot চালু হচ্ছে...")
    await client.start()
    print("Userbot এখন সম্পূর্ণ চালু এবং কাজ করছে!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())

