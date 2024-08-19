"""Третє завдання.
Скрипт приймає шлях до директорії в якості аргументу командного
                          рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів."""
import sys
from third_task.functionality import print_directories_and_files, get_length


def main():
    """Головна функція"""

    try:
        path = sys.argv[1]
        length = get_length(path)
        print_directories_and_files(path, length)
    except FileNotFoundError:
        print('Директорію не знайдено.')
    except NotADirectoryError:
        print('Не є директорією.')


if __name__ == '__main__':
    main()
