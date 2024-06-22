"""Третє завдання.
Скрипт приймає шлях до директорії в якості аргументу командного
                          рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів."""

from functionality import search_files, get_path_and_length


def main():
    """Головна функція"""
    sep = '------|'
    try:
        path, length = get_path_and_length()
        search_files(path, sep, length)
    except FileNotFoundError:
        print(f'{path}\nДиректорію не знайдено')
    except NotADirectoryError:
        print(f'{path}\nНе є директорією')


if __name__ == '__main__':
    main()
