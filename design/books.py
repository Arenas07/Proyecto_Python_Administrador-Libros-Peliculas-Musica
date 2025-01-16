from tabulate import tabulate
from logic.books import seeBooks, saveBooks

def seeAllBooksInTables():
    watch = seeBooks()
    watchModificated = []
    mostrar_sinopsis = input("¿Desea ver las sinopsis de los libros? (s/n): ")
    if mostrar_sinopsis.lower() == "s":
        print(tabulate(watch, headers="keys", tablefmt="pretty", numalign="center", showindex="always"))
        input("Presione enter para continuar -->")       
    else:
        for modify in watch:
            modify.pop("Descripcion")
            watchModificated.append(modify)
        print(tabulate(watchModificated, headers="keys", tablefmt="pretty", numalign="center", showindex="always"))
        input("Presione enter para continuar --> ")


def newBook(): 
    watch = seeBooks() 
    title = input("Ingrese el titulo del libro: ")
    findProducts = list(filter(lambda product: product.get("Titulo") == title, watch)) #Filtro para comparar si el dato ingresado existe
    if(not len(findProducts)): 
        newBook = {
            "Titulo": title,
            "Autor": input("Ingrese el nombre del autor: "),
            "Valoracion": input("Ingrese la valoracion de la obra (si no desea ponerla solo preicone enter): "),
            "Sinopsis": input("Ingrese la sinopsis del libro (si la copia y pega de internet presione Ctrl+Shift+V para pegar en consola): "),
            "Genero": [input("sadas")]
        }
    #     while True:
    #         newBook["Genero"].append({
    #             input("Ingrese el genero del libro: ")
    #         })
    #         saveBooks(watch)
    #         confirmation = "¿Quiere agregar otro genero? (s/n): "
    #         if confirmation.lower != "s":
    #             break 
        if newBook["Genero"]:
            watch.append(newBook)
            saveBooks(watch)
            print("Libro guardado correctamente")

    # else: 
    #     print("El libro ya existe en su coleccion")