"""Перше завдання"""

import re
from pathlib import Path


def total_salary(path: str) -> str | tuple[int, int]:
    """Функція  аналізує цей файл(path) і повертає загальну та середню
                                        суму заробітної плати всіх розробників.
    Обробляє: пусті строки та зайві пробіли, відсутність файлу, пошкодження файлу"""

    path = Path(path)
    total = 0
    count_dev = 0

    try:
        with open(path, 'r', encoding='utf_8') as fh:
            for line in fh:
                line = re.sub(r'\s', '', line)
                if not line:
                    continue
                else:
                    _, salary = line.split(',')
                    salary = int(salary)
                    total += salary
                    count_dev += 1
            mean = total // count_dev
            return total, mean
    except FileNotFoundError:
        return f'{path.absolute()}\nФайл не знайдено'
    except (ValueError, ZeroDivisionError):
        return f'{path.absolute()}\nФайл пошкоджено'
