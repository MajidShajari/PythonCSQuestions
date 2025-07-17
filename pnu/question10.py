FILE_NAME = "contacts.txt"


def add_contact(name, phone, address):
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"{name};{phone};{address}\n")


def search_contact(name):
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")
                if len(parts) != 3:
                    continue
                if parts[0].lower() == name.lower():
                    print(f"Phone: {parts[1]}")
                    return
        print("Not found")
    except FileNotFoundError:
        print("No contacts saved yet")


def list_contacts():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        if not lines:
            print("No contacts found")
            return
        for line in lines:
            print(line)
    except FileNotFoundError:
        print("No contacts saved yet")


def main():
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line.lower() == "exit":
            break
        parts = line.split(";")
        if not parts:
            continue
        command = parts[0].strip().lower()

        if command == "add" and len(parts) == 4:
            name = parts[1].strip()
            phone = parts[2].strip()
            address = parts[3].strip()
            add_contact(name, phone, address)
        elif command == "search" and len(parts) == 2:
            search_contact(parts[1].strip())
        elif command == "list":
            list_contacts()
        else:
            continue


if __name__ == "__main__":
    main()
