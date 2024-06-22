"""Головний функціонал"""

import re
from pathlib import Path
from colorama import Fore
import sys


def search_files(path, sep, last_length):
    """Функція виводить в терміналі всі піддиректорії та файли у вказаній директорії з використанням різних
                          кольорів для піддиректорій та файлів, що полегшить візуальне сприйняття файлової структури."""
    path = Path(path)

    all_objects = list(path.iterdir())

    for item in all_objects:
        length = len(str(item).split('\\'))
        dif = length - last_length

        if item.is_dir():
            print(Fore.MAGENTA + sep + str(item))
            if dif >= 0:
                search_files(item, sep=sep + ('------|' * dif), last_length=length)
            elif dif < 0:
                search_files(item, sep=sep.replace('------|', '', dif * dif), last_length=length)

    for item in all_objects:
        if item.is_file():
            print(Fore.CYAN + sep + str(item))
    print()


def get_path_and_length() -> type[str, int]:
    """Функція обробляє та повертає отриманий шлях та кількість рядків розділені '\' чи '/'"""
    pattern = r'[\\/]+'
    path = sys.argv[1]
    length = len(re.split(pattern, path))
    return path, length
