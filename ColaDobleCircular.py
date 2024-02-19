class Nodo:
    def __init__(self, valor):
        """
        Inicializa un nuevo nodo con un valor dado.
        """
        self.valor = valor
        self.siguiente = None  # Enlace al siguiente nodo
        self.anterior = None   # Enlace al nodo anterior

class ColaDobleCircular:
    def __init__(self):
        """
        Inicializa una cola doblemente circular vacía.
        """
        self.primero = None  # Referencia al primer nodo
        self.ultimo = None   # Referencia al último nodo

    def esta_vacia(self):
        """
        Verifica si la cola está vacía.
        """
        return self.primero is None

    def insertar_final(self, valor):
        """
        Inserta un elemento al final de la cola.
        """
        nuevo_nodo = Nodo(valor)  # Crea un nuevo nodo con el valor dado
        if self.esta_vacia():
            # Si la cola está vacía, el nuevo nodo es el primero y el último
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            # El siguiente y el anterior del nuevo nodo apuntan a sí mismo para formar un ciclo
            nuevo_nodo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nuevo_nodo
        else:
            # Si la cola no está vacía
            nuevo_nodo.anterior = self.ultimo  # El nodo anterior al nuevo nodo es el último nodo actual
            nuevo_nodo.siguiente = self.primero  # El siguiente al nuevo nodo es el primer nodo actual
            self.ultimo.siguiente = nuevo_nodo  # El siguiente del último nodo apunta al nuevo nodo
            self.primero.anterior = nuevo_nodo  # El anterior del primer nodo apunta al nuevo nodo
            self.ultimo = nuevo_nodo  # El nuevo nodo ahora es el último nodo

    def eliminar_inicio(self):
        """
        Elimina el primer elemento de la cola y devuelve su valor.
        """
        if self.esta_vacia():
            return None  # Si la cola está vacía, no hay nada que eliminar
        valor_eliminado = self.primero.valor  # Guarda el valor del primer nodo
        if self.primero == self.ultimo:
            # Si solo hay un nodo en la cola
            self.primero = None
            self.ultimo = None
        else:
            # Si hay más de un nodo en la cola
            self.primero = self.primero.siguiente  # El siguiente nodo se convierte en el nuevo primero
            self.ultimo.siguiente = self.primero  # El siguiente del último nodo apunta al nuevo primero
            self.primero.anterior = self.ultimo  # El anterior del nuevo primero apunta al último nodo
        return valor_eliminado

    def imprimir(self):
        """
        Imprime el contenido de la cola.
        """
        if self.esta_vacia():
            print("La cola está vacía")
        else:
            nodo_actual = self.primero  # Comienza desde el primer nodo
            while nodo_actual:
                print(nodo_actual.valor, end=" <-> ")  # Imprime el valor del nodo actual
                nodo_actual = nodo_actual.siguiente  # Avanza al siguiente nodo
                if nodo_actual == self.primero:
                    break  # Si hemos vuelto al primer nodo, terminamos el ciclo
            print()  # Imprime una nueva línea al final

# Ejemplo de uso:
cola = ColaDobleCircular()
cola.insertar_final(1)
cola.insertar_final(2)
cola.insertar_final(3)
cola.insertar_final(4)

print("Cola actual:")
cola.imprimir()

print("Eliminando el inicio de la cola...")
cola.eliminar_inicio()

print("Cola después de eliminar el inicio:")
cola.imprimir()
