import os
import csv
from datetime import datetime
from graphviz import Digraph


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y

def insert(node, data):
    if not node:
        return TreeNode(data)
    
    if data[1] < node.data[1]:
        node.left = insert(node.left, data)
    elif data[1] > node.data[1]:
        node.right = insert(node.right, data)
    else:
        return node

    node.height = 1 + max(get_height(node.left), get_height(node.right))
    balance = get_balance(node)

    if balance > 1 and data[1] < node.left.data[1]:
        return rotate_right(node)
    if balance < -1 and data[1] > node.right.data[1]:
        return rotate_left(node)
    if balance > 1 and data[1] > node.left.data[1]:
        node.left = rotate_left(node.left)
        return rotate_right(node)
    if balance < -1 and data[1] < node.right.data[1]:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def show(nodo_actual, prefix="", is_left=True):
    if nodo_actual:
        show(nodo_actual.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(nodo_actual.data[1]))
        show(nodo_actual.left, prefix + ("    " if is_left else "│   "), True)

def tree_graphviz(nodo, dot=None):
    if dot is None:
        dot = Digraph()
        dot.attr('node', shape='record', style='filled', fillcolor='lightblue')

    if nodo:
        nodo_label = f"ID: {nodo.data[0]} | {nodo.data[1]}"
        dot.node(str(id(nodo)), nodo_label)
        if nodo.left:
            dot.edge(str(id(nodo)), str(id(nodo.left)))
            tree_graphviz(nodo.left, dot)
        if nodo.right:
            dot.edge(str(id(nodo)), str(id(nodo.right)))
            tree_graphviz(nodo.right, dot)
    return dot

def main():
    raiz = None
    ciudades = []
    
    with open('u3/ciudades.csv', 'r', encoding='latin-1') as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            idC = int(fila['IdCiudad'])
            abr = fila['Abr']
            fec = datetime.strptime(fila['Inicio'], '%Y-%m-%d').date()
            datos = (idC, abr, fec, fec.year)
            ciudades.append(datos)
            raiz = insert(raiz, datos)

    print("Ciudades:", [c[1] for c in ciudades])
    show(raiz)
    
    dot = tree_graphviz(raiz)
    dot.render("arbol_final", format="png", view=True)

if __name__ == "__main__":
    main()