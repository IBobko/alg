import requests
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Загрузка HTML-страницы
url = 'https://www.bestchange.ru/'  # URL сайта BestChange.ru
response = requests.get(url)
html_content = response.content

# Парсинг HTML-страницы
tables = pd.read_html(html_content)

# Поиск таблицы по индексу или идентификатору
table_index = 0  # индекс таблицы (если на странице есть несколько таблиц)
table_id = 'curr_tab_c'  # идентификатор таблицы

# Извлечение данных из первого столбца таблицы
if table_id in tables[table_index].columns:
    table = tables[table_index][table_id]
else:
    table = tables[table_index]

first_column = table.iloc[:, 0]  # выбор только первого столбца

# Аутентификация и доступ к Google Sheets API
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', ['https://www.googleapis.com/auth/spreadsheets'])
client = gspread.authorize(credentials)

# Открытие таблицы по URL или имени
sheet_url = 'https://docs.google.com/spreadsheets/d/1gaboyjJu4IhnFNHe4T6heEVBKWkK630xsgufdlRtf0U/edit#gid=0'  # URL вашей Google таблицы
sheet = client.open_by_url(sheet_url)
# ИЛИ
# sheet_name = 'Your Sheet Name'  # Имя вашей Google таблицы
# sheet = client.open(sheet_name)

# Выбор листа для записи данных
worksheet = sheet.get_worksheet(0)  # 0 - индекс листа (первый лист)

# Запись данных в выбранный лист
worksheet.update_column(1, first_column.tolist())

print("Данные успешно сохранены в Google Sheets.")