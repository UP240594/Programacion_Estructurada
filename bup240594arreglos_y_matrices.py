nombres = ['Ana', 'Luis', 'Carlos', 'Marta', 'Promedio']
materias = ['','Matemáticas', 'Física', 'Química', 'Biología']
calificaciones = [[10, 9, 8, 7],
                  [9, 7, 6, 8],
                  [8, 9, 5, 9],
                  [7, 8, 9, 10]]

Filas = len(calificaciones); #Aqui se esta contando la cantidad total de las filas
Columnas = len(calificaciones[0]); #Aqui se esta contando las columnas, desde la posicion 1

#Esto es para el nombre de las materias, queremos mostrar el array 
for i in range(Columnas+1):
	print(materias[i] , end="\t")
	
	if(i == Columnas):
		print()
	
		#Normal
for i in range(Filas): #filas
	print(nombres[i] , end = "\t" )
	sum=0
	
	for j in range(Columnas): #Columnas
		sum += calificaciones[i][j]
		
		print(" ",calificaciones[i][j], end="\t\t")
	print(sum/Columnas )
	 #Nueva linea después de cada fila
	
for j in range(Columnas): #columnas
	sum=0
	for i in range(Filas): #filas
		sum += calificaciones[i][j]
	print("  " ,sum/Filas, " ",end="\t" )




