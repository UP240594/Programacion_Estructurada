#Tabla de multiplicar, Descendente
print("Decendente ")
def multiplicar(n):
       if( n <= 1):
              n = n*1
              print("5 *" ,n , "=" , n)
       else:
              multiplicar(n-1)
              print("5 *", n, "=", 5 * n)
              
n=10 
multiplicar(n)

#Tabla de multiplicaar ascendente

print("Ascendente")

def multiplicar(n):
       if( n <= 1):
              print("5 *" ,n , "=" , n)
              n = n*1
       else:
              print("5 *", n, "=", 5 * n)
              multiplicar(n-1)

              


n=10 
multiplicar(n)
                    