    #Resursividad, que un metodo se llama a si mismo 
def factorialR(n):
        if n <= 1:
            return 1
        else:
            return n * factorialR(n-1)
        

n=4

print(factorialR(n))



    