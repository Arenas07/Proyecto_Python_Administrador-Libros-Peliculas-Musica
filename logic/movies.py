import json

def seeMovies():
    with open("data/movies.json", "r", encoding="utf-8") as file:
            return json.load(file)

def saveMovie(temporalMovies):
    existingMovies = seeMovies()
    existing_titles = set()
    for movie in existingMovies:
        existing_titles.add(movie["Titulo"])
    movies_to_add = []
    for movie in temporalMovies: 
        if movie["Titulo"] not in existing_titles:
            movies_to_add.append(movie)        
    
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

def editMovieDirection(movie_id, direction): 
    from design.movies import temporalMovies
    for movie in temporalMovies:
        if movie["ID"] == movie_id:
            movie["Direccion"] = direction  

            print("Se ha actualizado el director en la lista temporal")
            break

def editMovieGenre(movie_id): 
    from design.movies import temporalMovies

    for movie in temporalMovies:
        if movie["ID"] == movie_id:
            new_genre = []
            while True:
                opcion = input("Ingrese el genero nuevo: ")
                new_genre.append(opcion)
                opc = input("Quiere agregar otro genero? (s/n): ")
                if opc.lower() != "s":
                    break
                if new_genre:
                    movie["Genero"] = new_genre
                else:
                    print("No se han ingresado generos")

def editMovieProduction(movie_id, production): 
    from design.movies import temporalMovies
    for movie in temporalMovies:
        if movie["ID"] == movie_id:
            movie["Producción"] = production  

            print("Se ha actualizado la producción en la lista temporal")
            break

def editMovieRate(movie_id, rate): 
    from design.movies import temporalMovies
    for movie in temporalMovies:
        if movie["ID"] == movie_id:
            movie["Valoracion"] = rate  
            print("Se ha actualizado la valoracion en la lista temporal")
            break

def editMovieCAT(movie_id, CAT): 
    from design.movies import temporalMovies
    for movie in temporalMovies:
        if movie["ID"] == movie_id:
            movie["Categoria"] = CAT  
            print("Se ha actualizado la categoria en la lista temporal")
            break

def editDirectionJSONmovies(temporalmovies):
    jsondata = seeMovies()  
    for temporalmovie in temporalmovies:
        for lookcode in jsondata:
            if lookcode["ID"] == temporalmovie["ID"]: 
                if lookcode["Direccion"] != temporalmovie["Direccion"]: 
                    lookcode["Direccion"] = temporalmovie["Direccion"] 
                    with open("data/books.json", "w", encoding="utf-8") as file:
                        convertJson = json.dumps(jsondata, indent=4, ensure_ascii=False)  
                        file.write(convertJson) 
                    print(f"Se ha actualizado el título de la pelicula")
                    break 

def editProductionJSONmovies(temporalmovies):
    jsondata = seeMovies()  
    for temporalmovie in temporalmovies:
        for lookcode in jsondata:
            if lookcode["ID"] == temporalmovie["ID"]: 
                if lookcode["Producción"] != temporalmovie["Producción"]: 
                    lookcode["Producción"] = temporalmovie["Producción"] 
                    with open("data/books.json", "w", encoding="utf-8") as file:
                        convertJson = json.dumps(jsondata, indent=4, ensure_ascii=False)  
                        file.write(convertJson) 
                    print(f"Se ha actualizado el título de la pelicula")
                    break 