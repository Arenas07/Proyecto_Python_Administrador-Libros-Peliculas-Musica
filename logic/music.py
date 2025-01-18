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