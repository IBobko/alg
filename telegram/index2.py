from telethon.tl.functions.messages import GetDialogFiltersRequest
from telethon.sync import TelegramClient

api_id = '66268'
api_hash = '467acdae7d88372640245b0dcef9baad'
phone = '16693506323'

with TelegramClient(phone, api_id, api_hash) as client:
    result = client(GetDialogFiltersRequest())
    for filter in result:
        print(filter)