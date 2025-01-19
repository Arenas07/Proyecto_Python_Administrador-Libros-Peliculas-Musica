import json

def seeMusic():
    with open("data/music.json", "r", encoding="utf-8") as file:
            return json.load(file)

def saveMusic(temporalSongs):
    existingSongs = seeMusic()
    existing_titles = {song["Titulo"] for song in existingSongs}
    songs_to_add = [
        movie for movie in temporalSongs if movie["Titulo"] not in existing_titles
    ]
    
    if songs_to_add:
        existingSongs.extend(songs_to_add)
        with open("data/music.json", "w", encoding="utf-8") as file:
            convertJson = json.dumps(existingSongs, indent=4, ensure_ascii=False)
            file.write(convertJson)
        print(f"Se han agregado {len(songs_to_add)} canciones nuevas al archivo JSON.")
    else:
        print("No se encontraron canciones nuevas para agregar.")
    temporalSongs.clear()

def editTitleJSONmusic(temporalsongs):
    jsondata = seeMusic()  
    for temporalsong in temporalsongs:
        for lookcode in jsondata:
            if lookcode["ID"] == temporalsong["ID"]: 
                if lookcode["Titulo"] != temporalsong["Titulo"]: 
                    lookcode["Titulo"] = temporalsong["Titulo"] 
                    with open("data/books.json", "w", encoding="utf-8") as file:
                        convertJson = json.dumps(jsondata, indent=4, ensure_ascii=False)  
                        file.write(convertJson) 
                    print(f"Se ha actualizado el título de la cancion")
                    break 

def editMusicTitle(music_id, new_title): 
    from design.music import temporalSongs
    for song in temporalSongs:
        if song["ID"] == music_id:
            song["Titulo"] = new_title  
            print("Se ha actualizado el título en la lista temporal")
            break