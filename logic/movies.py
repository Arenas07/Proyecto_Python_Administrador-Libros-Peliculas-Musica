import json

def seeMovies():
    with open("data/movies.json", "r", encoding="utf-8") as file:
            return json.load(file)
    
def updateJsonWhenSaveMovies():
    from design.movies import temporalMovies
    list = temporalMovies
    with open("data/movies.json", "w", encoding="utf-8") as file:
        convertJson = json.dumps(list, indent=4, ensure_ascii=False)
        file.write(convertJson)

    temporalMovies.clear()


def editMoviesTitle(movie_id, new_title): 
    from design.movies import temporalMovies
    for movie in temporalMovies:
        if movie["ID"] == movie_id.strip():
            movie["Titulo"] = new_title  
            print("Se ha actualizado el título en la lista temporal")
            break

def editMovieDirection(movie_id, direction): 
    from design.movies import temporalMovies
    for movie in temporalMovies:
        if movie["ID"] == movie_id.strip():
            movie["Direccion"] = direction  

            print("Se ha actualizado el director en la lista temporal")
            break

def editMovieGenre(movie_id): 
    from design.movies import temporalMovies

    for movie in temporalMovies:
        if movie["ID"] == movie_id.strip():
            new_genre = []
            while True:
                opcion = input("Ingrese el genero nuevo: ")
                new_genre.append(opcion)
                opc = input("Quiere agregar otro genero? (s/n): ").strip()
                if opc.lower() != "s":
                    break
                if new_genre:
                    movie["Genero"] = new_genre
                else:
                    print("No se han ingresado generos")

def editMovieProduction(movie_id, production): 
    from design.movies import temporalMovies
    for movie in temporalMovies:
        if movie["ID"] == movie_id.strip():
            movie["Producción"] = production  

            print("Se ha actualizado la producción en la lista temporal")
            break

def editMovieRate(movie_id, rate): 
    from design.movies import temporalMovies
    for movie in temporalMovies:
        if movie["ID"] == movie_id.strip():
            movie["Valoracion"] = rate  
            print("Se ha actualizado la valoracion en la lista temporal")
            break

def editMovieCAT(movie_id, CAT): 
    from design.movies import temporalMovies
    for movie in temporalMovies:
        if movie["ID"] == movie_id.strip(): 
            movie["Categoria"] = CAT  
            print("Se ha actualizado la categoria en la lista temporal")
            break

def deleteTEMPORALMovie(id): 
    from design.movies import temporalMovies
    info = temporalMovies
    
    for code in info: 
        if id.strip() == code.get("ID"): 
            security = input("¿Está seguro de eliminar la pelicula? (s/n): ".strip())
            if security.lower() == "s":  
                info.remove(code)  
                print("Pelicula eliminada correctamente")
                break
            else:
                input("Operación cancelada, presione enter para continuar: ")
                break
    input("Presione enter para continuar -->")     

def deleteTEMPORALMoviebyName(title): 
    from design.movies import temporalMovies
    info = temporalMovies
    
    for code in info: 
        if title == code.get("Titulo"): 
            security = input("¿Está seguro de eliminar la pelicula? (s/n): ".strip())
            if security.lower() == "s":  
                info.remove(code)  
                print("Pelicula eliminada correctamente")
                break
            else:
                input("Operación cancelada, presione enter para continuar: ")
                break
    input("Presione enter para continuar -->")  