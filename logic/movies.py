import json

def seeMovies():
    with open("data/movies.json", "r", encoding="utf-8") as file:
            return json.load(file)

def saveMovie(temporalMovies):
    existingMovies = seeMovies()
    existing_titles = {movie["Titulo"] for movie in existingMovies}
    movies_to_add = [
        movie for movie in temporalMovies if movie["Titulo"] not in existing_titles
    ]
    
    if movies_to_add:
        existingMovies.extend(movies_to_add)
        with open("data/movies.json", "w", encoding="utf-8") as file:
            convertJson = json.dumps(existingMovies, indent=4, ensure_ascii=False)
            file.write(convertJson)
        print(f"Se han agregado {len(movies_to_add)} libros nuevos al archivo JSON.")
    else:
        print("No se encontraron libros nuevos para agregar.")
    temporalMovies.clear()