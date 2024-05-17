# Доробіть консольного бота помічника
# та додайте обробку помилок за допомоги декораторів.

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    while True:
        try:
            name, phone = args
            contacts[name] = phone
            return "Contact added."
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Enter a command"           
        except IndexError:
            return "Enter the argument for the command."
           
    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    try:
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
            else:
                print("Enter the argument for the command")
    except Exception as e:
        print("Failed to add contact", e)

if __name__ == "__main__":
    main()
   