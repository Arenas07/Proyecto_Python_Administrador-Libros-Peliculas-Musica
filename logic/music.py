import json

def seeMusic():
    with open("data/music.json", "r", encoding="utf-8") as file:
            return json.load(file)
def updateJsonWhenSaveMusic():
    from design.music import temporalSongs
    list = temporalSongs
    with open("data/music.json", "w", encoding="utf-8") as file:
        convertJson = json.dumps(list, indent=4, ensure_ascii=False)
        file.write(convertJson)

def saveMusic(temporalSongs):
    existingSongs = seeMusic()
    existing_titles = set()
    for song in existingSongs:
        existing_titles.add(song["Titulo"])
    songs_to_add = []
    for song in temporalSongs:
        if song["Titulo"] not in existing_titles:
            songs_to_add.append(song)

    if songs_to_add:
        existingSongs.extend(songs_to_add)
        with open("data/music.json", "w", encoding="utf-8") as file:
            convertJson = json.dumps(existingSongs, indent=4, ensure_ascii=False)
            file.write(convertJson)
        print(f"Se han agregado {len(songs_to_add)} canciones nuevas al archivo JSON.")
    temporalSongs.clear()


def editMusicTitle(music_id, new_title): 
    from design.music import temporalSongs
    for song in temporalSongs:
        if song["ID"] == music_id:
            song["Titulo"] = new_title  
            print("Se ha actualizado el título en la lista temporal")
            break

def editMusicAutor(music_id, new_autor): 
    from design.music import temporalSongs
    for song in temporalSongs:
        if song["ID"] == music_id:
            song["Autor"] = new_autor 
            print("Se ha actualizado el autor en la lista temporal")
            break

def editMusicAlbum(music_id, album): 
    from design.music import temporalSongs
    for song in temporalSongs:
        if song["ID"] == music_id:
            song["Album"] = album 
            print("Se ha actualizado el album en la lista temporal")
            break

def editMusicGenre(music_id): 
    from design.music import temporalSongs

    for music in temporalSongs:
        if music["ID"] == music_id:
            new_genre = []
            while True:
                opcion = input("Ingrese el genero nuevo: ")
                new_genre.append(opcion)
                opc = input("Quiere agregar otro genero? (s/n): ")
                if opc.lower() != "s":
                    break
                if new_genre:
                    music["Genero"] = new_genre
                else:
                    print("No se han ingresado generos")

def editMusicCAT(music_id, cat): 
    from design.music import temporalSongs
    for song in temporalSongs:
        if song["ID"] == music_id:
            song["Categoria"] = cat 
            print("Se ha actualizado la categoria en la lista temporal")
            break

def editMusicDisc(music_id, disc): 
    from design.music import temporalSongs
    for song in temporalSongs:
        if song["ID"] == music_id:
            song["Discografica"] = disc
            print("Se ha actualizado la discografica en la lista temporal")
            break

def deleteTEMPORALSong(id): 
    from design.music import temporalSongs
    info = temporalSongs
    
    for code in info: 
        if id == code.get("ID"): 
            security = input("¿Está seguro de eliminar la cancion? (s/n): ".strip())
            if security.lower() == "s":  
                info.remove(code)  
                print("Cancion eliminada correctamente")
                break
            else:
                input("Operación cancelada, presione enter para continuar: ")
                break
    input("Presione enter para continuar -->")  

def deleteTEMPORALSongbyName(title): 
    from design.music import temporalSongs
    info = temporalSongs
    
    for code in info: 
        if title == code.get("Titulo"): 
            security = input("¿Está seguro de eliminar la cancion? (s/n): ".strip())
            if security.lower() == "s":  
                info.remove(code)  
                print("Cancion eliminada correctamente")
                break
            else:
                input("Operación cancelada, presione enter para continuar: ")
                break
    input("Presione enter para continuar -->")  