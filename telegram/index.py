from telethon.sync import TelegramClient
import asyncio

api_id = '66268'
api_hash = '467acdae7d88372640245b0dcef9baad'
phone = '16693506323'

async def main():
    async with TelegramClient(phone, api_id, api_hash) as client:
        dialogs = await client.get_dialogs()
        for dialog in dialogs:
            if dialog.name == "ChatGPT 4.0":
                print(dialog)
                print(dialog.name)
                break  # or dialog.title depending on the dialog type

# Python 3.7+
asyncio.run(main())