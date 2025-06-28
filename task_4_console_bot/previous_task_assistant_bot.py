# assistant_bot.py
""" Асистент-бот для управління контактами.
Цей бот дозволяє додавати, змінювати та переглядати контакти.
Він підтримує команди:                                  
- hello: вітання користувача
- add [name] [phone]: додавання нового контакту
- change [name] [new_phone]: зміна номера телефону для існуючого контакту
- phone: виведення номера телефону для вказаного контакту
- all: виведення всіх збережених контактів
- close та exit: вихід з програми"""
def parse_input(user_input):
    """Парсить введену користувачем команду та аргументи. Повертає команду та список аргументів"""              
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """ Додає новий контакт до списку контактів"""
    if len(args) != 2:
        return "Invalid number of arguments for 'add' command. Please use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """Змінює номер телефону для існуючого контакту"""
    if len(args) != 2:
        return "Invalid number of arguments for 'change' command. Please use: change [name] [new_phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found"

def show_phone(args, contacts):
    """Виводить номер телефону для вказаного контакту"""
    if len(args) != 1:
        return "Invalid number of arguments for 'phone' command. Please use: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    """Виводить усі збережені контакти з номерами телефонів"""
    if not contacts:
        return "No contacts saved."
    all_contacts = []
    for name, phone in contacts.items():
        all_contacts.append(f"{name}: {phone}")
    return "\n".join(all_contacts)

def main():
    """Головна функція для запуску асистент-бота"""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()