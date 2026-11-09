class Empleado:
    def __init__(self, nombre, documento, salario_base):
        self.nombre = nombre
        self.documento = documento
        self.__salario_base = float(salario_base)
        
        
    def __str__(self):
        return f"Nombre: {self.nombre}\nDocumento: {self.documento}\nSalario base: {self.__salario_base}"
    
    def calcular_salario(self) -> float:
        return self.__salario_base
    
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, documento, salario_base, bonificacion):
        super().__init__(nombre, documento, salario_base)   
        self.bonificacion = bonificacion
        
           
    def calcular_salario(self) -> float:
        return super().calcular_salario() + self.bonificacion   
    
    def __str__(self):
        return f"{super().__str__()}\nSalario total: {self.calcular_salario()}"

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, documento, salario_base, valor_hora, horas_trabajadas):
        super().__init__(nombre, documento, salario_base) 
        self.valor_hora = valor_hora
        self.horas_trabajadas = horas_trabajadas
        
    def calcular_salario(self) -> float:
        return super().calcular_salario() + (self.valor_hora * self.horas_trabajadas)
    
    def __str__(self):
        return f"{super().__str__()}\nSalario total: {self.calcular_salario()}"
    

class GestorEmpleados:
    def __init__(self):
        self.lista_empleados = []
        
    def guardar_empleado(self, nombre, documento, salario, bono=None, valor_hora=None, horas_trabajadas=None):
        if bono is not None and bono > 0:
            emp_tiempo_completo = EmpleadoTiempoCompleto(nombre, documento, salario, bono)
            self.lista_empleados.append(emp_tiempo_completo)
    
        elif horas_trabajadas is not None and horas_trabajadas > 0:
            if valor_hora is not None and valor_hora > 0:
                emp_por_horas = EmpleadoPorHoras(nombre, documento,salario, valor_hora, horas_trabajadas)
                self.lista_empleados.append(emp_por_horas)
        else:
            print("Algunos valores no deben ir vacios ")
    
    def mostrar_informacion(self):
        for emp in self.lista_empleados:
            print("===================")
            print(emp)
            print("===================")
        
class Datos:
    def __init__(self, gestor):
        self.gestor = gestor
    
    def pedir_datos(self):
        
        nombre = input("Ingrese el nombre del empleado: ")
        documento = input("Ingrese el documento: ")
        salario = float(input("Ingrese el salario: "))
        
        validar = int(input("Ingrese 0 para tiempo completo y 1 para trabajadores por horas: "))
        
        if validar == 0:
            bono = float(input("Ingrese el  valor del bono: "))
            
            if bono > 0:
                self.gestor.guardar_empleado(nombre, documento, salario, bono)
            else:
                print("El bono no puede ser menor o igual a 0")
        elif validar == 1:
            
            valor_hora = float(input("Ingrese el valor de la hora: "))
            horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
            
            if valor_hora and horas_trabajadas > 0:
                 self.gestor.guardar_empleado(nombre, documento, salario, valor_hora=valor_hora, horas_trabajadas=horas_trabajadas)
            else:
                print("Debe ingresar las horas trabajadas y el valor de la hora correctamente.")
                
    def mostrar(self):
        self.gestor.mostrar_informacion()

     

 
gestor = GestorEmpleados()
dato = Datos(gestor)
dato.pedir_datos()
dato.mostrar()

        
