from transformers import GPT2Tokenizer
import os


def split_message_by_tokens_and_save(file_path, max_tokens=26000):
    """
    This function reads a text file, tokenizes the content using GPT2Tokenizer, and splits it into parts.
    Each part contains up to max_tokens tokens. The parts are then saved as separate text files.

    Parameters:
    file_path (str): Path to the text file that will be tokenized and split.
    max_tokens (int): Maximum number of tokens per file part (default is 26000).

    Returns:
    int: The number of parts created from the original file.

    Raises:
    FileNotFoundError: If the specified file_path does not exist.
    """
    # Проверяем, существует ли файл
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found")

    # Инициализация токенизатора
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    # Чтение файла
    with open(file_path, 'r', encoding='utf-8') as file:
        message = file.read()

    # Токенизация всего сообщения
    tokens = tokenizer.encode(message)

    # Разбиение сообщения на части по max_tokens
    parts = []
    current_part = []
    current_length = 0

    for token in tokens:
        current_part.append(token)
        current_length += 1
        if current_length >= max_tokens:
            parts.append(current_part)
            current_part = []
            current_length = 0

    # Добавление последней части, если она не пуста
    if current_part:
        parts.append(current_part)

    # Создание и запись файлов для каждой части
    for index, part in enumerate(parts):
        part_file_path = f"{file_path}_part_{index + 1}.txt"
        with open(part_file_path, 'w', encoding='utf-8') as part_file:
            part_file.write(tokenizer.decode(part))

    return len(parts)  # Возвращаем количество созданных файлов


# Путь к файлу с сообщением
file_path = "/home/nox/zakon1.txt"

# Выполнение функции и вывод количества созданных файлов
try:
    num_parts = split_message_by_tokens_and_save(file_path)
    print(f"Created {num_parts} parts.")
except FileNotFoundError as e:
    print(e)
