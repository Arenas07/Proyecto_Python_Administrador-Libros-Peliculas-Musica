from tabulate import tabulate
from logic.movies import seeMovies
temporalMovies = []
def view_temporal_movies(): #Ver peliculas en la lista temporal
    if not temporalMovies:
        print("No hay peliculas registradas")
    else:
        table = [
            [
                movie["ID"],
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
        headers = ["ID", "Título", "Direccion", "Produccion", "Valoración", "Genero", "Fecha de estreno", "Categoria"]
        print("\n=== Peliculas Temporales Registradas ===")
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def loadJSONMovies(): #Cargar peliculas a la lista temporal
    load = seeMovies()
    existing_titles = set()  
    movies_to_add = [] 
    for movie in temporalMovies:
        existing_titles.add(movie["Titulo"])    

    for movie in load:
        if movie["Titulo"] not in existing_titles:
            movies_to_add.append(movie)
    temporalMovies.extend(movies_to_add)

def newMovie(): #Formulario nueva pelicula
    watch = seeMovies() 
    title = input("Ingrese el titulo de la pelicula: ")
    findMovies = list(filter(lambda peli: peli.get("Titulo") == title, watch)) 
    findRepetition = list(filter(lambda peli: peli.get("Titulo") == title, temporalMovies))
    allIDS = []
    for code in watch:
        if "ID" in code:
            allIDS.append(code["ID"])
    lastId = allIDS[-1] if allIDS else "PL-0"
    id = input(f"Ingrese el ID del libro (ultimo codigo: {lastId}): ")
    findid = list(filter(lambda libro: libro.get("ID") == id.strip(), watch)) 
    findRepetitionid = list(filter(lambda repe: repe.get("ID") == id.strip(), temporalMovies))
    if(not len(findMovies)) and (not len(findRepetition)) and (not len(findid) and (not len(findRepetitionid))):
        newMovie = {
            "ID": id,
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
            confirmation = input("¿Quiere agregar otro genero? (s/n): ").strip()
            if confirmation.lower() != "s":
                break
        temporalMovies.append(newMovie)
        print("Pelicula registrada con exito, si lo quiere guardar vaya al apartado de guardado")
        input("Presione enter para continuar -->")
    else: 
        print("La pelicula ya existe en su coleccion")

def filterMoviesbyTitle(title): #Ver peliculas por titulo
    data = temporalMovies
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Titulo") == title): 
            dataModify.append(diccionario) 
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró la cancion")
    input("Presione enter para continuar -->  ")

def showMovieTitles(): #Ver titulos de las peliculas
    if temporalMovies:
        data = temporalMovies
        dataModify = []
        filtro = set()
        for titles in data:
            title = titles.get("Titulo")
            if title and title not in filtro:
                filtro.add(title)
                movie_copy = titles.copy()
                movie_copy.pop("Categoria")   
                movie_copy.pop("Direccion")
                movie_copy.pop("Valoracion")
                movie_copy.pop("Genero")
                movie_copy.pop("Producción")
                movie_copy.pop("Fecha de estreno")
                movie_copy.pop("Categoria")
                dataModify.append(movie_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def showMovieDirector(): #Ver director de las peliculas
    if temporalMovies:
        data = temporalMovies
        dataModify = []
        filtro = set()
        for titles in data:
            title = titles.get("Direccion")
            if title and title not in filtro:
                filtro.add(title)
                movie_copy = titles.copy()  
                movie_copy.pop("Titulo")
                movie_copy.pop("Valoracion")
                movie_copy.pop("Genero")
                movie_copy.pop("Producción")
                movie_copy.pop("Fecha de estreno")
                movie_copy.pop("Categoria")
                dataModify.append(movie_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def filterMoviesbyDirector(director): #Ver peliculas por director
    data = temporalMovies 
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Producción") == director): 
            dataModify.append(diccionario) 
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro")
    input("Presione enter para continuar -->  ")

def showMovieCategory(): #Ver categorias peliculas
    if temporalMovies:
        data = temporalMovies
        dataModify = []
        filtro = set()
        for titles in data:
            title = titles.get("Categoria")
            if title and title not in filtro:
                filtro.add(title)
                movie_copy = titles.copy()  
                movie_copy.pop("Titulo")
                movie_copy.pop("Valoracion")
                movie_copy.pop("Genero")
                movie_copy.pop("Producción")
                movie_copy.pop("Fecha de estreno")
                movie_copy.pop("Direccion")
                dataModify.append(movie_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def filterMoviebyCategory(category):  #Ver peliculas por categorias
    data = temporalMovies
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Categoria") == category): 
            dataModify.append(diccionario) 
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro")
    input("Presione enter para continuar -->  ")

def showMovieGenre(): #Ver generos de las peliculas
    if temporalMovies:
        data = temporalMovies
        dataModify = []
        filtro = set()
        for titles in data:
            generos = titles.get("Genero")
            for genero in generos:
                if genero and genero not in filtro:
                    filtro.add(genero)
                    movie_copy = titles.copy()
                    movie_copy.pop("Direccion")
                    movie_copy.pop("Titulo")
                    movie_copy.pop("Valoracion")
                    movie_copy.pop("Categoria")
                    movie_copy["Genero"] = genero
                    dataModify.append(movie_copy)
        if dataModify:
            print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
        else:
            print("No se encontraron géneros registrados")
    else:
        print("No se encontraron títulos registrados")

def filterMoviebyGenre(genero):  #Ver peliculas por genero
    data = temporalMovies
    dataModify = [] 
    for diccionario in data:
        if genero in diccionario.get("Genero"):
            dataModify.append(diccionario)
    
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el libro con ese género")
    
    input("Presione enter para continuar -->  ")