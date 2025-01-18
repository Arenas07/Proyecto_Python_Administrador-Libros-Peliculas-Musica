import json

def seeBooks():
    with open("data/books.json", "r", encoding="utf-8") as file:
            return json.load(file)

def saveBooks(temporalBooks):
    existingBooks = seeBooks()
    existing_titles = {book["Titulo"] for book in existingBooks}
    books_to_add = [
        book for book in temporalBooks if book["Titulo"] not in existing_titles
    ]
    
    if books_to_add:
        existingBooks.extend(books_to_add)
        with open("data/books.json", "w", encoding="utf-8") as file:
            convertJson = json.dumps(existingBooks, indent=4, ensure_ascii=False)
            file.write(convertJson)
        print(f"Se han agregado {len(books_to_add)} libros nuevos al archivo JSON.")
    else:
        print("No se encontraron libros nuevos para agregar.")
    temporalBooks.clear()


