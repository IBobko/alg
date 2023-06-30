import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)
client = gspread.authorize(creds)

# Открыть существующую таблицу по URL
spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/your_spreadsheet_id')

# Создать новую таблицу
spreadsheet = client.create('Название вашей таблицы')

# Получить список листов
sheets = spreadsheet.worksheets()

# Получить доступ к листу по индексу
sheet = sheets[0]

# Получить значение ячейки
cell_value = sheet.acell('A1').value

# Обновить значение ячейки
sheet.update('A1', 'Новое значение')