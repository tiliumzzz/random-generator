import json
import os
from typing import List
from .models import Quote


def load_quotes() -> List[Quote]:
    file_path = os.path.join(os.path.dirname(__file__), "quotes.json")
    with open(file_path, "r", encoding="utf-8-sig") as file:
        data = json.load(file)
    return [Quote(**item) for item in data]
