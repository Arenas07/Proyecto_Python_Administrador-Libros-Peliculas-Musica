from design.books import  newBook, view_temporal_books, loadJSONBooks, showBookTitles, filterBooksbyTitle, showBookAutor, showBookCategory, filterBooksbyAutor, filterBooksbyCategory, showBookGenre, filterBooksbyGenre
from design.movies import newMovie, view_temporal_movies, loadJSONMovies, showMovieTitles, filterMoviesbyTitle, showMovieCategory, showMovieDirector, filterMoviesbyDirector, filterMoviebyCategory, showMovieGenre, filterMoviebyGenre
from design.music import newSong, view_temporal_songs, loadJSONSongs, showMusicTitles, filterMusicbyTitle, showMusicAutor, showMusicCategory, filterMusicbyCategory, filterMusicsbyAutor, showMusicGenre, filterMusicbyGenre
from logic.books import  editBooksTitle,  editBooksAutor, editBooksGenre, editBooksRate, editBooksCAT, deleteTEMPORAL, updateJsonWhenSave, deleteTEMPORALBookByName
from logic.movies import editMoviesTitle, editMovieDirection, editMovieGenre, editMovieProduction, editMovieRate, editMovieCAT, deleteTEMPORALMovie, deleteTEMPORALMoviebyName, updateJsonWhenSaveMovies
from logic.music import editMusicTitle, editMusicAutor, editMusicAlbum, editMusicGenre, editMusicCAT, editMusicDisc,   deleteTEMPORALSong, deleteTEMPORALSongbyName, updateJsonWhenSaveMusic
def menu_principal():
   print("""
            ===========================================
                    Administrador de Colección
            ===========================================
                1. Añadir un Nuevo Elemento
                2. Ver Todos los Elementos
                3. Buscar un Elemento
                4. Editar un Elemento
                5. Eliminar un Elemento
                6. Ver Elementos por Categoría
                7. Guardar y Cargar Colección
                8. Salir
            ===========================================
                Selecciona una opción (1-8):""")
   opcion_menu = input("--> ")   
   while True:

         try:
            match opcion_menu:
               case "1":
                  print("""
                        ===========================================
                              Añadir un Nuevo Elemento
                        ===========================================
                           ¿Qué tipo de elemento deseas añadir?
                        1. Libro
                        2. Película
                        3. Música
                        4. Regresar al Menú Principal
                        ===========================================
                           Selecciona una opción (1-4):""")
                  selection = input("Seleccione la opción que prefiera --> ")
                  try:
               
                     match selection:
                        case "1":
                           newBook()
                        case "2":
                           newMovie()
                        case "3":
                           newSong()
                        case "4":
                           return menu_principal()
                        case _:
                           input("Opcion no valida, presione enter para continuar -->")
                  except KeyboardInterrupt:
                     input("\n Volviendo al menu, presione enter para continuar -->")
                     return menu_principal()
               case "2":
                  print("""
                     ===========================================
                              Ver Todos los Elementos
                     ===========================================
                           ¿Qué categoría deseas ver?
                        1. Ver Todos los Libros
                        2. Ver Todas las Películas
                        3. Ver Toda la Música
                        4. Regresar al Menú Principal
                     ===========================================
                        Selecciona una opción (1-4):""")
                  selection = input("Seleccione la opción que prefiera --> ")
                  try:
                  
                     match selection:
                        case "1":
                           view_temporal_books()
                        case "2":
                           view_temporal_movies()
                        case "3":
                           view_temporal_songs()
                        case "4":
                           return menu_principal()
                        case _:
                           input("Opcion no encontrada, presione enter para continuar --> ")
                  except KeyboardInterrupt:
                     input("\n Volviendo al menu, presione enter para continuar -->")
                     return menu_principal()
               case "3":
                  print("""
                     ===========================================
                                 Buscar un Elemento
                     =========================================== 
                                 ¿Cómo deseas buscar?
                        1. Buscar por Título
                        2. Buscar por Autor/Director/Artista
                        3. Buscar por Genero
                        4. Regresar al Menú Principal
                     ===========================================
                        Selecciona una opción (1-4):""")
                  selection = input("Seleccione la opción que prefiera --> ")
                  try:
                     
                     match selection:
                        case "1":
                           print("""
                        ===========================================
                                    Buscar por Titulo
                        =========================================== 
                                    ¿Cómo deseas buscar?
                           1. Libros
                           2. Peliculas
                           3. Musica
                           4. Regresar a Buscar un elemento
                        ===========================================
                           Selecciona una opción (1-4):"""
                                 )
                           menu_selection = input("-->")
                           try:
                              
                              match menu_selection:
                                 case "1":
                                    showBookTitles()
                                    filterBooksbyTitle(input("Ingrese el titulo del libro: "))
                                 case "2":
                                    showMovieTitles()
                                    filterMoviesbyTitle(input("Ingrese el titulo de la pelicula: "))
                                 case "3":
                                    showMusicTitles()
                                    filterMusicbyTitle(input("Ingrese el titulo de la cancion: "))
                                 case "4":
                                    return menu_principal()
                                 case _:
                                    print("Opcion no encontrada")
                           except KeyboardInterrupt:
                              input("\n Volviendo al menu, presione enter para continuar -->")
                              return menu_principal()
                        case "2":
                           print("""
                        ===========================================
                              Buscar por Autor/Director/Artista
                        =========================================== 
                                    ¿Cómo deseas buscar?
                           1. Libros
                           2. Peliculas
                           3. Musica
                           4. Regresar a Buscar un elemento
                        ===========================================
                           Selecciona una opción (1-4):"""
                                 )
                           menu_selection = input("-->")
                           try:
                           
                              match menu_selection:
                                 case "1":
                                    showBookAutor()
                                    filterBooksbyAutor(input("Ingrese el titulo del libro: "))
                                 case "2":
                                    showMovieDirector()
                                    filterMoviesbyDirector(input("Ingrese el director de la pelicula: "))
                                 case "3":
                                    showMusicAutor()
                                    filterMusicsbyAutor(input("Ingrese el autor de la cancion: "))
                                 case "4":
                                    return menu_principal()
                                 case _:
                                    input("Opcion no disponible, presione enter para continuar -->")
                           except KeyboardInterrupt:
                              input("\n Volviendo al menu, presione enter para continuar -->")
                              return menu_principal()
                        case "3":
                           print("""
                        ===========================================
                                    Buscar por Genero
                        =========================================== 
                                    ¿Cómo deseas buscar?
                           1. Libros
                           2. Peliculas
                           3. Musica
                           4. Regresar a Buscar un elemento
                        ===========================================
                           Selecciona una opción (1-4):"""
                                 )
                           menu_selection = input("-->")
                           try:
                              
                              match menu_selection:
                                 case "1":
                                    showBookGenre()
                                    filterBooksbyGenre(input("Ingrese el genero del libro: "))
                                 case "2":
                                    showMovieGenre()
                                    filterMoviebyGenre(input("Ingrese el genero de la pelicula: "))
                                 case "3":
                                    showMusicGenre()
                                    filterMusicbyGenre(input("Ingrese el genero de la cancion: "))
                                 case "4":
                                    return menu_principal()
                                 case _:
                                    input("Opcion no disponible, presione enter para continuar --> ")  
                           except KeyboardInterrupt:
                              input("\n Volviendo al menu, presione enter para continuar -->")
                              return menu_principal()
                        case "4":
                           return menu_principal()
                        case _:
                           print("Opción no válida, por favor seleccione una opción válida.")
                  except KeyboardInterrupt:
                     input("\n Volviendo al menu, presione enter para continuar -->")
                     return menu_principal()
               case "4":
                  print("""
                     ===========================================
                                 Editar un Elemento
                     ===========================================
                        ¿Qué tipo de cambio deseas realizar?
                        1. Editar Libro
                        2. Editar Peliculas
                        3. Editar Canciones
                        4. Regresar al Menú Principal
                     ===========================================
                           Selecciona una opción (1-4):""")
                  selection = input("Ingrese la opcion --> ")
                  try:
                  
                     match selection:
                        case "1":
                           print("""
                        ===========================================
                                    Editar un Elemento
                        ===========================================
                           ¿Qué tipo de cambio deseas realizar?
                           1. Editar Título
                           2. Editar Autor
                           3. Editar Género
                           4. Editar Valoración
                           5. Editar Categoria
                           6. Regresar al Menú Principal
                        ===========================================
                              Selecciona una opción (1-6):""")
                           selection = input("Ingrese la opcion --> ")
                           try:
                              
                              match selection:
                                 case "1":
                                    view_temporal_books()
                                    id = input("Ingrese la ID del libro para buscar: ")
                                    newTitle = input("Ingrese el titulo por el que lo quiere reemplazar: ")
                                    editBooksTitle(id, newTitle)
                                 case "2":
                                    view_temporal_books()
                                    id = input("Ingrese la ID de la pelicula para buscar: ")
                                    newAutor = input("Ingrese el Autor por el que lo quiere reemplazar: ")
                                    editBooksAutor(id, newAutor)
                                 case "3":
                                    view_temporal_books()
                                    id = input("Ingrese la ID del libro para buscar: ")
                                    editBooksGenre(id)
                                 case "4":
                                    try:
                                       view_temporal_books()
                                       id = input("Ingrese la ID del libro para buscar: ")
                                       newRate = float(input("Ingrese la nueva valoración del libro: "))
                                       editBooksRate(id, newRate)
                                    except ValueError:
                                       input("Rango no disponible, porfavor use numeros")
                                 case "5":
                                    view_temporal_books()
                                    id = input("Ingrese la ID del libro para buscar: ")
                                    newCAT = input("Ingrese la nueva categoria del libro ")
                                    editBooksCAT(id, newCAT)
                                 case "6":
                                    return menu_principal()
                                 case _:
                                    print("Opcion no disponible")
                                    input("Presione enter para continuar --> ")
                           except KeyboardInterrupt:
                              input("\n Volviendo al menu, presione enter para continuar -->")
                              return menu_principal()
                        case "2":
                           print("""
                        ===========================================
                                    Editar un Elemento
                        ===========================================
                           ¿Qué tipo de cambio deseas realizar?
                           1. Editar Título
                           2. Editar Direccion
                           3. Editar Produccion
                           4. Editar Valoración
                           5. Editar Genero
                           6. Editar Categoria
                           7. Regresar al Menú Principal
                        ===========================================
                              Selecciona una opción (1-7):""")
                           selection = input("Ingrese la opcion --> ")
                           try:
                              
                              match selection:
                                 case "1":
                                    view_temporal_movies()
                                    id = input("Ingrese la ID de la pelicula para buscar: ")
                                    newTitle = input("Ingrese el Titulo por el que lo quiere reemplazar: ")
                                    editMoviesTitle(id, newTitle)
                                 case "2":
                                    view_temporal_movies()
                                    id = input("Ingrese la ID de la pelicula para buscar: ")
                                    newAutor = input("Ingrese el Autor por el que lo quiere reemplazar: ")
                                    editMovieDirection(id, newAutor)
                                 case "3":
                                    view_temporal_movies()
                                    id = input("Ingrese la ID de la pelicula para buscar: ")
                                    newPro = input("Ingrese el productor por el que lo quiere reemplazar: ")
                                    editMovieProduction(id, newPro)
                                 case "4":
                                    try:
                                       view_temporal_movies()
                                       id = input("Ingrese la ID de la pelicula para buscar: ")
                                       newRate = float(input("Ingrese la valoracion por la que lo quiere reemplazar: "))
                                       editMovieRate(id, newRate)
                                    except ValueError:
                                       input("Rango no disponible, porfavor use numeros")
                                 case "5":
                                    view_temporal_movies()
                                    id = input("Ingrese la ID de la pelicula para buscar: ")
                                    editMovieGenre(id)
                                 case "6":
                                    view_temporal_movies()
                                    id = input("Ingrese la ID de la pelicula para buscar: ")
                                    newCAT = input("Ingrese la nueva categoria: ")
                                    editMovieCAT(id, newCAT)
                                 case "7":
                                    return menu_principal()
                                 case _:
                                    input("Opcion ingresada no existe, presione enter para continuar -->")
                           except KeyboardInterrupt:
                              input("\n Volviendo al menu, presione enter para continuar -->")
                              return menu_principal()
                        case "3":
                           print("""
                        ===========================================
                                    Editar un Elemento
                        ===========================================
                           ¿Qué tipo de cambio deseas realizar?
                           1. Editar Título
                           2. Editar Autor
                           3. Editar Album
                           4. Editar Genero
                           5. Editar Categoria
                           6. Editar Discografica
                           7. Regresar al Menú Principal
                        ===========================================
                              Selecciona una opción (1-7):""")
                           selection = input("Ingrese la opcion --> ")
                           try:
                           
                              match selection:
                                 case "1":
                                    view_temporal_songs()
                                    id = input("Ingrese la ID de la cancion para buscar: ")
                                    title = input("Ingrese el nuevo nombre de la canción: ")
                                    editMusicTitle(id, title)
                                 case "2":
                                    view_temporal_songs()
                                    id = input("Ingrese la ID de la cancion para buscar: ")
                                    autor = input("Ingrese el autor de la cancion: ")
                                    editMusicAutor(id, autor)
                                 case "3":
                                    view_temporal_songs()
                                    id = input("Ingrese la ID de la cancion para buscar: ")
                                    album = input("Ingrese el album de la cancion: ")
                                    editMusicAlbum(id, album)
                                 case "4":   
                                    view_temporal_songs()
                                    id = input("Ingrese la ID de la cancion")
                                    editMusicGenre(id)
                                 case "5":
                                    view_temporal_songs()
                                    id = input("Ingrese la ID de la cancion para buscar: ")
                                    cat = input("Ingrese la categoria de la cancion: ")
                                    editMusicCAT(id, cat)
                                 case "6":
                                    view_temporal_songs()
                                    id = input("Ingrese la ID de la cancion para buscar: ")
                                    disc = input("Ingrese la discografica de la cancion: ")
                                    editMusicDisc(id, disc)
                                 case "7":
                                    return menu_principal()
                                 case _:
                                    print("La opcion ingresada no se encuentra disponible")
                                    input("Presione enter para continuar --> ")
                           except KeyboardInterrupt:
                              input("\n Volviendo al menu, presione enter para continuar -->")
                              return menu_principal()
                        case "4":
                           return menu_principal()
                        case _:
                           input("Opcion no disponible, presione enter para continuar -->")
                  except KeyboardInterrupt:
                     input("\n Volviendo al menu, presione enter para continuar -->")
                     return menu_principal()
               case "5":
                  print("""
                     ===========================================
                                 Eliminar un Elemento
                     ===========================================
                              ¿Cómo deseas eliminar?
                        1. Eliminar por Título
                        2. Eliminar por Identificador Único
                        3. Regresar al Menú Principal
                     ===========================================
                        Selecciona una opción (1-3):""")
                  selection = input("Seleccione una opcion --> ")
                  try:
                     
                     match selection:
                        case "1":
                           print("""
                        ===========================================
                                    Eliminar un Elemento
                        ===========================================
                           ¿Qué tipo de cambio deseas realizar?
                           1. Eliminar Libro
                           2. Eliminar Peliculas
                           3. Eliminar Canciones
                           4. Regresar al Menú Principal
                        ===========================================
                              Selecciona una opción (1-4):""")
                           selection = input("Ingrese la opcion --> ")
                           try:
                              
                              match selection:
                                 case "1":
                                    view_temporal_books()
                                    title = input("Seleccione el titulo del libro a eliminar: ")
                                    deleteTEMPORALBookByName(title)
                                 case "2":
                                    view_temporal_movies()
                                    title = input("Seleccione el titulo de la pelicula a eliminar: ")
                                    deleteTEMPORALMoviebyName(title)
                                 case "3":
                                    view_temporal_songs()
                                    title = input("Seleccione el titulo de la cancion a eliminar: ")
                                    deleteTEMPORALSongbyName(title)
                                 case "4":
                                    return menu_principal()
                                 case _:
                                    input("Opcion no disponible, presione enter para continuar -->")
                           except KeyboardInterrupt:
                              input("\n Volviendo al menu, presione enter para continuar -->")
                              return menu_principal()
                        case "2":
                           print("""
                        ===========================================
                                    Eliminar un Elemento
                        ===========================================
                           ¿Qué tipo de cambio deseas realizar?
                           1. Eliminar Libro
                           2. Eliminar Peliculas
                           3. Eliminar Canciones
                           4. Regresar al Menú Principal
                        ===========================================
                              Selecciona una opción (1-4):""")
                           selection = input("Ingrese la opcion --> ")
                           try:
                              
                              match selection:
                                 case "1":
                                    view_temporal_books()
                                    id = input("Seleccione la ID del libro a eliminar: ")
                                    deleteTEMPORAL(id)
                                 case "2":
                                    view_temporal_movies()
                                    id = input("Seleccione la ID de la pelicula a eliminar: ")
                                    deleteTEMPORALMovie(id)
                                 case "3":
                                    view_temporal_songs()
                                    id = input("Seleccione la ID de la cancion a eliminar: ")
                                    deleteTEMPORALSong(id)
                                 case "4":
                                    return menu_principal()
                                 case _:
                                    input("Opcion no disponible, preisone enter para continuar --> ")
                           except KeyboardInterrupt:
                              input("Volviendo al menu, presione enter para continuar -->")
                              return menu_principal()
                        case "3":
                           return menu_principal()
                        case _:
                           input("Opcion no disponible, presione enter para continuar -->")
                  except KeyboardInterrupt:
                     input("\n Volviendo al menu, presione enter para continuar -->")
                     return menu_principal()
               case "6":
                  print("""
                     ===========================================
                           Ver Elementos por Categoría
                     ===========================================
                           ¿Qué categoría deseas ver?
                        1. Ver Libros
                        2. Ver Películas
                        3. Ver Música
                        4. Regresar al Menú Principal
                     ===========================================
                        Selecciona una opción (1-4):""")
                  selection = input("Ingrese la opcion --> ")
                  try:
                     
                     match selection:
                        case "1":
                           showBookCategory()
                           filterBooksbyCategory(input("Ingrese la categoria del libro: "))
                        case "2":
                           showMovieCategory()
                           filterMoviebyCategory(input("Ingrese la categoria de la pelicula: "))
                        case "3":
                           showMusicCategory()
                           filterMusicbyCategory(input("Ingrese la categoria de la cancion: "))
                        case "4":
                           return menu_principal()
                        case _:
                           input("Opcion no disponible, presione enter para continuar -->")        
                  except KeyboardInterrupt:
                     input("\n Volviendo al menu, presione enter para continuar -->")
                     return menu_principal()

               case "7":
                  print("""
                     ===========================================
                              Guardar y Cargar Colección
                     ===========================================
                                 ¿Qué deseas hacer?
                        1. Guardar la Colección Actual
                        2. Cargar una Colección Guardada
                        3. Regresar al Menú Principal
                     ===========================================
                        Selecciona una opción (1-3):""")
                  selection = input("--> ")
                  try:
                     
                     match selection:
                        case "1":
                           updateJsonWhenSave()
                           updateJsonWhenSaveMovies()
                           updateJsonWhenSaveMusic()
                           print("Cambios realizados con exito")
                           input("Presione enter para continuar -->")
                        case "2":
                           loadJSONBooks()
                           loadJSONMovies()
                           loadJSONSongs()
                           input("Archivos cargados correctamente, presione enter para continuar -->")
                        case "3":
                           return menu_principal()
                        case _:
                           input("Opcion no disponible, presione enter para continuar -->")
                  except KeyboardInterrupt:
                     input("\n Volviendo al menu, presione enter para continuar -->")
                     return menu_principal()
               case "8":
                  print("Gracias por usar el programa")
                  break
               case _:
                  input("Opción no disponible, presione enter para continuar -->")
                  return menu_principal()
         except KeyboardInterrupt:
            print("\n Saliendo del programa")
            break
            

