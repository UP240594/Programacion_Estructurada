import os;
class Nodo:
    def __init__(self,valor): 
        self.valor = valor
        self.siguiente = None
   


class Pila:
     def __init__(self):
        self.top = None 
        self.size = 0
        


     def push(self,valor):
        nuevoNodo = Nodo(valor)
        nuevoNodo.siguiente = self.top
        self.top = nuevoNodo
        print("Valor del nodo agregado:     " , nuevoNodo.valor)
        self.size += 1
    
     def pop(self):
        if(self.top == None):
             print("No hay valor que mostrar")
             return None
 

        print("         Sacando el valor de la pila....         ")
        print("               ",self.top.valor)
        print("         Valor removido con exito        ")
        self.top = self.top.siguiente
        self.size -= 1

     def peek(self):
        if(self.top == None):
             print("No hay nada que mostrar")
             return None   


        print("Valor Top:  " ,self.top.valor);                   

     def show(self):
        currentNode = self.top
        print("Datos pila: ")
        while currentNode:
             print("     ",currentNode.valor , end="->")
             currentNode=currentNode.siguiente

        print("Null")    

     def isEmpty(self):
        if(self.top == None):
            return print("¿La pila esta vacia? " ,True)

        print("¿La pila esta vacia?  " ,False)    

     def Size(self):
         print("Tamaño de pila  " ,self.size)          


def main ():
        myFamily = Pila()
        myFamily.push("Olivia")
        myFamily.push("chikis")
        myFamily.push("vaquita")
        myFamily.push("cuatito")
        myFamily.show()
        myFamily.isEmpty()
        myFamily.peek()
        myFamily.pop()
        myFamily.Size()
        myFamily.show()
        

if __name__ == "__main__":
    os.system('clear')
myFamily = Pila()
main()



    