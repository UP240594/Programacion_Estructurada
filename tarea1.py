nombres = ['Ana', 'Luis', 'Carlos', 'Marta']
materias = ['','Matemáticas', 'Física', 'Química', 'Biología']
calificaciones = [[10, 9, 8, 7],
                  [9, 7, 6, 8],
                  [8, 9, 5, 9],
                  [7, 8, 9, 10]]

Filas = len(calificaciones);
Columnas = len(calificaciones[0]);


for i in range(Columnas):
	print(materias[i] , end="\t")
	print()
#Normal
for i in range(Filas): #filas
	print(materias[i] , end="\t")
	print()
	for j in range(Columnas): #Columnas
		print(calificaciones[i][j], end="\t")
	print() #Nueva linea después de cada fila
