class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None
    
    def primer_elemento(self):
        if not self.esta_vacia():
            return self.elementos[0]
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def longitud(self):
        return len(self.elementos)