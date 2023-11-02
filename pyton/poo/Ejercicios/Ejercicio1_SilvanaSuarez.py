# TI: 1027525528
# Nombre : SilvanaSuarezCarvajal
# Ejercicio_ : Ejercicio1
# Grupo 10 _ Programación orientada a objetos

class Automovil:
    """ Esta clase se usa para definir los estados y el comportamiento de un automóvil"""

    def __init__(self, anio: int, marca: str, tipo: str, color: str, velocidad: float):
        self.anio = anio
        self.marca = marca
        self.tipo = tipo
        self.color = color
        self.velocidad = velocidad
        self.velocidad_inicial = 0

    def arrancar(self):
        if self.velocidad_inicial == 0:
            self.velocidad_inicial += self.velocidad
            texto = f"El carro {self.marca} {self.anio} alcanzó una velocidad de {self.velocidad_inicial}"
        else:
            texto = f"El carro {self.marca} {self.anio} ya se encuentra en movimiento"
        return texto

    def acelerar(self, aceleracion=10):
        if self.velocidad_inicial == 0:
            texto = f"El carro {self.marca} {self.anio} debe arrancar antes de acelerar."
        else:
            self.velocidad = self.velocidad + aceleracion
            texto = f"El carro {self.marca} {self.anio} ahora avanza a una velocidad de {self.velocidad}"

        return texto

    def frenar(self, desaceleracion=10):
        self.velocidad = self.velocidad - desaceleracion
        if self.velocidad <= 0:
            texto = f"El carro {self.marca} {self.anio} se detuvo"
        elif self.velocidad_inicial == 0:
            texto = f"El carro {self.marca} {self.anio } no requiere frenar."
        else:
            texto = f"El carro {self.marca} {self.anio} ahora avanza a una velocidad de {self.velocidad}"

        return texto

    def girar(self, direccion="derecha"):
        direccion = direccion.lower()
        if self.velocidad_inicial == 0:
            texto = f"El carro {self.marca} {self.anio} no puede girar"
        elif ((direccion != "derecha") & (direccion != "izquierda") &
                (direccion != "diagonal derecha") & (direccion != "diagonal izquierda")):
            texto = "Verifique si su carro puede girar hacia la dirección que señaló"
        else:
            texto = f"El carro {self.marca} {self.anio} ahora está girando hacia la {direccion}"
        return texto


auto1 = Automovil(2020, "Toyota", "Sedán", "Azul", 120.5)
auto2 = Automovil(2018, "Ford", "SUV", "Negro", 105.0)
auto3 = Automovil(2015, "Honda", "Compacto", "Rojo", 95.2)
auto4 = Automovil(2022, "Chevrolet", "Camioneta", "Blanco", 130.8)
auto5 = Automovil(2019, "Nissan", "Hatchback", "Plateado", 110.2)


"""Pruebas de código"""

print(auto1.acelerar())
# El carro Toyota 2020 debe arrancar antes de acelerar.
print(auto2.frenar())
# El carro Ford 2018 no requiere frenar.
print(auto3.arrancar())
# El carro Honda 2015 alcanzó una velocidad de 95.2
print(auto3.acelerar())
# El carro Honda 2015 ahora avanza a una velocidad de 105.2
print(auto3.frenar(15))
# El carro Honda 2015 ahora avanza a una velocidad de 90.2

print(auto4.arrancar())
# El carro Chevrolet 2022 alcanzó una velocidad de 130.8
print(auto4.acelerar(35))
# El carro Chevrolet 2022 ahora avanza a una velocidad de 165.8
print(auto4.frenar())
# El carro Chevrolet 2022 ahora avanza a una velocidad de 155.8
print(auto4.frenar(200))
# El carro Chevrolet 2022 se detuvo

print(auto5.girar())
# El carro Nissan 2019 no puede girar
auto5.arrancar()
print(auto5.girar("atrás"))
# Verifique si su carro puede girar hacia la dirección que señaló
print(auto5.girar("IZquIErdA"))
# El carro Nissan 2019 ahora está girando hacia la izquierda
print(auto5.girar())
# El carro Nissan 2019 ahora está girando hacia la derecha
