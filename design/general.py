from design.books import seeAllBooksInTables
from design.movies import seeAllMoviesInTables
from design.music import seeAllMusicInTables

def menu_principal():
   print("""===========================================
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
            print("""===========================================
                            Añadir un Nuevo Elemento
                     ===========================================
                        ¿Qué tipo de elemento deseas añadir?
                     1. Libro
                     2. Película
                     3. Música
                     4. Regresar al Menú Principal
                     ===========================================
                         Selecciona una opción (1-4):""")
         case "2":
            print("""===========================================
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
                  seeAllBooksInTables()
               case "2":
                  seeAllMoviesInTables()
               case "3":
                  seeAllMusicInTables()
               case "4":
                  return menu_principal()
               case _:
                  input("Opcion no encontrada, presione enter para continuar --> ")

         case "3":
            print("""===========================================
                            Buscar un Elemento
                 =========================================== #! CAMBIAR ESTO DE LUGAR
                           ¿Cómo deseas buscar?
                    1. Buscar por Título
                    2. Buscar por Autor/Director/Artista
                    3. Buscar por Género
                    4. Regresar al Menú Principal
                 ===========================================
                    Selecciona una opción (1-4):""")
         case "4":
            print("""===========================================
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
            print("""===========================================
                           Eliminar un Elemento
                 ===========================================
                          ¿Cómo deseas eliminar?
                    1. Eliminar por Título
                    2. Eliminar por Identificador Único
                    3. Regresar al Menú Principal
                 ===========================================
                    Selecciona una opción (1-3):""")
         case "6":
            print("""===========================================
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
            print("""===========================================
                        Guardar y Cargar Colección
                 ===========================================
                            ¿Qué deseas hacer?
                    1. Guardar la Colección Actual
                    2. Cargar una Colección Guardada
                    3. Regresar al Menú Principal
                 ===========================================
                    Selecciona una opción (1-3):""")
         case "8":
            break
         case _:
            input("Opción no disponible, presione enter para continuar -->")
         

