#Una empresa de alquiler de vehículos necesita un sistema para gestionar sus reservas.

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, placa, modelo, precio_dia, estado):
        super().__init__()
        self.marca = marca
        self.placa = placa
        self.modelo = modelo
        self.precio_dia = precio_dia
        self.estado = estado
        
    @abstractmethod
    def calcular_costo(self, dia: int) -> float:
        pass
    
    @abstractmethod
    def mostrar_detalles(self):
        pass
    
    
class Automovil(Vehiculo):
    def __init__(self, marca, placa, modelo, precio_dia, estado, puertas, capacidad):
        super().__init__(marca, placa, modelo, precio_dia, estado)
        self.puertas = puertas
        self.capacidad = capacidad
        
    def calcular_costo(self, dia: int) -> float:
        if dia <= 0 or self.precio_dia <=0:
            print("Debe ingresar el valor correcto de los dias y el precio por dia")  
            return 0
        
        return dia * self.precio_dia
    
    def mostrar_detalles(self):
        return f"Marca: {self.marca}\nPlaca: {self.placa}\nModelo: {self.modelo}\nPrecio *dia: {self.precio_dia}\nEstado: {self.estado}\nPuertas: {self.puertas}\nCapacidad: {self.capacidad}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, placa, modelo, precio_dia, estado, cilindraje):
        super().__init__(marca, placa, modelo, precio_dia, estado)
        self.cilindraje = cilindraje
        
    def calcular_costo(self, dia: int) -> float:
        if dia <= 0 or self.precio_dia <= 0:
           print("Debe ingresar el valor correcto de los dias y el precio por dia")
           return 0
        
        return self.precio_dia * dia
    
    def mostrar_detalles(self):
        return f"Marca: {self.marca}\nPlaca: {self.placa}\nModelo: {self.modelo}\nPrecio *dia: {self.precio_dia}\nEstado: {self.estado}\nCilindraje: {self.cilindraje}"
               
class Camioneta(Vehiculo):
    def __init__(self, marca, placa, modelo, precio_dia, estado, carga):
        super().__init__(marca, placa, modelo, precio_dia, estado)
        self.carga = carga
        
    def calcular_costo(self, dia: int) -> float:
        if dia <= 0 or self.precio_dia <= 0:
            print("Debe ingresar el valor correcto de los dias o el precio")
            return 0
        return self.precio_dia * dia
        
    def mostrar_detalles(self):
        return f"Marca: {self.marca}\nPlaca: {self.placa}\nModelo: {self.modelo}\nPrecio *dia: {self.precio_dia}\nEstado: {self.estado}\nCarga: {self.carga}"
     
class Reserva:
    def __init__(self, cliente, vehiculo, cantidad_dias):
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.cantidad_dias = cantidad_dias
           
    def validar_reserva(self) -> bool:
        if not self.vehiculo.estado:
            print("El vehiculo no esta disponible")
            return False
        return True
    
    def procesar_reserva(self) -> bool:
        if not self.validar_reserva():
            return False
        
        if self.cantidad_dias <= 0:
            print("El precio debe ser mayor a 0")
            return False
        
        print("Reserva exitosa")
        return True
    
    def calcular_total(self):
        return self.vehiculo.calcular_costo(self.cantidad_dias)
    
class ResultadoReserva:
    def __init__(self, reserva, valor_total):
        self.reserva = reserva
        self.valor_total = valor_total
        
    def mostrar_reserva(self):
        if not self.reserva.vehiculo.estado:
            return
        print("=====================")
        print("Resultado de reserva")
        print("=====================")
        print(f"Cliente: {self.reserva.cliente}\n{self.reserva.vehiculo.mostrar_detalles()}\nDias aquilado: {self.reserva.cantidad_dias}\nTotal valor dia: {self.valor_total}")
        self.reserva.vehiculo.estado = False
        

auto1 = Automovil("Audi 30", 989, "2009", 2300, True, "4 puertas", 4)
camioneta = Camioneta("Toyota TX", 888, "2020",5500, True, "2 toneladas")
moto = Motocicleta("Yamaha", 123,"2010", 3200, False, "200cc"  )

reserva1 = Reserva("Duvan",auto1, 6)
reserva2 = Reserva("Pablo",camioneta, 8)
reserva3 = Reserva("Alexander", moto, 5)

reserva1.procesar_reserva()
resultado_reserva = ResultadoReserva(reserva1, reserva1.calcular_total())
resultado_reserva.mostrar_reserva()

reserva2.procesar_reserva()
resultado_reserva = ResultadoReserva(reserva2, reserva2.calcular_total())
resultado_reserva.mostrar_reserva()

reserva3.procesar_reserva()
resultado_reserva = ResultadoReserva(reserva3, reserva3.calcular_total())
resultado_reserva.mostrar_reserva()



