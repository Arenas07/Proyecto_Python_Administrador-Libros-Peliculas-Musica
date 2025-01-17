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

def showMoviesTitles():
    data = seeMovies()
    dataModify = []
    filtro = set()
    for titles in data:
        title = titles.get("Titulo")
        if title and title not in filtro:
            filtro.add(title)
            titles.pop("Categoria")
            titles.pop("Direccion")
            titles.pop("Producción")
            titles.pop("Genero")
            titles.pop("Valoracion")
            titles.pop("Fecha de estreno")
            dataModify.append(titles)
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))

def showMoviesDirector():
    data = seeMovies()
    dataModify = []
    filtro = set()
    for directors in data:
        director = directors.get("Direccion")
        if director and director not in filtro:
            filtro.add(director)
            directors.pop("Categoria")
            directors.pop("Titulo")
            directors.pop("Producción")
            directors.pop("Genero")
            directors.pop("Valoracion")
            directors.pop("Fecha de estreno")
            dataModify.append(directors)
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))