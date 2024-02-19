import os
os.system('cls' if os.name == 'nt' else 'clear')

class Node:
    """
    Clase para representar un nodo en la cola doblemente enlazada circular.
    Cada nodo contiene un dato y referencias al siguiente y al anterior nodo.
    """

    def __init__(self, data):
        """
        Inicializa un nuevo nodo con el dato especificado.
        """
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    """
    Clase para representar una cola doblemente enlazada circular.
    """

    def __init__(self):
        """
        Inicializa una nueva cola doblemente enlazada circular.
        """
        self.head = None

    def insert_front(self, data):
        """
        Inserta un elemento al frente de la cola.
        """
        new_node = Node(data)
        if not self.head:
            # Si la lista está vacía, el nuevo nodo será el único nodo en la lista.
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # Si la lista no está vacía, insertamos el nuevo nodo al frente.
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node
        print(f"Elemento {data} insertado al frente\n")
        self.display()

    def insert_rear(self, data):
        """
        Inserta un elemento al final de la cola.
        """
        new_node = Node(data)
        if not self.head:
            # Si la lista está vacía, el nuevo nodo será el único nodo en la lista.
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # Si la lista no está vacía, insertamos el nuevo nodo al final.
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
        print(f"Elemento {data} insertado al final\n")
        self.display()

    def delete_front(self):
        """
        Elimina el elemento al frente de la cola.
        """
        if not self.head:
            # Si la lista está vacía, no se puede eliminar ningún elemento.
            print("La lista está vacía, no se puede eliminar ningún elemento.\n")
            return
        if self.head.next == self.head:
            # Si hay solo un nodo en la lista, lo eliminamos y establecemos la cabeza en None.
            data = self.head.data
            self.head = None
        else:
            # Si hay más de un nodo, eliminamos el nodo al frente.
            data = self.head.data
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next
        print(f"Elemento {data} eliminado del frente\n")
        self.display()

    def delete_rear(self):
        """
        Elimina el elemento al final de la cola.
        """
        if not self.head:
            # Si la lista está vacía, no se puede eliminar ningún elemento.
            print("La lista está vacía, no se puede eliminar ningún elemento.\n")
            return
        if self.head.next == self.head:
            # Si hay solo un nodo en la lista, lo eliminamos y establecemos la cabeza en None.
            data = self.head.data
            self.head = None
        else:
            # Si hay más de un nodo, eliminamos el nodo al final.
            data = self.head.prev.data
            self.head.prev.prev.next = self.head
            self.head.prev = self.head.prev.prev
        print(f"Elemento {data} eliminado del final\n")
        self.display()

    def display(self):
        """
        Muestra los elementos de la cola.
        """
        if not self.head:
            print("La lista está vacía.\n")
            return
        current = self.head
        while True:
            print(current.data, end=", ")  # Imprime una coma entre elementos
            current = current.next
            if current == self.head:
                break
        print()  # Salto de línea al final

# Función para solicitar una opción al usuario
def menu():
    """
    Muestra el menú de opciones.
    """
    print("\n1. Insertar elemento al frente")
    print("2. Insertar elemento al final")
    print("3. Eliminar elemento del frente")
    print("4. Eliminar elemento del final")
    print("5. Salir")

# Código principal
cdll = CircularDoublyLinkedList()

while True:
    menu()
    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        data = input("Ingrese el elemento a insertar al frente:\n")
        cdll.insert_front(data)
    elif opcion == "2":
        data = input("Ingrese el elemento a insertar al final:\n")
        cdll.insert_rear(data)
    elif opcion == "3":
        cdll.delete_front()
    elif opcion == "4":
        cdll.delete_rear()
    elif opcion == "5":
        print("Saliendo del programa...\n")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.\n")
