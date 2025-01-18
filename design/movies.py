from tabulate import tabulate
from logic.movies import seeMovies
temporalMovies = []
def view_temporal_movies():
    if not temporalMovies:
        print("No hay peliculas registradas")
    else:
        table = [
            [
                movie["Titulo"],
                movie["Direccion"],
                movie["Producción"],
                movie["Valoracion"],
                ", ".join(movie["Genero"]),
                movie["Fecha de estreno"],
                movie["Categoria"]
            ]
            for movie in temporalMovies
        ]
        headers = ["Título", "Direccion", "Produccion", "Valoración", "Genero", "Fecha de estreno", "Categoria"]
        print("\n=== Peliculas Temporales Registradas ===")
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def loadJSONMovies():
    load = seeMovies()
    existing_titles = set()  
    movies_to_add = [] 
    for movie in temporalMovies:
        existing_titles.add(movie["Titulo"])    

    for movie in load:
        if movie["Titulo"] not in existing_titles:
            movies_to_add.append(movie)
    temporalMovies.extend(movies_to_add)

def newMovie():  
    watch = seeMovies() 
    title = input("Ingrese el titulo de la pelicula: ")
    findMovies = list(filter(lambda peli: peli.get("Titulo") == title, watch)) 
    findRepetition = list(filter(lambda peli: peli.get("Titulo") == title, temporalMovies))
    if(not len(findMovies)) and (not len(findRepetition)): 
        newMovie = {
            "Titulo": title,
            "Direccion": input("Ingrese el director de la pelicula: "),
            "Producción": input("Ingrese la producción de la pelicula: "),
            "Valoracion": input("Ingrese la valoración de la pelicula: "),
            "Genero": [],
            "Fecha de estreno": input("Ingrese la fecha de estreno de la pelicula: "),
            "Categoria": input("Ingrese la categoria de la pelicula: ")
            
        }
        while True:
            genero = input("Ingrese el genero de la pelicula: ").capitalize()
            if genero:
                newMovie["Genero"].append(genero)
            else:
                print("El genero no puede quedar vacio")
            confirmation = input("¿Quiere agregar otro genero? (s/n): ")
            if confirmation.lower() != "s":
                break
        temporalMovies.append(newMovie)
        print("Pelicula registrada con exito, si lo quiere guardar vaya al apartado de guardado")
        input("Presione enter para continuar -->")
    else: 
        print("La pelicula ya existe en su coleccion")
