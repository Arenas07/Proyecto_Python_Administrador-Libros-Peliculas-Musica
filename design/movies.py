from tabulate import tabulate
from logic.movies import seeMovies
temporalMovies = []
def view_temporal_movies(): #Ver peliculas en la lista temporal
    if not temporalMovies: #Si no encuentra nada en la lista
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
            for movie in temporalMovies #Ciclo para ir viendo cada valor de las peliculas
        ] #Tabular esa informacion
        headers = ["ID", "Título", "Direccion", "Produccion", "Valoración", "Genero", "Fecha de estreno", "Categoria"]
        print("\n=== Peliculas Temporales Registradas ===")
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

def loadJSONMovies(): #Cargar peliculas a la lista temporal
    load = seeMovies()
    existing_titles = set()  
    movies_to_add = [] 
    for movie in temporalMovies: #Mira todas las peliculas de la lista
        existing_titles.add(movie["Titulo"]) #Revisa el titulo que tienen

    for movie in load: #Mira todas las peliculas cargadas en el json
        if movie["Titulo"] not in existing_titles: #Compara si no son repetidas
            movies_to_add.append(movie) 
    temporalMovies.extend(movies_to_add) #Las mete al archivo temporal

def newMovie(): #Formulario nueva pelicula
    watch = seeMovies() #Toma la información actual del JSON
    title = input("Ingrese el titulo de la pelicula: ")
    findMovies = list(filter(lambda peli: peli.get("Titulo") == title, watch)) #Filtro para saber todos los titulos 
    findRepetition = list(filter(lambda peli: peli.get("Titulo") == title, temporalMovies)) #Filtro para saber los titulos temporales
    allIDS = []
    for code in watch:
        if "ID" in code:
            allIDS.append(code["ID"])
            #Pone todos los codigos en la lista allIDS
    lastId = allIDS[-1] if allIDS else "PL-0"
    #Revisa el ultimo codigo registrado en la lista
    id = input(f"Ingrese el ID de la pelicula (ultimo codigo: {lastId}): ")
    findid = list(filter(lambda peli: peli.get("ID") == id.strip(), watch)) #Filtro buscar IDS
    findRepetitionid = list(filter(lambda repe: repe.get("ID") == id.strip(), temporalMovies)) #Buscar ids en la lista temporal
    if(not len(findMovies)) and (not len(findRepetition)) and (not len(findid) and (not len(findRepetitionid))):
        #Si no hay repeticion prosiga con el formulario
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
        while True: #Ciclo para agregar mas de un genero al libro
            genero = input("Ingrese el genero de la pelicula: ").capitalize()
            if genero:
                newMovie["Genero"].append(genero)
            else:
                print("El genero no puede quedar vacio")
            confirmation = input("¿Quiere agregar otro genero? (s/n): ").strip()
            if confirmation.lower() != "s":
                break
        temporalMovies.append(newMovie) #Toda la info la guarda como nuevo libro en la lista temporal
        print("Pelicula registrada con exito, si lo quiere guardar vaya al apartado de guardado")
        input("Presione enter para continuar -->")
    else: 
        print("La pelicula ya existe en su coleccion") #Validacion

def filterMoviesbyTitle(title): #Ver peliculas por titulo
    data = temporalMovies #Tomamos todos los titulos
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Titulo") == title): #Si el titulo ingresado se encuentra entre los disponibles
            dataModify.append(diccionario) #Append para mostrar toda su informacion y despues tabular
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
        for titles in data: #Recorre todos los libros
            title = titles.get("Titulo") #Title almacena todos los titulos registrados
            if title and title not in filtro: #Si existen titulos y no se encuentra repetido
                filtro.add(title) #Añade el titulo al filtro para que no se repita
                movie_copy = titles.copy() #saco una copia para no modificar la lista original
                movie_copy.pop("Categoria")   
                movie_copy.pop("Direccion")
                movie_copy.pop("Valoracion") #borro toda la info que no es necesaria
                movie_copy.pop("Genero")
                movie_copy.pop("Producción")
                movie_copy.pop("Fecha de estreno")
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
            title = titles.get("Direccion") #Recorre todas las peliculas
            if title and title not in filtro: #Title almacena todos los autores registrados
                filtro.add(title) #Añade el titulo al filtro para que no se repita
                movie_copy = titles.copy() #saco una copia para no modificar la lista original
                movie_copy.pop("Titulo")
                movie_copy.pop("Valoracion")
                movie_copy.pop("Genero")
                movie_copy.pop("Producción") #borro toda la info que no es necesaria
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
        if(diccionario.get("Direccion") == director): #Si el input del director es el mismo al del json
            dataModify.append(diccionario) #Muestra toda la informacion de la lista
    if dataModify:   
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el director")
    input("Presione enter para continuar -->  ")

def showMovieCategory(): #Ver categorias peliculas
    if temporalMovies:
        data = temporalMovies
        dataModify = []
        filtro = set()
        for titles in data:
            title = titles.get("Categoria") #Recorre todas las peliculas
            if title and title not in filtro:#Title almacena todos los autores registrados
                filtro.add(title) #Añade el titulo al filtro para que no se repita
                movie_copy = titles.copy()  #saco una copia para no modificar la lista original
                movie_copy.pop("Titulo")
                movie_copy.pop("Valoracion")
                movie_copy.pop("Genero")
                movie_copy.pop("Producción")
                movie_copy.pop("Fecha de estreno") #borro toda la info que no es necesaria
                movie_copy.pop("Direccion")
                dataModify.append(movie_copy)
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontraron títulos registrados")

def filterMoviebyCategory(category):  #Ver peliculas por categorias
    data = temporalMovies
    dataModify = []
    for diccionario in data: 
        if(diccionario.get("Categoria") == category): #Si el input del director es el mismo al del json
            dataModify.append(diccionario) #Muestra toda la informacion de la lista
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró la pelicula")
    input("Presione enter para continuar -->  ")

def showMovieGenre(): #Ver generos de las peliculas
    if temporalMovies:
        data = temporalMovies
        dataModify = []
        filtro = set()
        for titles in data:
            generos = titles.get("Genero") #Recorre todas las peliculas
            for genero in generos: #Recorre todos los generos dentro de la lista
                if genero and genero not in filtro: #Title almacena todos los autores registrados
                    filtro.add(genero) #Añade el titulo al filtro para que no se repita
                    movie_copy = titles.copy() #saco una copia para no modificar la lista original
                    movie_copy.pop("Direccion")
                    movie_copy.pop("Titulo")
                    movie_copy.pop("Valoracion")
                    movie_copy.pop("Producción")
                    movie_copy.pop("Fecha de estreno") #borro toda la info que no es necesaria
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
        if genero in diccionario.get("Genero"): #Si el input del director es el mismo al del json
            dataModify.append(diccionario) #Muestra toda la informacion de la lista
    
    if dataModify:    
        print(tabulate(dataModify, headers="keys", tablefmt="grid", numalign="center"))
    else:
        print("No se encontró el la pelicula con ese género")
    
    input("Presione enter para continuar -->  ")