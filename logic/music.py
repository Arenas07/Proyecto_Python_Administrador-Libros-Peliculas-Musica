import json

def seeMusic(): #Ver musica del json
    with open("data/music.json", "r", encoding="utf-8") as file:
            return json.load(file)
def updateJsonWhenSaveMusic(): #Guardar cambios en el json
    from design.music import temporalSongs
    list = temporalSongs
    with open("data/music.json", "w", encoding="utf-8") as file:
        convertJson = json.dumps(list, indent=4, ensure_ascii=False)
        file.write(convertJson)
    temporalSongs.clear()


def editMusicTitle(music_id, new_title): #Editar titulo que recibe id y nuevo nombre
    from design.music import temporalSongs
    for song in temporalSongs:
        if song["ID"] == music_id.strip(): #si el id existe
            song["Titulo"] = new_title   #actualiza el titulo
            print("Se ha actualizado el título en la lista temporal")
            break

def editMusicAutor(music_id, new_autor): #Editar autor que recibe id y nuevo nombre
    from design.music import temporalSongs
    for song in temporalSongs:
        if song["ID"] == music_id.strip(): #si el id existe
            song["Autor"] = new_autor  #actualiza el autor
            print("Se ha actualizado el autor en la lista temporal")
            break

def editMusicAlbum(music_id, album): #Editar album que recibe id y el nuevo nombre
    from design.music import temporalSongs
    for song in temporalSongs:
        if song["ID"] == music_id.strip(): #si el id existe
            song["Album"] = album  #actualiza el album
            print("Se ha actualizado el album en la lista temporal")
            break

def editMusicGenre(music_id): 
    from design.music import temporalSongs

    for music in temporalSongs:
        if music["ID"] == music_id.strip(): #si el id existe
            new_genre = []
            while True:
                opcion = input("Ingrese el genero nuevo: ")
                new_genre.append(opcion)
                opc = input("Quiere agregar otro genero? (s/n): ").strip()
                if opc.lower() != "s":
                    break
                if new_genre:
                    music["Genero"] = new_genre #actualiza el genero
                else:
                    print("No se han ingresado generos")

def editMusicCAT(music_id, cat): #Editar categoria que recibe id y nueva categoria
    from design.music import temporalSongs
    for song in temporalSongs:
        if song["ID"] == music_id.strip():#si el id existe
            song["Categoria"] = cat #actualiza la categoria
            print("Se ha actualizado la categoria en la lista temporal")
            break

def editMusicDisc(music_id, disc): #Editar discografia que recive id y el nuevo nombre
    from design.music import temporalSongs
    for song in temporalSongs:
        if song["ID"] == music_id.strip(): #si el id existe
            song["Discografica"] = disc #actualiza la discografica
            print("Se ha actualizado la discografica en la lista temporal")
            break

def deleteTEMPORALSong(id): #Borrar musica por id
    from design.music import temporalSongs
    info = temporalSongs
    
    for code in info: 
        if id == code.get("ID"):  #si el id existe
            security = input("¿Está seguro de eliminar la cancion? (s/n): ".strip())
            if security.lower() == "s":  
                info.remove(code)  
                print("Cancion eliminada correctamente")
                break
            else:
                input("Operación cancelada, presione enter para continuar: ")
                break
    input("Presione enter para continuar -->")  

def deleteTEMPORALSongbyName(title): #Borrar musica por el nombre
    from design.music import temporalSongs
    info = temporalSongs
    
    for code in info: 
        if title == code.get("Titulo"): #Si el titulo existe
            security = input("¿Está seguro de eliminar la cancion? (s/n): ".strip())
            if security.lower() == "s":  
                info.remove(code)  
                print("Cancion eliminada correctamente")
                break
            else:
                input("Operación cancelada, presione enter para continuar: ")
                break
    input("Presione enter para continuar -->")  