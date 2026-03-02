import os

class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None

class Lista:
    def __init__(self):
        self.head = None
        self.size_count = 0

    def add(self, value):
        newNode = Nodo(value)
        if self.head == None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode
        self.size_count += 1

    def insertAt(self, value, posicion):
        if posicion < 0 or posicion > self.size_count:
            print("Posicion invalida")
            return
        
        newNode = Nodo(value)
        if posicion == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            currentNode = self.head
            for i in range(posicion - 1):
                currentNode = currentNode.next
            newNode.next = currentNode.next
            currentNode.next = newNode
        self.size_count += 1

    def removeValue(self, value):
        if self.head == None:
            print("Lista vacia")
            return

        if self.head.value == value:
            self.head = self.head.next
            self.size_count -= 1
            return

        currentNode = self.head
        while currentNode.next:
            if currentNode.next.value == value:
                currentNode.next = currentNode.next.next
                self.size_count -= 1
                return
            currentNode = currentNode.next
        print("Valor no encontrado")

    def removePosition(self, posicion):
        if posicion < 0 or posicion >= self.size_count:
            print("Posicion invalida")
            return

        if posicion == 0:
            self.head = self.head.next
        else:
            currentNode = self.head
            for i in range(posicion - 1):
                currentNode = currentNode.next
            currentNode.next = currentNode.next.next
        self.size_count -= 1

    def size(self):
        print("Tamaño: ", self.size_count)

    def show(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" --> ")
            currentNode = currentNode.next
        print("Null")

    def isEmpty(self):
        if self.head == None:
            print("¿La lista esta vacia? ", True)
        else:
            print("¿La lista esta vacia? ", False)

def main():
    myList = Lista()
    myList.add("Olivia")
    myList.add("Chikis")
    myList.insertAt("Vaquita", 1)
    myList.show()
    myList.removeValue("Olivia")
    myList.show()
    myList.removePosition(1)
    myList.show()
    myList.size()
    myList.isEmpty()

if __name__ == "__main__":
    os.system('clear' if os.name == 'posix' else 'cls')
    main()