import requests
from bs4 import BeautifulSoup

# Загрузка HTML-страницы
url = 'https://www.bestchange.ru/'  # URL сайта BestChange.ru
response = requests.get(url)
html_content = response.content

# Парсинг HTML-страницы
soup = BeautifulSoup(html_content, 'html.parser')

# Поиск таблицы по идентификатору
table = soup.find('table', {'id': 'curr_tab_c'})

# Проверка на наличие таблицы
if table is not None:
    # Извлечение данных из первого столбца таблицы
    rows = table.find_all('tr')

    # Перебор строк и извлечение данных из первого столбца
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 0:
            data = cells[0].text.strip()
            print(data)
else:
    print("Таблица с идентификатором 'curr_tab_c' не найдена на странице.")