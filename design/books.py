from tabulate import tabulate
from logic.books import seeBooks

def seeAllBooksInTables():
    watch = seeBooks()
    watchModificated = []
    for modify in watch:
        modify.pop("Sinopsis")
        watchModificated.append(modify)
    print(tabulate(watchModificated, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    input("--> Presione enter para continuar")