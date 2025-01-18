from tabulate import tabulate
from logic.books import seeBooks, saveBooks
temporalBooks = []

def newBook():  
    watch = seeBooks() 
    title = input("Ingrese el titulo del libro: ")
    findBooks = list(filter(lambda libro: libro.get("Titulo") == title, watch)) 
    findRepetition = list(filter(lambda repe: repe.get("Titulo") == title, temporalBooks))
    if(not len(findBooks)) and (not len(findRepetition)): 
        newBook = {
            "Titulo": title,
            "Autor": input("Ingrese el nombre del autor: "),
            "Valoracion": float(input("Ingrese la valoracion de la obra: ")),
            "Categoria": input("Ingrese la categoria del libro: "),
            "Genero": []
        }
        while True:
            genero = input("Ingrese el genero del libro: ").capitalize()
            if genero:
                newBook["Genero"].append(genero)
            else:
                print("El genero no puede quedar vacio")
            confirmation = input("¿Quiere agregar otro genero? (s/n): ")
            if confirmation.lower() != "s":
                break
        temporalBooks.append(newBook)
        print("Libro registrado con exito, si lo quiere guardar vaya al apartado de guardado")
        input("Presione enter para continuar -->")
    else: 
        print("El libro ya existe en su coleccion")

def view_temporal_books():
    if not temporalBooks:
        print("No hay libros registrados")
    else:
        table = [
            [
                book["Titulo"],
                book["Autor"],
                book["Valoracion"],
                book["Categoria"],
                ", ".join(book["Genero"]),
            ]
            for book in temporalBooks
        ]
        headers = ["Título", "Autor", "Valoración", "Categoría", "Géneros"]
        print("\n=== Libros Temporales Registrados ===")
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def loadJSONBooks():
    load = seeBooks()
    existing_titles = set()
    books_to_add = []
    for book in temporalBooks:
        existing_titles.add(book["Titulo"])    
 
    for book in load:
        if book["Titulo"] not in existing_titles:
            books_to_add.append(book)
    temporalBooks.extend(books_to_add)

