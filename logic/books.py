import json

def seeBooks():  #Ver libros json
    with open("data/books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    
def updateJsonWhenSave(): #Actualizar archivo json
    from design.books import temporalBooks
    if temporalBooks:
        with open("data/books.json", "w", encoding="utf-8") as file:
            convertJson = json.dumps(temporalBooks, indent=4, ensure_ascii=False)
            file.write(convertJson)
    temporalBooks.clear()

def editBooksTitle(book_id, new_book): #Actualizar titulo libro
    from design.books import temporalBooks
    for book in temporalBooks:
        if book["ID"] == book_id.strip():
            book["Titulo"] = new_book  
            print("Se ha actualizado el título en la lista temporal ")
            break
        
def editBooksAutor(book_id, new_autor): #Actualizar autor libro
    from design.books import temporalBooks
    for book in temporalBooks:
        if book["ID"] == book_id.strip():
            book["Autor"] = new_autor  
            print("Se ha actualizado el autor en la lista temporal ")
            break

def editBooksGenre(book_id): #Actualizar genero libro
    from design.books import temporalBooks

    for book in temporalBooks:
        if book["ID"] == book_id.strip():
            new_genre = []
            while True:
                opcion = input("Ingrese el genero nuevo: ")
                new_genre.append(opcion)
                opc = input("Quiere agregar otro genero? (s/n): ").strip()
                if opc.lower() != "s":
                    break
                if new_genre:
                    book["Genero"] = new_genre
                else:
                    print("No se han ingresado generos")

def editBooksRate(book_id, newRate): #Actualizar valoracion libro
    from design.books import temporalBooks

    for book in temporalBooks:
        if book["ID"] == book_id.strip():
            book["Valoracion"] = newRate
            print("Se ha actualizado la valoracion en la lista temporal ")
            break

def editBooksCAT(book_id, newCAT): #Actualizar categoria libro
    from design.books import temporalBooks

    for book in temporalBooks:
        if book["ID"] == book_id.strip():
            book["Categoria"] = newCAT
            print("Se ha actualizado la categoria en la lista temporal ")
            break

def deleteTEMPORAL(id): #Borrar libro
    from design.books import temporalBooks
    info = temporalBooks
    
    for code in info: 
        if id.strip() == code.get("ID"): 
            security = input("¿Está seguro de eliminar el libro? (s/n): ".strip())
            if security.lower() == "s":  
                info.remove(code)  
                print("Libro eliminado correctamente")
                break
            else:
                input("Operación cancelada, presione enter para continuar: ")
                break
    input("Presione enter para continuar -->")  

def deleteTEMPORALBookByName(title): #Borrar libro por titulo
    from design.books import temporalBooks
    info = temporalBooks
    
    for code in info: 
        
        if title == code.get("Titulo"): 
            security = input("¿Está seguro de eliminar el libro? (s/n): ".strip())
            if security.lower() == "s":  
                info.remove(code)  
                print("Libro eliminado correctamente")
                break
            else:
                input("Operación cancelada, presione enter para continuar: ")
                break
    input("Presione enter para continuar -->")      

