def main():
    books = []

    while True:
        try:
            command = input().strip()
        except EOFError:
            break
        if command.lower() == "exit":
            break

        parts = command.split(";")
        if len(parts) == 0:
            continue

        action = parts[0].strip().lower()

        if action == "add" and len(parts) == 4:
            title = parts[1].strip()
            author = parts[2].strip()
            try:
                year = int(parts[3].strip())
            except ValueError:
                continue
            books.append({"title": title, "author": author, "year": year})

        elif action == "remove" and len(parts) == 2:
            title = parts[1].strip()
            books = [book for book in books if book["title"] != title]

        elif action == "list":
            sorted_books = sorted(books, key=lambda b: b["year"])
            for book in sorted_books:
                print(f"{book['title']} - {book['author']} - {book['year']}")


if __name__ == "__main__":
    main()
