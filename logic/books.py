import json

def seeBooks():
    with open("data/books.json", "r") as file:
        data = file.read() #Read es para hacerlo un string
        convertListOrDict = json.loads(data) #Lo convierte a estructura de datos
        return convertListOrDict

def saveBooks(data):
    with open("data/books.json", "w", encoding="utf-8") as file:
        str(data).encode('utf-8')
        convertJson = json.dumps(data, indent=4, ensure_ascii=False)
        file.write(convertJson)
        return "Se modificó el archivo products.json"