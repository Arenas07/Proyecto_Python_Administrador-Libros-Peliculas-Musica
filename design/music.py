from tabulate import tabulate
from logic.music import seeMusic

temporalSongs = []
def view_temporal_songs(): #Ver canciones en archivo temporal
    if not temporalSongs: #Si la lista temporal esta vacia
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
            for song in temporalSongs #Recorre la lista y le asignamos el valor a las llaves
        ]
        headers = ["Título", "Autor", "Album", "Genero", "Categoria", "Discografia"]
        print("\n=== Canciones Temporales Registradas ===")
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def loadJSONSongs(): #Cargar archivos a la lista temporal
    load = seeMusic() #Ver libros json
    existing_titles = set()  
    songs_to_add = [] 
    for song in temporalSongs: #Recorre todos los libros ya guardados y los pone en un set para evitar repeticion
        existing_titles.add(song["Titulo"])    

    for song in load: #Si el titulo es diferente lo mete a la lista temporal
        if song["Titulo"] not in existing_titles:
            songs_to_add.append(song)
    temporalSongs.extend(songs_to_add) #Extend para agregar más de uno

def newSong():  #Formulario nueva cancion
    watch = seeMusic() #Toma la información actual del JSON
    title = input("Ingrese el nombre de la cancion: ")
    findSongs = list(filter(lambda peli: peli.get("Titulo") == title, watch)) #Filtro para saber todos los titulos 
    findRepetition = list(filter(lambda peli: peli.get("Titulo") == title, temporalSongs)) #Filtro para saber los titulos temporales
    allIDS = []
    for code in watch:
        if "ID" in code:
            allIDS.append(code["ID"])
            #Pone todos los codigos en la lista allIDS
    lastId = allIDS[-1] if allIDS else "MS-0"
    #Revisa el ultimo codigo registrado en la lista
    id = input(f"Ingrese el ID de la canción (ultimo codigo: {lastId}): ")
    findid = list(filter(lambda peli: peli.get("ID") == id.strip(), watch))  #Filtro buscar IDS
    findRepetitionid = list(filter(lambda repe: repe.get("ID") == id.strip(), temporalSongs)) #Buscar ids en la lista temporal
    if(not len(findSongs)) and (not len(findRepetition)) and (not len(findid) and (not len(findRepetitionid))):
        #Si no hay repeticion prosiga con el formulario
        newSong = {
                "ID": id,
                "Titulo": title,
                "Autor": input("Ingrese el autor de la cancion: "),
                "Album": input("Ingrese el album de la cancion: "),
                "Genero": [],
                "Categoria": input("Ingrese la categoria de la cancion: "),
                "Discografica": input("Ingrese la discografica de la cancion: ")
            }
        while True: #Ciclo para agregar mas de un genero al libro
            genero = input("Ingrese el genero de la cancion: ").capitalize()
            if genero:
                newSong["Genero"].append(genero)
            else:
                print("El genero no puede quedar vacio")
            confirmation = input("¿Quiere agregar otro genero? (s/n): ")
            if confirmation.lower() != "s":
                break
        temporalSongs.append(newSong) #Toda la info la guarda como nuevo libro en la lista temporal
        print("Cancion registrada con exito, si lo quiere guardar vaya al apartado de guardado")
        input("Presione enter para continuar -->")
    else: 
        print("La canción ya existe en su coleccion")

def filterMusicbyTitle(title): #Ver canciones por titulo
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

def showMusicTitles(): #Ver titulos de canciones
    if temporalSongs: #Si la lista temporal esta vacia
        data = temporalSongs 
        dataModify = []
        filtro = set()
        for titles in data: #Recorre todo
            title = titles.get("Titulo")  #Title almacena todos los autores registrados
            if title and title not in filtro: #Si existen autores y no se encuentra repetido
                filtro.add(title) #Añade el titulo al filtro para que no se repita
                music_copy = titles.copy()  #saco una copia para no modificar la lista original
                music_copy.pop("Autor")   
                music_copy.pop("Album")
                music_copy.pop("Discografica") #borro toda la info que no es necesaria
                music_copy.pop("Genero")
                music_copy.pop("Categoria")
                dataModify.append(music_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def filterMusicsbyAutor(autor): #Ver canciones por autor
    data = temporalSongs
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Autor") == autor): #Si el autor dado es el mismo al autor de la lista
            dataModify.append(diccionario) #Tabula toda la información
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el autor")
    input("Presione enter para continuar -->  ")

def showMusicAutor(): #Ver autores de cancion
    if temporalSongs: #Si la lista temporal esta vacia
        data = temporalSongs
        dataModify = []
        filtro = set()
        for titles in data:
            title = titles.get("Autor") #Title almacena todos los autores registrados
            if title and title not in filtro: #Si existen autores y no se encuentra repetido
                filtro.add(title) #Añade el titulo al filtro para que no se repita
                music_copy = titles.copy() #saco una copia para no modificar la lista original
                music_copy.pop("Titulo")   
                music_copy.pop("Album")
                music_copy.pop("Discografica") #borro toda la info que no es necesaria
                music_copy.pop("Genero")
                music_copy.pop("Categoria")
                dataModify.append(music_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def filterMusicbyCategory(category):  #Ver canciones por categoria
    data = temporalSongs
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Categoria") == category):  #Si la categoria dado es el mismo a la categoria de la lista
            dataModify.append(diccionario) #Tabula toda la información
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró la cancion")
    input("Presione enter para continuar -->  ")

def showMusicCategory(): #Ver categoria de canciones
    if temporalSongs: #Si la lista temporal esta vacia
        data = temporalSongs
        dataModify = []
        filtro = set()
        for titles in data:
            title = titles.get("Categoria") #Title almacena todos los autores registrados
            if title and title not in filtro: #Si existen autores y no se encuentra repetido
                filtro.add(title) #Añade el titulo al filtro para que no se repita
                music_copy = titles.copy()  #saco una copia para no modificar la lista original
                music_copy.pop("Autor")   
                music_copy.pop("Album")
                music_copy.pop("Discografica")
                music_copy.pop("Genero")
                music_copy.pop("Titulo")
                dataModify.append(music_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def showMusicGenre(): #Ver generos de canciones
    if temporalSongs:
        data = temporalSongs
        dataModify = []
        filtro = set()
        for titles in data:
            generos = titles.get("Genero")  #Title almacena todos los autores registrados
            for genero in generos:
                if genero and genero not in filtro: #Si existen autores y no se encuentra repetido
                    filtro.add(genero) #Añade el titulo al filtro para que no se repita
                    music_copy = titles.copy() #saco una copia para no modificar la lista original
                    music_copy.pop("Autor")
                    music_copy.pop("Album")
                    music_copy.pop("Discografica")
                    music_copy.pop("Titulo")
                    music_copy.pop("Categoria")
                    music_copy["Genero"] = genero
                    dataModify.append(music_copy)
        if dataModify:
            print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
        else:
            print("No se encontraron géneros registrados")
    else:
        print("No se encontraron títulos registrados")

def filterMusicbyGenre(genero):  #Ver canciones por genero
    data = temporalSongs
    dataModify = [] 
    for diccionario in data:
        if genero in diccionario.get("Genero"): #Se usa el in debido a que puede haber más de un genero
            dataModify.append(diccionario) #Se pone toda la informacion en la lista
    
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró la cancion con ese género")
    
    input("Presione enter para continuar -->  ")