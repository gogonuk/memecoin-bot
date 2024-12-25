from telethon import TelegramClient, events
import yaml
import logging
import os

# Load config
with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

API_ID = config["telegram"]["api_id"]
API_HASH = config["telegram"]["api_hash"]
SESSION_NAME = "memecoin_session"

# Set up logging
logging.basicConfig(filename='data/logs/telegram_monitor.log', level=logging.INFO)

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage(chats=config["telegram"]["groups"]))
async def monitor(event):
    message = event.raw_text
    if "Contract" in message:
        logging.info(f"New call: {message}")
        # Save to log file
        try:
            with open("data/logs/calls_log.txt", "a") as f:
                f.write(message + "\n")
        except Exception as e:
            logging.error(f"Failed to write to log file: {e}")

async def main():
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())