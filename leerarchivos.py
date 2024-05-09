# Lee todo el contenido del archivo de una sola vez
import time
inicio = time.time()

with open('archivo.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    #print(contenido)
hola="saludos"

print("ultimo valor, ",contenido[3])
#for var in contenido:
#    print("valor", var)
fin = time.time()
print("tiempo ",fin-inicio)
input()





# Lee el archivo línea por línea usando un bucle
inicio = time.time()
with open('archivo.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        (linea.strip())  # `.strip()` elimina los saltos de línea al final
# Lee un número determinado de bytes o caracteres

fin = time.time()
print("tiempo ",fin-inicio)
input()

with open('archivo.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read(50)  # Lee los primeros 50 caracteres
    print(contenido)
