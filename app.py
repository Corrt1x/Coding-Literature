import json

with open('books.json', 'r') as file_handle:
    favorite_books = json.load(file_handle)

print("---Book List---")
print("A collection of useful books.")
print()

for title, description in favorite_books.items():
    print(f"{title}: {description}\n")
