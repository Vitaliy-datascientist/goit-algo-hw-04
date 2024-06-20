"""Друге завдання"""

import re
from pathlib import Path


def get_cats_info(path: str) -> str | list[dict]:
    """Функція читає цей файл та повертає список словників
                                        з інформацією про кожного кота.
    Обробляє: пусті строки та зайві пробіли, відсутність файлу, пошкодження файлу."""

    res = []
    path = Path(path)

    try:
        with open(path, 'r', encoding='utf-8') as fh:
            for line in fh:
                line = re.sub(r'\s', '', line)
                if not line:
                    continue
                else:
                    cat_id, name, age = line.split(',')
                    cat_info = {'id': cat_id, 'name': name, 'age': age}
                    res.append(cat_info)
    except FileNotFoundError:
        return f'{path.absolute()}\nФайл не знайдено'
    except ValueError:
        return f'{path.absolute()}\nФайл пошкоджено'
    else:
        return res


if __name__ == '__main__':
    print(get_cats_info('test.txt'))
