from tabulate import tabulate
from logic.books import seeBooks
temporalBooks = []

def newBook(): #Formulario nuevo libro
    watch = seeBooks() #Toma la información actual del JSON
    title = input("Ingrese el titulo del libro: ")
    findBooks = list(filter(lambda libro: libro.get("Titulo") == title, watch)) #Filtro para saber todos los titulos 
    findRepetition = list(filter(lambda repe: repe.get("Titulo") == title, temporalBooks)) #Filtro para saber los titulos temporales
    allIDS = []
    for code in watch:
        if "ID" in code:
            allIDS.append(code["ID"])
            #Pone todos los codigos en la lista allIDS
    lastId = allIDS[-1] if allIDS else "LB-0"
    #Revisa el ultimo codigo registrado en la lista
    id = input(f"Ingrese el ID del libro (ultimo codigo: {lastId}): ")
    findid = list(filter(lambda libro: libro.get("ID") == id.strip(), watch)) #Filtro buscar IDS
    findRepetitionid = list(filter(lambda repe: repe.get("ID") == id.strip(), temporalBooks)) #Buscar ids en la lista temporal
    if(not len(findBooks)) and (not len(findRepetition)) and (not len(findid) and (not len(findRepetitionid))): 
        #Si no hay repeticion prosiga con el formulario
        newBook = {
            "ID": id,
            "Titulo": title,
            "Autor": input("Ingrese el nombre del autor: "),
            "Valoracion": (input("Ingrese la valoracion de la obra: ")),
            "Categoria": input("Ingrese la categoria del libro: "),
            "Genero": []
        }
        while True: #Ciclo para agregar mas de un genero al libro
            genero = input("Ingrese el genero del libro: ").capitalize()
            if genero:
                newBook["Genero"].append(genero)
            else:
                print("El genero no puede quedar vacio")
            confirmation = input("¿Quiere agregar otro genero? (s/n): ").strip()
            if confirmation.lower() != "s":
                break
        temporalBooks.append(newBook) #Toda la info la guarda como nuevo libro en la lista temporal
        print("Libro registrado con exito, si lo quiere guardar vaya al apartado de guardado")
        input("Presione enter para continuar --> ")
    else: 
        print("El libro o codigo ya existe en su coleccion") #Validacion
        input("Presione enter para continuar --> ")

def view_temporal_books(): #Vew libros en la lista temporal
    if not temporalBooks: #Si la lista temporal esta vacia
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
            for book in temporalBooks #Recorre la lista y le asignamos el valor a las llaves
        ]
        headers = ["ID", "Título", "Autor", "Valoración", "Categoría", "Géneros"] #Tabular
        print("\n=== Libros Temporales Registrados ===")
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def loadJSONBooks(): #Cargar libros del json a la lista temporal
    load = seeBooks() #Ver libros json
    existing_titles = set()  
    books_to_add = [] 
    for book in temporalBooks:  #Recorre todos los libros ya guardados y los pone en un set para evitar repeticion
        existing_titles.add(book["Titulo"])

    for book in load: #Si el titulo es diferente lo mete a la lista temporal
        if book["Titulo"] not in existing_titles:
            books_to_add.append(book)

    temporalBooks.extend(books_to_add) #Extend para agregar más de uno


def filterBooksbyTitle(title): #Ver libro por titulo
    data = temporalBooks #Tomamos todos los titulos
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Titulo") == title): #Si el titulo ingresado se encuentra entre los disponibles
            dataModify.append(diccionario) #Append para mostrar toda su informacion y despues tabular
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro")
    input("Presione enter para continuar -->  ")
def showBookTitles(): #Mostrar titulos de libro
    if temporalBooks:
        data = temporalBooks 
        dataModify = []
        filtro = set()
        for titles in data: #Recorre todos los libros
            title = titles.get("Titulo") #Title almacena todos los titulos registrados
            if title and title not in filtro: #Si existen titulos y no se encuentra repetido
                filtro.add(title) #Añade el titulo al filtro para que no se repita
                book_copy = titles.copy() #saco una copia para no modificar la lista original
                book_copy.pop("Categoria")   
                book_copy.pop("Autor")      #borro toda la info que no es necesaria
                book_copy.pop("Valoracion")
                book_copy.pop("Genero")
                dataModify.append(book_copy) 
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def showBookAutor(): #Mostrar autores libro
    if temporalBooks:
        data = temporalBooks
        dataModify = []
        filtro = set()
        for titles in data: #Recorre todos los libros
            title = titles.get("Autor") #Title almacena todos los autores registrados
            if title and title not in filtro: #Si existen autores y no se encuentra repetido
                filtro.add(title) #Añade el titulo al filtro para que no se repita
                book_copy = titles.copy() #saco una copia para no modificar la lista original
                book_copy.pop("Categoria")   
                book_copy.pop("Titulo") #borro toda la info que no es necesaria
                book_copy.pop("Valoracion")
                book_copy.pop("Genero")
                dataModify.append(book_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def filterBooksbyAutor(autor): #Ver libro por autor
    data = temporalBooks 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Autor") == autor): #Si el autor dado es el mismo al autor de la lista
            dataModify.append(diccionario)  #Tabula toda la información
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro")
    input("Presione enter para continuar -->  ")
    
def showBookCategory(): #Mostrar categorias libros
    if temporalBooks:
        data = temporalBooks
        dataModify = []
        filtro = set()
        for titles in data: #Recorre todos los libros
            title = titles.get("Categoria") #Title almacena todos las categorias registradas
            if title and title not in filtro: #Si existen autores y no se encuentra repetido
                filtro.add(title) #Añade el titulo al filtro para que no se repita
                book_copy = titles.copy() #saco una copia para no modificar la lista original
                book_copy.pop("Autor")   
                book_copy.pop("Titulo")
                book_copy.pop("Valoracion") #borro toda la info que no es necesaria
                book_copy.pop("Genero")
                dataModify.append(book_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def filterBooksbyCategory(category):  #Ver libro por categoria
    data = temporalBooks 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Categoria") == category): #Si la categoria dado es el mismo a la categoria de la lista
            dataModify.append(diccionario)  #Tabula toda la información
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro")
    input("Presione enter para continuar -->  ")

def showBookGenre(): #Ver generos del libro
    if temporalBooks:
        data = temporalBooks
        dataModify = []
        filtro = set()
        for titles in data: #Recorre todos los libros
            generos = titles.get("Genero") #Title almacena todos las categorias registradas
            for genero in generos: 
                if genero and genero not in filtro: #Si existen generos y no se encuentra repetidos
                    filtro.add(genero)#Añade el titulo al filtro para que no se repita
                    book_copy = titles.copy()
                    book_copy.pop("Autor")
                    book_copy.pop("Titulo")
                    book_copy.pop("Valoracion") #Elimina todo lo que no usamos
                    book_copy.pop("Categoria")
                    book_copy["Genero"] = genero
                    dataModify.append(book_copy)
        if dataModify:
            print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
        else:
            print("No se encontraron géneros registrados")
    else:
        print("No se encontraron títulos registrados")

def filterBooksbyGenre(genero): #Ver libros por genero
    data = temporalBooks
    dataModify = [] 
    for diccionario in data:
        if genero in diccionario.get("Genero"): #Se usa el in debido a que puede haber más de un genero
            dataModify.append(diccionario) #Se pone toda la informacion en la lista
    
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro con ese género")
    
    input("Presione enter para continuar -->  ")
