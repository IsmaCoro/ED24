class Node:
    """
    Clase para representar un nodo en la cola doblemente circular.
    Cada nodo tiene un valor de datos y punteros al nodo anterior y al siguiente.
    """
    def __init__(self, data):
        """Inicializa un nodo con el valor de datos especificado."""
        self.data = data
        self.prev = None  # Puntero al nodo anterior
        self.next = None  # Puntero al nodo siguiente


class CircularDoubleEndedQueue:
    """
    Clase para representar una cola doblemente circular.
    Esta estructura de datos permite añadir y eliminar elementos tanto al frente como al final de la cola.
    """
    def __init__(self):
        """Inicializa una cola doblemente circular vacía."""
        self.head = None  # Puntero al primer nodo de la cola
        self.tail = None  # Puntero al último nodo de la cola

    def is_empty(self):
        """Verifica si la cola está vacía."""
        return self.head is None

    def add_front(self, data):
        """
        Añade un elemento al frente de la cola.
        Se crea un nuevo nodo con el dato especificado y se coloca al frente de la cola.
        """
        new_node = Node(data)
        if self.is_empty():
            # Si la cola está vacía, el nuevo nodo es el único en la cola
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # Si la cola no está vacía, se actualizan los punteros del nuevo nodo y de los nodos existentes
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node  # Se actualiza el puntero al primer nodo
        print(f"Se añadió el elemento {data} al frente")  # Se imprime un mensaje
        self.display()  # Se muestra la cola actualizada

    def add_rear(self, data):
        """
        Añade un elemento al final de la cola.
        Se crea un nuevo nodo con el dato especificado y se coloca al final de la cola.
        """
        new_node = Node(data)
        if self.is_empty():
            # Si la cola está vacía, el nuevo nodo es el único en la cola
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # Si la cola no está vacía, se actualizan los punteros del nuevo nodo y de los nodos existentes
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.tail = new_node  # Se actualiza el puntero al último nodo
        print(f"Se añadió el elemento {data} al final")  # Se imprime un mensaje
        self.display()  # Se muestra la cola actualizada

    def remove_front(self):
        """
        Elimina un elemento del frente de la cola y lo devuelve.
        Si la cola está vacía, se imprime un mensaje de error y se devuelve None.
        """
        if self.is_empty():
            print("La cola está vacía")
            return None
        data = self.head.data  # Se guarda el dato del nodo a eliminar
        if self.head == self.tail:
            # Si hay un solo nodo en la cola, se eliminan los punteros de la cola
            self.head = None
            self.tail = None
        else:
            # Si hay más de un nodo en la cola, se actualizan los punteros de los nodos restantes
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        print(f"Se eliminó el elemento {data} del frente")  # Se imprime un mensaje
        self.display()  # Se muestra la cola actualizada
        return data

    def remove_rear(self):
        """
        Elimina un elemento del final de la cola y lo devuelve.
        Si la cola está vacía, se imprime un mensaje de error y se devuelve None.
        """
        if self.is_empty():
            print("La cola está vacía")
            return None
        data = self.tail.data  # Se guarda el dato del nodo a eliminar
        if self.head == self.tail:
            # Si hay un solo nodo en la cola, se eliminan los punteros de la cola
            self.head = None
            self.tail = None
        else:
            # Si hay más de un nodo en la cola, se actualizan los punteros de los nodos restantes
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        print(f"Se eliminó el elemento {data} del final")  # Se imprime un mensaje
        self.display()  # Se muestra la cola actualizada
        return data

    def display(self):
        """Muestra los elementos de la cola."""
        if self.is_empty():
            print("La cola está vacía")
            return
        current = self.head
        print("Elementos de la cola:", end=" ")
        while True:
            print(current.data, end=" <--> ")
            current = current.next
            if current == self.head:
                break
        print()


# Ejemplo de uso
cola = CircularDoubleEndedQueue()

while True:
    print("\n1. Añadir al frente")
    print("2. Añadir al final")
    print("3. Eliminar del frente")
    print("4. Eliminar del final")
    print("5. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        dato = input("Introduce el dato a añadir al frente: ")
        cola.add_front(dato)
    elif opcion == 2:
        dato = input("Introduce el dato a añadir al final: ")
        cola.add_rear(dato)
    elif opcion == 3:
        dato = cola.remove_front()
        if dato is not None:
            print("Se eliminó el dato:", dato)
    elif opcion == 4:
        dato = cola.remove_rear()
        if dato is not None:
            print("Se eliminó el dato:", dato)
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
