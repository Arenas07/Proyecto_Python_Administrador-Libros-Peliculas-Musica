from tabulate import tabulate
from logic.books import seeBooks, saveBooks

def seeAllBooksInTables():
    watch = seeBooks()  
    print(tabulate(watch, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    input("--> Presione enter para continuar")

def newBook(): 
    watch = seeBooks() 
    title = input("Ingrese el titulo del libro: ")
    findProducts = list(filter(lambda product: product.get("Titulo") == title, watch)) #Filtro para comparar si el dato ingresado existe
    if(not len(findProducts)): 
        newBook = {
            "Titulo": title,
            "Autor": input("Ingrese el nombre del autor: "),
            "Valoracion": int(input("Ingrese la valoracion de la obra: ")),
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
            if confirmation.lower != "s":
                 break
        watch.append(newBook)
        saveBooks(watch)
        print("Libro registrado con exito")
    else: 
        print("El libro ya existe en su coleccion")

def filterBooksbyTitle(title): 
    data = seeBooks() 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Titulo") == title): 
            dataModify.append(diccionario) 
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    input("Presione enter para continuar -->  ")

def filterBooksbyAutor(autor): 
    data = seeBooks() 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Autor") == autor): 
            dataModify.append(diccionario) 
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    input("Presione enter para continuar -->  ")

def filterBooksbyCategory(category): 
    data = seeBooks() 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Categoria") == category): 
            dataModify.append(diccionario) 
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    input("Presione enter para continuar -->  ")