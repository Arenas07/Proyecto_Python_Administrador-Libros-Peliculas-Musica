from tabulate import tabulate
from logic.movies import seeMovies

def seeAllMoviesInTables():
    watch = seeMovies()
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
        input("Presione enter para continuar --> ")  #!ARREGLAR LA DESCRIPCION DE LAS TABLAS
        