# --------------------------------------------
# Simple Library Management System
# Uses list comprehensions, nested data, and validation
# --------------------------------------------

library = []  # List of dictionaries (nested data structure)


def add_book():
    print("\n Add a New Book")
    try:
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        year = input("Enter publication year: ").strip()

        # Data validation
        if not title or not author:
            raise ValueError("Title and author cannot be empty.")
        if not year.isdigit():
            raise ValueError("Year must be a number.")

        library.append({"title": title, "author": author, "year": int(year)})
        print(" Book added successfully!")
    except ValueError as e:
        print(" Error:", e)


def view_books():
    print("\n Library Books")
    if not library:
        print("No books found.")
        return

    for i, book in enumerate(library, start=1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']})")


def search_books():
    keyword = input("\n Enter a keyword to search: ").lower().strip()

    # Filtering using list comprehension
    results = [book for book in library
               if keyword in book["title"].lower() or keyword in book["author"].lower()]

    if results:
        print("\n Search Results:")
        for book in results:
            print(f"- {book['title']} by {book['author']} ({book['year']})")
    else:
        print(" No matching books found.")


def main():
    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            print(" Exiting Library System. Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
