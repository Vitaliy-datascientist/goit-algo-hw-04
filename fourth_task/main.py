"""Четверте завдання.
Консольний бот помічник, який розпізнає команди, що вводяться з клавіатури,
                                    та відповідає відповідно до введеної команди."""


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError, TypeError):
            return "Enter the argument for the command."
        except KeyError:
            return f'No contacts found under the name {args[0]}.'

    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return 'Contact added.'
    else:
        return f'A contact named {name} already exists.'


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Contact changed.'
    else:
        return f'No contacts found under the name: {name}.'


@input_error
def show_phone(args, contacts):
    name = args
    return contacts[name]


@input_error
def show_all_contacts(args, contacts):
    if args:
        return 'The command accepts no arguments.'
    if not contacts:
        return 'No contacts.'
    res = ''
    for key in contacts.keys():
        res += f'{key}: {contacts[key]}\n'
    return res


def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command:')
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(*args, contacts))
        elif command == 'all':
            print(show_all_contacts(args, contacts))
        else:
            print('Invalid command.')


if __name__ == '__main__':
    main()
