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

def evaluar_postfix(cadena_p):
    pila_numeros = Pila()
    
    elementos = cadena_p.split()
    elementos.append(")") 
    
    for elemento in elementos:
        if elemento == ")":
            break
            
        if elemento not in "+-*/^":
            pila_numeros.push(float(elemento))
            
        else:
            b = pila_numeros.pop()
            a = pila_numeros.pop() 
            
            if elemento == "+": c = a + b
            elif elemento == "-": c = a - b
            elif elemento == "*": c = a * b
            elif elemento == "/": c = a / b
            elif elemento == "^": c = a ** b 
            
            pila_numeros.push(c)
            
    return pila_numeros.pop()

def main():
    exp1 = "5 6 2 + * 12 4 / -"
    exp2 = "2 2 3 ^ 2 * 6 4 2 - / - 10 - * 2 -"
    
    print("--- EVALUACIÓN DE POSTFIX ---")
    
    res1 = evaluar_postfix(exp1)
    print(f"Expresión 1: {exp1}")
    print(f"Resultado: {res1}") 
    
    print("-" * 30)
    
    res2 = evaluar_postfix(exp2)
    print(f"Expresión 2: {exp2}")
    print(f"Resultado: {res2}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()