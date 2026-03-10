import os

class Nodo:
    def __init__(self, valor): 
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.top = None 
        self.size = 0

    def push(self, valor):
        nuevoNodo = Nodo(valor)
        nuevoNodo.siguiente = self.top
        self.top = nuevoNodo
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        valor_extraido = self.top.valor
        self.top = self.top.siguiente
        self.size -= 1
        return valor_extraido 

    def show(self):
        currentNode = self.top
        print("Estado de la Pila: ", end="")
        while currentNode:
            print(f"[{currentNode.valor}]", end=" -> ")
            currentNode = currentNode.siguiente
        print("NULL")

# --- FUNCIÓN DE EVALUACIÓN (Basada en tu algoritmo) ---
def evaluar_postfix(vector_p):
    pila_numeros = Pila()
    
    # 1. Agregar ")" al final como centinela
    vector_p.append(")")
    
    # 2. Escanear P hasta encontrar ")"
    for elemento in vector_p:
        if elemento == ")":
            break
            
        # 3. Si es un operando (número), push a la Stack
        if isinstance(elemento, (int, float)):
            pila_numeros.push(elemento)
            
        # 4. Si es un operador (+, -, *, /)
        else:
            # a) B = pop, A = pop
            b = pila_numeros.pop()
            a = pila_numeros.pop()
            
            # b) C = A operador B
            if elemento == "+": c = a + b
            elif elemento == "-": c = a - b
            elif elemento == "*": c = a * b
            elif elemento == "/": c = a / b
            
            # c) push(C) a la Stack
            pila_numeros.push(c)
            
    # Devolver el resultado final
    return pila_numeros.pop()

def main():
    # Ejemplo de prueba: (10 + 5) * 2  => [10, 5, "+", 2, "*"]
    expresion = [10, 5, "+", 2, "*"]
    
    print("Evaluando expresión Postfix:", expresion)
    print("-" * 30)
    
    resultado = evaluar_postfix(expresion)
    
    print("-" * 30)
    print(f"RESULTADO FINAL: {resultado}")

if __name__ == "__main__":
    # Limpiar pantalla según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')
    main()