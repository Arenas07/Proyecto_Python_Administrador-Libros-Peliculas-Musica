from design.books import  newBook, temporalBooks, view_temporal_books, loadJSONBooks, showBookTitles, filterBooksbyTitle, showBookAutor, showBookCategory, filterBooksbyAutor, filterBooksbyCategory
from design.movies import newMovie, temporalMovies, view_temporal_movies, loadJSONMovies, showMovieTitles, filterMoviesbyTitle, showMovieCategory, showMovieDirector, filterMoviesbyDirector, filterMoviebyCategory
from design.music import newSong,  temporalSongs, view_temporal_songs, loadJSONSongs, showMusicTitles, filterMusicbyTitle, showMusicAutor, showMusicCategory, filterMusicbyCategory, filterMusicsbyAutor
from logic.books import saveBooks
from logic.movies import saveMovie
from logic.music import saveMusic
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
            match selection:
               case "1":
                  newBook()
               case "2":
                  newMovie()
               case "3":
                  newSong()
               case "4":
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

         case "3":
            print("""
                 ===========================================
                            Buscar un Elemento
                 =========================================== 
                           ¿Cómo deseas buscar?
                    1. Buscar por Título
                    2. Buscar por Autor/Director/Artista
                    3. Buscar por Categoria
                    4. Regresar al Menú Principal
                 ===========================================
                    Selecciona una opción (1-4):""")
            selection = input("Seleccione la opción que prefiera --> ")
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
                  match menu_selection:
                     case "1":
                        showBookTitles()
                        filterBooksbyTitle(input("Ingrese el titulo del libro: ").capitalize())
                     case "2":
                        showMovieTitles()
                        filterMoviesbyTitle(input("Ingrese el titulo de la pelicula: ").capitalize())
                     case "3":
                        showMusicTitles()
                        filterMusicbyTitle(input("Ingrese el titulo de la cancion: ").capitalize())
                     case "4":
                        return menu_principal()
                     case _:
                        print("Opcion no encontrada")
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
                  match menu_selection:
                     case "1":
                        showBookAutor()
                        filterBooksbyAutor(input("Ingrese el titulo del libro: ").capitalize())
                     case "2":
                        showMovieDirector()
                        filterMoviesbyDirector(input("Ingrese el director de la pelicula: ".capitalize()))
                     case "3":
                        showMusicAutor()
                        filterMusicsbyAutor(input("Ingrese el autor de la cancion: ").capitalize()  )
                     case "4":
                        break
               case "3":
                  print("""
                 ===========================================
                           Buscar por Categoria
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
                  match menu_selection:
                     case "1":
                        showBookCategory()
                        filterBooksbyCategory(input("Ingrese la categoria del libro: ").capitalize())
                     case "2":
                        showMovieCategory()
                        filterMoviebyCategory(input("Ingrese la categoria de la pelicula: ").capitalize())
                     case "3":
                        showMusicCategory()
                        filterMusicbyCategory(input("Ingrese la categoria de la cancion: ").capitalize())
                     case "4":
                        break        
               case "4":
                  return menu_principal()
               case _:
                  print("Opción no válida, por favor seleccione una opción válida.")
         case "4":
            print("""
                 ===========================================
                            Editar un Elemento
                 ===========================================
                   ¿Qué tipo de cambio deseas realizar?
                  1. Editar Título
                  2. Editar Autor/Director/Artista
                  3. Editar Género
                  4. Editar Valoración
                  5. Regresar al Menú Principal
                 ===========================================
                     Selecciona una opción (1-5):""")
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
            match selection:
               case "1":
                  saveBooks(temporalBooks)
                  saveMusic(temporalSongs)
                  saveMovie(temporalMovies)
                  input("Presione enter para continuar")
               case "2":
                  loadJSONBooks()
                  loadJSONMovies()
                  loadJSONSongs()
                  input("Presione enter para continuar")

               case "3":
                  return menu_principal()
         case "8":
            print("Gracias por usar el programa")
            break
         case _:
            input("Opción no disponible, presione enter para continuar -->")
            return menu_principal()
         

