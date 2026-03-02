import os

class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None

class Cola:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size_count = 0

    def queue(self, value):
        newNode = Nodo(value)
        if self.head == None:
           self.head = newNode
           self.tail = newNode
        else:   
            self.tail.next = newNode
            self.tail = newNode
        self.size_count += 1

    def dequeue(self):
        if self.head is None:
            print("La cola está vacía")
            return None
        valor = self.head.value
        self.head = self.head.next 
        if self.head is None: 
            self.tail = None
        self.size_count -= 1
        return valor

    def show(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" --> ")
            currentNode = currentNode.next    
        print("Null")   

    def peek(self):
        if self.head is None:
            print("No hay nada que mostrar")
            return None    
        print("Valor cola: ", self.head.value)

    def size(self):
        print("Tamaño: ", self.size_count)

    def isEmpty(self):
        if self.head == None:
            print("¿La cola esta vacia? ", True)
        else:
            print("¿La cola esta vacia? ", False)            

    def find(self, value):
        currentNode = self.head
        posicion = 0
        while currentNode:
            if currentNode.value == value:
                print(value, posicion)
                return True  
            currentNode = currentNode.next
            posicion += 1
        print("Null")
        return False    

def main():
    myFamily = Cola()
    myFamily.queue("Olivia")
    myFamily.queue("Olivia")
    myFamily.queue("Chikis")
    myFamily.queue("chuatito")
    myFamily.queue("vaquita")
    myFamily.queue("choncho")
    myFamily.show()
    myFamily.dequeue()
    myFamily.show()    
    myFamily.find("Chikis")
    myFamily.isEmpty()
    myFamily.peek()
    myFamily.size()
    myFamily.show()
    myFamily.dequeue()
    myFamily.show()

if __name__ == "__main__":
    os.system('clear' if os.name == 'posix' else 'cls')
    main()