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

def editTitleJSONmovies(temporalmovies):
    jsondata = seeMovies()  
    for temporalmovie in temporalmovies:
        for lookcode in jsondata:
            if lookcode["ID"] == temporalmovie["ID"]: 
                if lookcode["Titulo"] != temporalmovie["Titulo"]: 
                    lookcode["Titulo"] = temporalmovie["Titulo"] 
                    with open("data/books.json", "w", encoding="utf-8") as file:
                        convertJson = json.dumps(jsondata, indent=4, ensure_ascii=False)  
                        file.write(convertJson) 
                    print(f"Se ha actualizado el título de la pelicula")
                    break 

def editMoviesTitle(movie_id, new_title): 
    from design.movies import temporalMovies
    for movie in temporalMovies:
        if movie["ID"] == movie_id:
            movie["Titulo"] = new_title  
            print("Se ha actualizado el título en la lista temporal")
            break

