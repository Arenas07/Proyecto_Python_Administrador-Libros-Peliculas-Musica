import json

def seeBooks():
    with open("data/books.json", "r", encoding="utf-8") as file:
            return json.load(file)
    
def updateJsonWhenSave():
    from design.books import temporalBooks
    list = temporalBooks
    with open("data/books.json", "w", encoding="utf-8") as file:
        convertJson = json.dumps(list, indent=4, ensure_ascii=False)
        file.write(convertJson)

def saveBooks(temporalBooks):

    existingBooks = seeBooks()
    existing_titles = set()
    for book in existingBooks:
        existing_titles.add(book["Titulo"])

    books_to_add = []
    for book in temporalBooks:
        if book["Titulo"] not in existing_titles:
            books_to_add.append(book)

    
    if books_to_add:
        existingBooks.extend(books_to_add)
        with open("data/books.json", "w", encoding="utf-8") as file:
            convertJson = json.dumps(existingBooks, indent=4, ensure_ascii=False)
            file.write(convertJson)
        print(f"Se han agregado {len(books_to_add)} libros nuevos al archivo JSON.")
    else:
        print("No se encontraron libros nuevos para agregar.")
    temporalBooks.clear()

def editTitleJSON(temporalbooks):
    jsondata = seeBooks()  
    for temporalbook in temporalbooks:
        for lookcode in jsondata:
            if lookcode["ID"] == temporalbook["ID"]: 
                if lookcode["Titulo"] != temporalbook["Titulo"]: 
                    lookcode["Titulo"] = temporalbook["Titulo"] 
                    with open("data/books.json", "w", encoding="utf-8") as file:
                        convertJson = json.dumps(jsondata, indent=4, ensure_ascii=False)  
                        file.write(convertJson) 
                    print(f"Se ha actualizado el título del libro ")
                    break  

def editAutorJSON(temporalbooks):
    jsondata = seeBooks()  
    for temporalbook in temporalbooks:
        for lookcode in jsondata:
            if lookcode["ID"] == temporalbook["ID"]: 
                if lookcode["Autor"] != temporalbook["Autor"]: 
                    lookcode["Autor"] = temporalbook["Autor"] 
                    with open("data/books.json", "w", encoding="utf-8") as file:
                        convertJson = json.dumps(jsondata, indent=4, ensure_ascii=False)  
                        file.write(convertJson) 
                    print(f"Se ha actualizado el autor del libro")
                    break  

def editGenreJSON(temporalbooks):
    jsondata = seeBooks()  
    for temporalbook in temporalbooks:
        for lookcode in jsondata:
            if lookcode["ID"] == temporalbook["ID"]: 
                if lookcode["Genero"] != temporalbook["Genero"]: 
                    lookcode["Genero"] = temporalbook["Genero"] 
                    with open("data/books.json", "w", encoding="utf-8") as file:
                        convertJson = json.dumps(jsondata, indent=4, ensure_ascii=False)  
                        file.write(convertJson) 
                    print(f"Se ha actualizado el genero del libro")
                    break  

def editRateJSON(temporalbooks):
    jsondata = seeBooks()  
    for temporalbook in temporalbooks:
        for lookcode in jsondata:
            if lookcode["ID"] == temporalbook["ID"]: 
                if lookcode["Valoracion"] != temporalbook["Valoracion"]: 
                    lookcode["Valoracion"] = temporalbook["Valoracion"] 
                    with open("data/books.json", "w", encoding="utf-8") as file:
                        convertJson = json.dumps(jsondata, indent=4, ensure_ascii=False)  
                        file.write(convertJson) 
                    print(f"Se ha actualizado el título del libro")
                    break 

def editCategoryJSON(temporalbooks):
    jsondata = seeBooks()  
    for temporalbook in temporalbooks:
        for lookcode in jsondata:
            if lookcode["ID"] == temporalbook["ID"]: 
                if lookcode["Categoria"] != temporalbook["Categoria"]: 
                    lookcode["Categoria"] = temporalbook["Categoria"] 
                    with open("data/books.json", "w", encoding="utf-8") as file:
                        convertJson = json.dumps(jsondata, indent=4, ensure_ascii=False)  
                        file.write(convertJson) 
                    print(f"Se ha actualizado el título del libro con ID: {temporalbook['ID']}")
                    break   

def editBooksTitle(book_id, new_book): 
    from design.books import temporalBooks
    for book in temporalBooks:
        if book["ID"] == book_id:
            book["Titulo"] = new_book  
            print("Se ha actualizado el título en la lista temporal ")
            break

def editBooksAutor(book_id, new_autor): 
    from design.books import temporalBooks
    for book in temporalBooks:
        if book["ID"] == book_id:
            book["Autor"] = new_autor  
            print("Se ha actualizado el autor en la lista temporal ")
            break

def editBooksGenre(book_id): 
    from design.books import temporalBooks

    for book in temporalBooks:
        if book["ID"] == book_id:
            new_genre = []
            while True:
                opcion = input("Ingrese el genero nuevo: ")
                new_genre.append(opcion)
                opc = input("Quiere agregar otro genero? (s/n): ")
                if opc.lower() != "s":
                    break
                if new_genre:
                    book["Genero"] = new_genre
                else:
                    print("No se han ingresado generos")

def editBooksRate(book_id, newRate): 
    from design.books import temporalBooks

    for book in temporalBooks:
        if book["ID"] == book_id:
            book["Valoracion"] = newRate
            print("Se ha actualizado la valoracion en la lista temporal ")
            break

def editBooksCAT(book_id, newCAT): 
    from design.books import temporalBooks

    for book in temporalBooks:
        if book["ID"] == book_id:
            book["Categoria"] = newCAT
            print("Se ha actualizado la categoria en la lista temporal ")
            break

def deleteTEMPORAL(id): 
    from design.books import temporalBooks
    info = temporalBooks
    
    for code in info: 
        if id == code.get("ID"): 
            security = input("¿Está seguro de eliminar el libro? (s/n): ".strip())
            if security.lower() == "s":  
                info.remove(code)  
                print("Libro eliminado correctamente")
                break
            else:
                input("Operación cancelada, presione enter para continuar: ")
                break
    print("No se encontró el codigo")
    input("Presione enter para continuar -->")  

def deleteTEMPORALBookByName(title): 
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
    print("No se encontró el titulo")
    input("Presione enter para continuar -->")      

