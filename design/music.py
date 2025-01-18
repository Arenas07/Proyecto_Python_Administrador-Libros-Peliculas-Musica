from tabulate import tabulate
from logic.music import seeMusic

temporalSongs = []
def view_temporal_songs():
    if not temporalSongs:
        print("No hay canciones registradas")
    else:
        table = [
            [
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
    if(not len(findSongs)) and (not len(findRepetition)): 
        newSong = {
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