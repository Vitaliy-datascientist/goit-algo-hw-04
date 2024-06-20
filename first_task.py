"""Перше завдання"""

import re


def total_salary(path):
    """Функція  аналізує цей файл(path) і повертає загальну та середню
                                        суму заробітної плати всіх розробників.
    Обробляє: пусті строки між розробниками, відсутність файлу, пошкодження файлу"""
    total = 0
    count_dev = 0
    try:
        with open(path, 'r', encoding='utf_8') as fh:
            for line in fh:
                line = re.sub(r'\s', '', line)
                if not line:
                    continue
                _, salary = line.split(',')
                salary = int(salary)
                total += salary
                count_dev += 1
    except FileNotFoundError:
        return f'{path} не знайдено'
    except ValueError:
        return f'{path} пошкоджено'

    mean = total // count_dev
    return total, mean
