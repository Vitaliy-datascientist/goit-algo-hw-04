"""Четверте завдання.
Консольний бот помічник, який розпізнає команди, що вводяться з клавіатури,
                                    та відповідає відповідно до введеної команди."""


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added.'


def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        add_contact(args, contacts)
        return 'Contact changed.'
    else:
        return f'No contacts found under the name {name}.'


def show_phone(args, contacts):
    if not len(args) == 1:
        return 'Incorrect arguments, try again.'
    else:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return f'No contacts found under the name {name}.'


def show_all_contacts(args, contacts):
    if args:
        return 'The command accepts no arguments.'
    elif not contacts:
        return 'No contacts.'
    res = ''
    for key in contacts.keys():
        res += f'{key} - {contacts[key]}\n'
    return res


def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command:')
        command, *args = parse_input(user_input)
        try:
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
                print(show_phone(args, contacts))
            elif command == 'all':
                print(show_all_contacts(args, contacts))
            else:
                print('Invalid command.')
        except ValueError:
            print('Incorrect arguments, try again.')


if __name__ == '__main__':
    main()
