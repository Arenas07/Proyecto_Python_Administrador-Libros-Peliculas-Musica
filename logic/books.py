import json

from tabulate import tabulate
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

def editBooks(book_name): 
    from design.books import temporalBooks
    if temporalBooks:
        books = temporalBooks
        for iterate in books: 
            if iterate.get("Titulo") == book_name:   
                print(f"Detalles actuales del pedido {book_name}:\n")
                print(tabulate(iterate, headers="keys", tablefmt="fancy_grid"))

                book_detail = {
                    "Titulo": input("Escriba el nombre del titulo (si está mal escrito) sino vuelva a escribir el titulo: ").capitalize(),
                    "Autor": input("Escriba el nombre del autor: ").capitalize(),
                    "Genero": [],
                    "Categoria": input("Escriba la categoria nueva: ").capitalize()
                }
            while True:
                genero = input("Ingrese el genero del libro: ").capitalize()
                if genero:
                    book_detail["Genero"].append(genero)
                else:
                    print("El genero no puede quedar vacio")
                confirmation = input("¿Quiere agregar otro genero? (s/n): ")
                if confirmation.lower() != "s":
                    break
                    

                iterate.update(book_detail)
                print(f"El libro '{book_name}' ha sido actualizado.")
                break
        else:
            print(f"No se encontró el libro con el título '{book_name}'.")
    else:
        print("No hay libros temporales para editar.")


            

