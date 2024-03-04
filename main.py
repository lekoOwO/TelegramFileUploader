#!/usr/bin/env python3

from argparse import ArgumentParser
from os import environ
from sys import argv

from telethon import TelegramClient, events, sync

api_id = environ.get("API_ID")
if not api_id:
    print("API_ID is missing")
    exit(1)
api_id = int(api_id)
api_hash = environ.get("API_HASH")
if not api_hash:
    print("API_HASH is missing")
    exit(1)
bot_token = environ.get("BOT_TOKEN")
if not bot_token:
    print("BOT_TOKEN is missing")
    exit(1)

bot = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)


async def main(client: TelegramClient, to: str, message: str, files: list[str]):
    # Printing upload progress
    def callback(current, total):
        print(f"Uploaded{current}/{total}")

    msg = await client.send_file(
        entity=to, file=files, caption=message, progress_callback=callback
    )


parser = ArgumentParser(prog="TelegramFileUploader", epilog="@GitHub:xz-dev")
parser.add_argument("--to", help="Chat ID or username")
parser.add_argument("--message", help="Message")
parser.add_argument("--files", help="Files", nargs="+")
args = parser.parse_args()
with bot:
    bot.loop.run_until_complete(main(bot, args.to, args.message, args.files))

# Example:
# python3 main.py --to "me" --message "Hello, World!" --files "file1.txt" "file2.txt"
