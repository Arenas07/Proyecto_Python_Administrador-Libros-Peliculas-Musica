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
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    input("Presione enter para continuar -->  ")
