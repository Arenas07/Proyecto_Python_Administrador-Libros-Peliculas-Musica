import json

def seeMovies(): #Ver las peliculas del json
    with open("data/movies.json", "r", encoding="utf-8") as file:
            return json.load(file)
    
def updateJsonWhenSaveMovies(): #Actualizar al haber un cambio
    from design.movies import temporalMovies
    list = temporalMovies
    with open("data/movies.json", "w", encoding="utf-8") as file:
        convertJson = json.dumps(list, indent=4, ensure_ascii=False)
        file.write(convertJson)

    temporalMovies.clear()


def editMoviesTitle(movie_id, new_title):  #Editar titulo peliculas
    from design.movies import temporalMovies
    for movie in temporalMovies:
        if movie["ID"] == movie_id.strip(): #si el id existe
            movie["Titulo"] = new_title  #actualiza el titulo
            print("Se ha actualizado el título en la lista temporal")
            break

def editMovieDirection(movie_id, direction): #Editar el director
    from design.movies import temporalMovies 
    for movie in temporalMovies: 
        if movie["ID"] == movie_id.strip(): #si el id existe
            movie["Direccion"] = direction  #actualiza el director

            print("Se ha actualizado el director en la lista temporal")
            break

def editMovieGenre(movie_id): #Editar genero de la pelicula
    from design.movies import temporalMovies

    for movie in temporalMovies:
        if movie["ID"] == movie_id.strip(): #si el id existe
            new_genre = [] 
            while True: #Ciclo para agregar
                opcion = input("Ingrese el genero nuevo: ")
                new_genre.append(opcion)
                opc = input("Quiere agregar otro genero? (s/n): ").strip()
                if opc.lower() != "s":
                    break
                if new_genre:
                    movie["Genero"] = new_genre #actualiza el genero
                else:
                    print("No se han ingresado generos")

def editMovieProduction(movie_id, production): #Editar el productor de la pelicula
    from design.movies import temporalMovies
    for movie in temporalMovies:
        if movie["ID"] == movie_id.strip(): #si el id existe
            movie["Producción"] = production #Actualiza el productor

            print("Se ha actualizado la producción en la lista temporal")
            break

def editMovieRate(movie_id, rate): #Editar la valoracion de la pelicula
    from design.movies import temporalMovies 
    for movie in temporalMovies:
        if movie["ID"] == movie_id.strip(): #si el id existe
            movie["Valoracion"] = rate   #Actualiza la valoracion
            print("Se ha actualizado la valoracion en la lista temporal")
            break

def editMovieCAT(movie_id, CAT):  #Editar la categoria de la pelicula
    from design.movies import temporalMovies
    for movie in temporalMovies:
        if movie["ID"] == movie_id.strip(): #si el id existe
            movie["Categoria"] = CAT  #actualiza la categoria
            print("Se ha actualizado la categoria en la lista temporal")
            break

def deleteTEMPORALMovie(id): #borrar de la lista temporal
    from design.movies import temporalMovies
    info = temporalMovies
    
    for code in info: 
        if id.strip() == code.get("ID"): #si el id existe
            security = input("¿Está seguro de eliminar la pelicula? (s/n): ".strip())
            if security.lower() == "s":  
                info.remove(code)  
                print("Pelicula eliminada correctamente")
                break
            else:
                input("Operación cancelada, presione enter para continuar: ")
                break
    input("Presione enter para continuar -->")     

def deleteTEMPORALMoviebyName(title): #borrar de la lista temporal
    from design.movies import temporalMovies
    info = temporalMovies
    
    for code in info: 
        if title == code.get("Titulo"):  #borra por nombre
            security = input("¿Está seguro de eliminar la pelicula? (s/n): ".strip())
            if security.lower() == "s":  
                info.remove(code)  
                print("Pelicula eliminada correctamente")
                break
            else:
                input("Operación cancelada, presione enter para continuar: ")
                break
    input("Presione enter para continuar -->")  