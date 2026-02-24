import os;
class Nodo:
    def __init__(self,valor): #constructor, sirve para inicializar la clase y traerla a existir
        self.valor = valor
        self.siguiente = None
 # setter y getter realmente no son necesarios   


class Cola:
    def __init__(self):
        self.primero = None #head
        self.ultimo = None #tail
        self.size = 0
        
    def isEmpty(self):
        if self.primero is None:
            return True
        
        else:
            return False
        #return true if self.size == 0 else false  ternario
        # return self.size == 0
        # return not self.primero
    def peek(self): #muestra el primero
        pass
        if self.isEmpty():
            return None
        return self.primero.valor
    
    def enqueue(self,valor):
        pass
        nuevoNodo = Nodo(valor)
        self.size = self.size + 1
        if self.isEmpty():
            self.primero = self.ultimo = nuevoNodo
        else:
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo

    def show(self):
        currentNode = self.primero
        while currentNode:
            print(currentNode.valor , end="-->")
            currentNode=currentNode.siguiente

        print("Null");
        


    

def main ():
        myH = Cola()
        myM = Cola()
        myH.enqueue("Jorge")
        myH.enqueue("Paco")
        myH.enqueue("Adrian")
        print("Direccion de myH: " , myH)
        myH.show()

        myM.enqueue("Mari")
        myM.enqueue("Rosa")
        myM.enqueue("Ana")
        print("Direccion de myM: " , myM)
        myM.show()

        

if __name__ == "__main__":
    os.system('clear')
myH = Cola()
myM = Cola()
main()



    