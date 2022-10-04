file = open('archivo.txt', 'w')
file.write("Escribiendo...\n")
file.close()

file = open('archivo.txt', 'r+')
file.readline()
file.write("Escribiendo...otra vez")

file.seek(0)
print(file.read())
file.close()
