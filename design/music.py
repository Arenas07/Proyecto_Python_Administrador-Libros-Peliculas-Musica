from tabulate import tabulate
from logic.music import seeMusic

def seeAllMusicInTables():
    watch = seeMusic()
    print(tabulate(watch, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    input("--> Presione enter para continuar")