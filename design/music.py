from tabulate import tabulate
from logic.music import seeMusic

def seeAllMusicInTables():
    watch = seeMusic()
    print(tabulate(watch, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    input("--> Presione enter para continuar")

def filterMusicbyTitle(title): 
    data = seeMusic() 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Titulo") == title): 
            dataModify.append(diccionario) 
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    input("Presione enter para continuar -->  ")

def filterMusicbyAutor(autor): 
    data = seeMusic() 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Autor") == autor): 
            dataModify.append(diccionario) 
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    input("Presione enter para continuar -->  ")

def filterMusicbyCategory(category): 
    data = seeMusic() 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Categoria") == category): 
            dataModify.append(diccionario) 
    if not dataModify:
        print("No se encontró la categoria")
    else:
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    input("Presione enter para continuar -->  ")

def showMusicCategory():
    data = seeMusic()
    dataModify = []
    filtro = set()
    for categorias in data:
        categoria = categorias.get("Categoria")
        if categoria and categoria not in filtro:
            filtro.add(categoria)
            categorias.pop("Titulo")
            categorias.pop("Autor")
            categorias.pop("Album")
            categorias.pop("Genero")
            categorias.pop("Discografica")
            dataModify.append(categorias)
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))

def showMusicAutor():
    data = seeMusic()
    dataModify = []
    filtro = set()
    for autors in data:
        autor = autors.get("Autor")
        if autor and autor not in filtro:
            filtro.add(autor)
            autors.pop("Titulo")
            autors.pop("Categoria")
            autors.pop("Album")
            autors.pop("Genero")
            autors.pop("Discografica")
            dataModify.append(autors)
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))

def showMusicTitle():
    data = seeMusic()
    dataModify = []
    filtro = set()
    for titles in data:
        title = titles.get("Titulo")
        if title and title not in filtro:
            filtro.add(title)
            titles.pop("Categoria")
            titles.pop("Autor")
            titles.pop("Album")
            titles.pop("Genero")
            titles.pop("Discografica")
            dataModify.append(titles)
    print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))