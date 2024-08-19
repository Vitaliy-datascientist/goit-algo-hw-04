"""Головний функціонал"""

import re
from pathlib import Path
from colorama import Fore


def print_directories_and_files(path, last_length, sep='------|'):
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
                print_directories_and_files(item, sep=sep + ('------|' * dif), last_length=length)
            elif dif < 0:
                print_directories_and_files(item, sep=sep.replace('------|', '', dif * dif), last_length=length)

    for item in all_objects:
        if item.is_file():
            print(Fore.CYAN + sep + str(item))
    print()


def get_length(path) -> int:
    """Функція обробляє та повертає отриманий шлях та кількість рядків розділені '\' чи '/'"""
    pattern = r'[\\/]+'
    length = len(re.split(pattern, path))
    return length
