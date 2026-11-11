from abc import ABC, abstractmethod


class CuentaBancaria(ABC):
    def __init__(self, titular, cuenta, saldo):
        super().__init__()
        self.titular = titular
        self._cuenta = cuenta
        self._saldo = saldo
        
    @abstractmethod 
    def calcular_interes(self):
        pass
    
    def retirar(self, monto):
        if monto <= 0:
            print("No se permite retiros en 0 o inferiores")
            return
        
        if self._saldo <= 0:
            print("Fondos insuficientes")
            return
        
        self._saldo -= monto
        
        print("Retiro exitoso ")
        print(f"Retiro realizado: {monto}")
        print("")
        
    def depositar(self, monto):
        if monto <= 0:
            print("No se permiten montos en 0 o un valor inferior.")
            return
        
        self._saldo += monto
        
        print("Deposito exitoso...")
        print(f"Monto depositado: {monto}")
        print("")
        
    def consultar_saldo(self):
        return self._saldo
    
    def __str__(self) -> str:
        return f"Titular: {self.titular}\nCuenta: {self._cuenta}\nSaldo: {self._saldo}"

class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, cuenta, saldo, interes_cuenta):
        super().__init__(titular, cuenta, saldo)
        self.interes_cuenta = interes_cuenta
        
    def calcular_interes(self):
        if self._saldo <= 0:
            print("No se puede calcular interes a un saldo 0 o negativo")
            return
        interes = self._saldo * self.interes_cuenta / 100
        print(f"Intereses: {interes}")
        return interes
    
    def retirar(self, monto):
        return super().retirar(monto)
        

    def depositar(self, monto):
        super().depositar(monto)
    
    def consultar_saldo(self):
        return f"Saldo disponible: {super().consultar_saldo()}"
    
    def __str__(self) -> str:
        return f"{super().__str__()}\nInteres: {self.interes_cuenta}"
    
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, cuenta, saldo, intereses, sobregiro):
        super().__init__(titular, cuenta, saldo)
        self.intereses = intereses
        self.sobregiro = sobregiro
        
    def calcular_interes(self):
        interes = self._saldo * self.intereses / 100
        print(f"Intereses: {interes}")
        return interes
    
    def retirar(self, monto):
        if self._saldo <= 0:
            print("Fondos insuficientes")
            return
        
        if monto <= 0:
            print("El monto de retiro es invalido")
            return
        
        total_sobregiro = self._saldo + self.sobregiro
        if monto > total_sobregiro:
            print("Transaccion rechazada")
            return
        
        self._saldo = self._saldo - monto
        print("Retiro exitoso")
        print(f"Monto retiro: {monto}")
        
    def depositar(self, monto):
        return super().depositar(monto)
    
    def consultar_saldo(self):
        return f"Saldo disponible: {super().consultar_saldo()}"
    
    def __str__(self) -> str:
        return f"{super().__str__()}\nInteres: {self.intereses}\nSobregiro: {self.sobregiro}"

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_cuentas = []    
    
    def guardar_cuenta(self, **kwargs):
        if not kwargs:
            print("No se puede registrar esta cuenta")
            return
        
        if kwargs in self.lista_cuentas:
            print("Esta cuenta ya existe")
            return
        
        self.lista_cuentas.append(kwargs)
        print("Cuenta guardada exitosamente..")
        
    def buscar_cuenta(self, cuenta):
            validar = next((c[str(cuenta)] for c in self.lista_cuentas if str(cuenta) in c), None)
            if validar:
                print("Si exiete esta cuenta")
            else:
                print("Esta cuenta no existe")
            
    def listar_cuenta(self):
        if not self.lista_cuentas:
            print("No hay cuentas registradas")
            return
        for cuenta in self.lista_cuentas:
            print("==================")
            for valor in cuenta.values():
                print(valor)
                print("=================")

cuenta1 = CuentaAhorros("Duvan", 12345,  200000, 2)
cuenta1.depositar(5000)
cuenta1.retirar(1000)
cuenta1.calcular_interes()
print(cuenta1.consultar_saldo())

cuenta2 = CuentaCorriente("Alex", 3456, 200000, 5, 50000)
cuenta2.depositar(50000)
cuenta2.retirar(300000)
cuenta2.calcular_interes()
print(cuenta2.consultar_saldo())

banco = Banco("Bancolombia")
banco.guardar_cuenta(**{str(cuenta1._cuenta): cuenta1, str(cuenta2._cuenta): cuenta2})
banco.buscar_cuenta(1234)