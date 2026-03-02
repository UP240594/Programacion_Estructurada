import os

class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None

class Lista:
    def __init__(self):
        self.head = None
        self.size_count = 0
    # Add sin el sort, inserta pero no ordena

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

    # 1. ADD SORT: Inserta y ordena al mismo tiempo
    def addSort(self, value):
        newNode = Nodo(value)
        # Si la lista esta vacia o el valor es el mas chico, va al principio
        if self.head == None or value <= self.head.value:
            newNode.next = self.head
            self.head = newNode
        else:
            # Buscamos su lugar en medio o al final
            curr = self.head
            while curr.next != None and curr.next.value < value:
                curr = curr.next
            
            newNode.next = curr.next
            curr.next = newNode
        self.size_count += 1

    # 2. SORT: Ordenar (Usaremos un metodo sencillo de seleccion, no es burbuja)
    def sort(self):
        if self.head == None: return

        curr = self.head
        while curr:
            minimo = curr
            apuntador = curr.next
            while apuntador:
                if apuntador.value < minimo.value:
                    minimo = apuntador
                apuntador = apuntador.next
            
            # Intercambiamos los valores
            aux = curr.value
            curr.value = minimo.value
            minimo.value = aux
            curr = curr.next
        print("Lista ordenada")

    # 3. SEEK: Busqueda binaria
    def seek(self, value):
        inicio = 0
        fin = self.size_count - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            
            # Para llegar al medio en una lista, hay que caminar desde el head
            curr = self.head
            for i in range(medio):
                curr = curr.next
            
            if curr.value == value:
                print(f"Encontrado {value} en la posicion {medio}")
                return True
            elif curr.value < value:
                inicio = medio + 1
            else:
                fin = medio - 1
        
        print("No se encontro")
        return False

    def show(self):
        curr = self.head
        while curr:
            print(curr.value, end=" --> ")
            curr = curr.next
        print("Null")

def main():
    myList = Lista()
    myList2 = Lista()
    
    myList.addSort(30)
    myList.addSort(10)
    myList.addSort(20)
    print("Lista con AddSort:")
    myList.show()

    myList.seek(20)

   
  
    myList2.add(30)
    myList2.add(10)
    myList2.add(20)
    print("Lista con solo Add:")
    myList2.show()
    myList2.sort()
    myList2.show()
    

if __name__ == "__main__":
    os.system('clear' if os.name == 'posix' else 'cls')
    main()