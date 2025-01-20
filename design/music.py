from tabulate import tabulate
from logic.music import seeMusic

temporalSongs = []
def view_temporal_songs():
    if not temporalSongs:
        print("No hay canciones registradas")
    else:
        table = [
            [
                song["ID"],
                song["Titulo"],
                song["Autor"],
                song["Album"],
                ", ".join(song["Genero"]),
                song["Categoria"],
                song["Discografica"]
            ]
            for song in temporalSongs
        ]
        headers = ["Título", "Autor", "Album", "Genero", "Categoria", "Discografia"]
        print("\n=== Canciones Temporales Registradas ===")
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def loadJSONSongs():
    load = seeMusic()
    existing_titles = set()  
    songs_to_add = [] 
    for song in temporalSongs:
        existing_titles.add(song["Titulo"])    

    for song in load:
        if song["Titulo"] not in existing_titles:
            songs_to_add.append(song)
    temporalSongs.extend(songs_to_add)

def newSong():  
    watch = seeMusic() 
    title = input("Ingrese el nombre de la cancion: ")
    findSongs = list(filter(lambda peli: peli.get("Titulo") == title, watch)) 
    findRepetition = list(filter(lambda peli: peli.get("Titulo") == title, temporalSongs))
    allIDS = []
    for code in watch:
        if "ID" in code:
            allIDS.append(code["ID"])
    lastId = allIDS[-1] if allIDS else "MS-0"
    if(not len(findSongs)) and (not len(findRepetition)): 
        newSong = {
                "ID": input(f"Ingrese el codigo del libro (ultimo codigo {lastId}, recomiendo sumarle 1 a ese): "),
                "Titulo": title,
                "Autor": input("Ingrese el autor de la cancion: "),
                "Album": input("Ingrese el album de la cancion: "),
                "Genero": [],
                "Categoria": input("Ingrese la categoria de la cancion: "),
                "Discografica": input("Ingrese la discografica de la cancion: ")
            }
        while True:
            genero = input("Ingrese el genero de la cancion: ").capitalize()
            if genero:
                newSong["Genero"].append(genero)
            else:
                print("El genero no puede quedar vacio")
            confirmation = input("¿Quiere agregar otro genero? (s/n): ")
            if confirmation.lower() != "s":
                break
        temporalSongs.append(newSong)
        print("Cancion registrada con exito, si lo quiere guardar vaya al apartado de guardado")
        input("Presione enter para continuar -->")
    else: 
        print("La canción ya existe en su coleccion")

def filterMusicbyTitle(title): 
    data = temporalSongs
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Titulo") == title): 
            dataModify.append(diccionario) 
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró la cancion")
    input("Presione enter para continuar -->  ")

def showMusicTitles():
    if temporalSongs:
        data = temporalSongs
        dataModify = []
        filtro = set()
        for titles in data:
            title = titles.get("Titulo")
            if title and title not in filtro:
                filtro.add(title)
                music_copy = titles.copy()
                music_copy.pop("Autor", None)   
                music_copy.pop("Album", None)
                music_copy.pop("Discografica", None)
                music_copy.pop("Genero", None)
                music_copy.pop("Categoria", None)
                dataModify.append(music_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def filterMusicsbyAutor(autor): 
    data = temporalSongs
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Autor") == autor): 
            dataModify.append(diccionario) 
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro")
    input("Presione enter para continuar -->  ")

def showMusicAutor():
    if temporalSongs:
        data = temporalSongs
        dataModify = []
        filtro = set()
        for titles in data:
            title = titles.get("Autor")
            if title and title not in filtro:
                filtro.add(title)
                music_copy = titles.copy()
                music_copy.pop("Titulo", None)   
                music_copy.pop("Album", None)
                music_copy.pop("Discografica", None)
                music_copy.pop("Genero", None)
                music_copy.pop("Categoria", None)
                dataModify.append(music_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def filterMusicbyCategory(category): 
    data = temporalSongs
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Categoria") == category): 
            dataModify.append(diccionario) 
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro")
    input("Presione enter para continuar -->  ")

def showMusicCategory():
    if temporalSongs:
        data = temporalSongs
        dataModify = []
        filtro = set()
        for titles in data:
            title = titles.get("Categoria")
            if title and title not in filtro:
                filtro.add(title)
                music_copy = titles.copy()
                music_copy.pop("Autor")   
                music_copy.pop("Album")
                music_copy.pop("Discografica")
                music_copy.pop("Genero")
                music_copy.pop("Titulo")
                dataModify.append(music_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def showMusicGenre():
    if temporalSongs:
        data = temporalSongs
        dataModify = []
        filtro = set()
        for titles in data:
            generos = titles.get("Genero")
            for genero in generos:
                if genero and genero not in filtro:
                    filtro.add(genero)
                    music_copy = titles.copy()
                    music_copy.pop("Autor")
                    music_copy.pop("Titulo")
                    music_copy.pop("Valoracion")
                    music_copy.pop("Categoria")
                    music_copy["Genero"] = genero
                    dataModify.append(music_copy)
        if dataModify:
            print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
        else:
            print("No se encontraron géneros registrados")
    else:
        print("No se encontraron títulos registrados")

def filterMusicbyGenre(genero): 
    data = temporalSongs
    dataModify = [] 
    for diccionario in data:
        if genero in diccionario.get("Genero"):
            dataModify.append(diccionario)
    
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro con ese género")
    
    input("Presione enter para continuar -->  ")