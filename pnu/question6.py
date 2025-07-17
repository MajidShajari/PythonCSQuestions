def main():
    items = set()
    while True:
        try:
            command = input().strip()
        except EOFError:
            break
        if command.lower() == "exit":
            break
        parts = command.split(";")
        if not parts or not parts[0]:
            continue
        action = parts[0].strip().lower()
        if action == "add" and len(parts) == 2:
            item = parts[1].strip()
            if item.isalpha() and item not in items:
                items.add(item)
        elif action == "remove" and len(parts) == 2:
            item = parts[1].strip()
            if item in items:
                items.remove(item)
        elif action == "list":
            if not items:
                print("No items")
            else:
                for item in sorted(items):
                    print(item)
        elif action == "edit" and len(parts) == 3:
            old_item = parts[1].strip()
            new_item = parts[2].strip()
            if old_item in items and new_item.isalpha() and new_item not in items:
                items.remove(old_item)
                items.add(new_item)
            if new_item in items and old_item in items and new_item != old_item:
                items.remove(old_item)
        else:
            continue


if __name__ == "__main__":
    main()
