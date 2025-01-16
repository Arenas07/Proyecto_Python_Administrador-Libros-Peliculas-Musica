from tabulate import tabulate
from logic.movies import seeMovies

def seeAllMoviesInTables():
    watch = seeMovies()
    watchModificated = []
    for modify in watch:
        modify.pop("Descripcion")
        watchModificated.append(modify)
    print(tabulate(watchModificated, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    input("--> Presione enter para continuar")