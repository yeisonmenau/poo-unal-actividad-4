class Notas ():
    def __init__(self, lista_notas: list[int]):
        self.lista_notas = lista_notas
        
    def calcular_promedio(self) -> float:
        suma = 0
        if len(self.lista_notas) <= 0:
            return suma
        else:
            for i in self.lista_notas:
                suma += i
            return suma / 5
    
    def calcular_desviacion(self) -> float:
        prom = self.calcular_promedio()
        suma = 0
        for i in self.lista_notas:
            suma += (i - prom) ** 2
        return (suma / 5) ** 0.5
    
    def calcular_menor(self) -> float:
        menor = self.lista_notas[0]
        for i in self.lista_notas:
            if i < menor:
                menor = i
        return menor
    
    def calcular_mayor(self) -> float:
        mayor = self.lista_notas[0]
        for i in self.lista_notas:
            if i > mayor:
                mayor = i
        return mayor

        