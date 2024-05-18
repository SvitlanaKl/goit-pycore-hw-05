# Доробіть консольного бота помічника
# та додайте обробку помилок за допомоги декораторів.

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Name doesn't exist."
        except IndexError:
            return "Please give me name"
        
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if contacts[name]:
        contacts[name] = phone
        return "Contact updated."  
    
@input_error
def show_phone(args, contacts):
    name = args[0]
    phone = contacts[name]
    return f'Your contact {name} has following number {phone}'

def show_all(contacts: dict):
    if not contacts:
        return 'No contacts'
    result = ''
    for name, phone in contacts.items():
        result += f'{name}-{phone}\n'
    return result      

def main():
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
        elif command == "show_phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Enter the argument for the command")
    
if __name__ == "__main__":
    main()
   