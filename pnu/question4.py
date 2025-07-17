def main():
    dictionary = {}

    while True:
        try:
            command = input().strip()
        except EOFError:
            break

        if command.lower() == "exit":
            break

        parts = command.split(";")
        if not parts:
            continue

        action = parts[0].strip().lower()

        if action == "add" and len(parts) == 3:
            word = parts[1].strip().lower()
            meaning = parts[2].strip()
            dictionary[word] = meaning

        elif action == "remove" and len(parts) == 2:
            word = parts[1].strip().lower()
            dictionary.pop(word, None)

        elif action == "search" and len(parts) == 2:
            word = parts[1].strip().lower()
            if word in dictionary:
                print(dictionary[word])
            else:
                print("Not found")

        elif action == "list":
            for word in sorted(dictionary.keys()):
                print(f"{word}: {dictionary[word]}")


if __name__ == "__main__":
    main()
