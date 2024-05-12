def add_book(library, title, author):
    new_book = (title, author)
    if new_book not in library:
        library.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")
    else:
        print(f"Book '{title}' by {author} is already in the library.")


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


add_book(library, "The Great Gatsby", "Scott Fitzgerald")
add_book(library, "1984", "George Orwell")

print("Updated Library:")
print(library)