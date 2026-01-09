import os
import json

# Путь к файлу с цитатами
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.dirname(current_dir)
quotes_path = os.path.join(backend_dir, "app", "quotes.json")


def test_quotes_file_exists():
    # Проверка что файл quotes.json существует
    assert os.path.exists(quotes_path), f"Файл {quotes_path} не найден"


def test_quotes_valid_json():
    # Проверка что quotes.json - валидный JSON и содержит цитаты
    with open(quotes_path, "r", encoding="utf-8-sig") as f:
        quotes = json.load(f)

    # Должен быть список
    assert isinstance(quotes, list), "quotes.json должен содержать список"

    # Список не должен быть пустым
    assert len(quotes) > 0, "Список цитат не должен быть пустым"

    # Проверяем первую цитату
    first_quote = quotes[0]
    assert isinstance(first_quote, dict), "Цитата должна быть словарем"

    # Должно быть поле с текстом
    assert (
        "text" in first_quote or "quote" in first_quote
    ), "Цитата должна содержать поле 'text' или 'quote'"


def test_backend_structure():
    # Проверяем структуру папок backend
    app_dir = os.path.join(backend_dir, "app")

    # Папка app должна существовать
    assert os.path.exists(app_dir), "Папка app должна существовать"

    # Файл quotes.json должен быть в app
    assert os.path.exists(quotes_path), "Файл quotes.json должен быть в папке app"
