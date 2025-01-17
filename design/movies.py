from tabulate import tabulate
from logic.movies import seeMovies

def seeAllMoviesInTables():
    watch = seeMovies()  
    print(tabulate(watch, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    input("--> Presione enter para continuar")
    
def filterMoviesbyTitle(title): 
    data = seeMovies() 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Titulo") == title): 
            dataModify.append(diccionario) 
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    input("Presione enter para continuar -->  ")

def filterMoviesByDirector(director): 
    data = seeMovies() 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Direccion") == director): 
            dataModify.append(diccionario) 
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    input("Presione enter para continuar -->  ")

def filterMoviesbyCategory(category): 
    data = seeMovies() 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Categoria") == category): 
            dataModify.append(diccionario) 
    if not dataModify:
        print("No se encontró la categoria")
    else:
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    input("Presione enter para continuar -->  ")

def showMoviesCategory():
    data = seeMovies()
    dataModify = []
    filtro = set()
    for categorias in data:
        categoria = categorias.get("Categoria")
        if categoria and categoria not in filtro:
            filtro.add(categoria)
            categorias.pop("Titulo")
            categorias.pop("Direccion")
            categorias.pop("Producción")
            categorias.pop("Genero")
            categorias.pop("Valoracion")
            categorias.pop("Fecha de estreno")
            dataModify.append(categorias)
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))