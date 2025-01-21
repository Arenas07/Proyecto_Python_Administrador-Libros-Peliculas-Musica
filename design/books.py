from tabulate import tabulate
from logic.books import seeBooks, saveBooks
temporalBooks = []

def newBook():  
    watch = seeBooks() 
    title = input("Ingrese el titulo del libro: ")
    findBooks = list(filter(lambda libro: libro.get("Titulo") == title, watch)) 
    findRepetition = list(filter(lambda repe: repe.get("Titulo") == title, temporalBooks))
    allIDS = []
    for code in watch:
        if "ID" in code:
            allIDS.append(code["ID"])
    lastId = allIDS[-1] if allIDS else "LB-0"
    id = input(f"Ingrese el ID del libro (ultimo codigo: {lastId}): ")
    findid = list(filter(lambda libro: libro.get("ID") == id, watch)) 
    findRepetitionid = list(filter(lambda repe: repe.get("ID") == id, temporalBooks))
    if(not len(findBooks)) and (not len(findRepetition)) and (not len(findid) and (not len(findRepetitionid))): 
        newBook = {
            "ID": id,
            "Titulo": title,
            "Autor": input("Ingrese el nombre del autor: "),
            "Valoracion": (input("Ingrese la valoracion de la obra: ")),
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
        input("Presione enter para continuar --> ")
    else: 
        print("El libro o codigo ya existe en su coleccion")
        input("Presione enter para continuar --> ")

def view_temporal_books():
    if not temporalBooks:
        print("No hay libros registrados")
    else:
        table = [
            [
                book["ID"],
                book["Titulo"],
                book["Autor"],
                book["Valoracion"],
                book["Categoria"],
                ", ".join(book["Genero"]),
            ]
            for book in temporalBooks
        ]
        headers = ["ID", "Título", "Autor", "Valoración", "Categoría", "Géneros"]
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


def filterBooksbyTitle(title): 
    data = temporalBooks 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Titulo") == title): 
            dataModify.append(diccionario) 
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro")
    input("Presione enter para continuar -->  ")
def showBookTitles():
    if temporalBooks:
        data = temporalBooks
        dataModify = []
        filtro = set()
        for titles in data:
            title = titles.get("Titulo")
            if title and title not in filtro:
                filtro.add(title)
                book_copy = titles.copy()
                book_copy.pop("Categoria")   
                book_copy.pop("Autor")
                book_copy.pop("Valoracion")
                book_copy.pop("Genero")
                dataModify.append(book_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def showBookAutor():
    if temporalBooks:
        data = temporalBooks
        dataModify = []
        filtro = set()
        for titles in data:
            title = titles.get("Autor")
            if title and title not in filtro:
                filtro.add(title)
                book_copy = titles.copy()
                book_copy.pop("Categoria")   
                book_copy.pop("Titulo")
                book_copy.pop("Valoracion")
                book_copy.pop("Genero")
                dataModify.append(book_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def filterBooksbyAutor(autor): 
    data = temporalBooks 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Autor") == autor): 
            dataModify.append(diccionario) 
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro")
    input("Presione enter para continuar -->  ")
    
def showBookCategory():
    if temporalBooks:
        data = temporalBooks
        dataModify = []
        filtro = set()
        for titles in data:
            title = titles.get("Categoria")
            if title and title not in filtro:
                filtro.add(title)
                book_copy = titles.copy()
                book_copy.pop("Autor")   
                book_copy.pop("Titulo")
                book_copy.pop("Valoracion")
                book_copy.pop("Genero")
                dataModify.append(book_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def filterBooksbyCategory(category): 
    data = temporalBooks 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Categoria") == category): 
            dataModify.append(diccionario) 
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro")
    input("Presione enter para continuar -->  ")

def showBookGenre():
    if temporalBooks:
        data = temporalBooks
        dataModify = []
        filtro = set()
        for titles in data:
            generos = titles.get("Genero")
            for genero in generos:
                if genero and genero not in filtro:
                    filtro.add(genero)
                    book_copy = titles.copy()
                    book_copy.pop("Autor")
                    book_copy.pop("Titulo")
                    book_copy.pop("Valoracion")
                    book_copy.pop("Categoria")
                    book_copy["Genero"] = genero
                    dataModify.append(book_copy)
        if dataModify:
            print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
        else:
            print("No se encontraron géneros registrados")
    else:
        print("No se encontraron títulos registrados")

def filterBooksbyGenre(genero): 
    data = temporalBooks
    dataModify = [] 
    for diccionario in data:
        if genero in diccionario.get("Genero"):
            dataModify.append(diccionario)
    
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro con ese género")
    
    input("Presione enter para continuar -->  ")
