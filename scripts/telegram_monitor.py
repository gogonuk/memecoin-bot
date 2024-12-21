from telethon import TelegramClient, events
import yaml

# Load config
with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

API_ID = config["telegram"]["api_id"]
API_HASH = config["telegram"]["api_hash"]
SESSION_NAME = "memecoin_session"

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage(chats=config["telegram"]["groups"]))
async def monitor(event):
    message = event.raw_text
    if "Contract" in message:
        print(f"New call: {message}")
        # Save to log file
        with open("data/logs/calls_log.txt", "a") as f:
            f.write(message + "\n")

async def main():
    await client.start()
    await client.run_until_disconnected()

if name == "main":
    import asyncio
    asyncio.run(main())
