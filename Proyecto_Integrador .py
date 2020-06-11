#Juan Carlos Jiménez Tapia       A01750115
##
import random as r

class Usuario:
    '''Esta clase permite al usuario ingresar sus datos (nombre, destino y aerolinea) para comprar un
    boleto, también tiene una función para asignar asientos y para imprimir el pase de abordar.'''
    
    def __init__(self, nombre, destino, aerolinea, peso):
        '''Esta función, al igual que en las otras clases, podríamos decir que reparte los diferentes
        valores a los atributos del objeto.'''
        self.__nombre = nombre
        self.__destino = destino
        self.__aerolinea = aerolinea
        self.__vuelos = {}
        self.__asiento = 0
        self.__equipaje = peso
        
    @property
    def asiento(self):
        '''Gracias a esta @property, podemos acceder a este atributo ya que es privado. Lo mismo
        pasa en las otras clases.'''
        return self.__asiento
        
    def escoger_vuelo(self, vuelos):
        '''Esta función permite al usuario ver si hay un vuelo disponible de acuerdo a su destino y
        aerolinea.'''
        if (self.__destino == vuelos.destino) and (self.__aerolinea == vuelos.aerolinea): 
            print('Este vuelo esta disponible: \n', vuelos)
            self.__vuelos[vuelos] = vuelos
        else:
            print('No hay vuelos disponibles.')
            
    def asientos(self):
        '''Aquí le damos un número de asiento al azar al usuario del 1 al 60.'''
        self.__asiento = r.randrange(0,61)
        return self.__asiento
    
    def imprimir_pase(self, aeropuerto, vuelo):
        '''Con este método podemos imprimir los datos del vuelo y del usuario con formato de un pase
        de abordar.'''
        print(f'Pase de Abordar | {self.__nombre}')
        for v in self.__vuelos:
            print(v)
            print(f'Asiento: {self.asientos()}           Puerta: {aeropuerto.puerta}           Terminal: {aeropuerto.term(v1)}           Peso Maleta:{self.__equipaje}')
            
    def __str__(self):
        '''Aquí se le da formato a los datos del usuario.'''
        return f'Nombre: {self.__nombre} - Destino: {self.__destino} - Aerolinea: {self.__aerolinea}'
        
class Vuelos:
    '''En esta clase creamos los diferentes vuelos que el usuario puede encontrar.'''
    
    num_vuelo = 1
    
    def __init__(self, destino, aerolinea, horario):
        self.__destino = destino
        self.__aerolinea = aerolinea
        self.__horario = horario
        self.__num_vuelo = Vuelos.num_vuelo
        Vuelos.num_vuelo += 1

        
    @property
    def destino(self):
        return self.__destino
    
    @property
    def aerolinea(self): 
        return self.__aerolinea
    
    @property
    def horario(self):
        return self.__horario
    
    def __str__(self):
        '''Este método le la formato al objeto (al vuelo) para cada vez que tenga que ser mostrado'''
        return f'Número de Vuelo: {self.__num_vuelo} * Origen: CDMX * Destino: {self.__destino} * Aerolinea: {self.__aerolinea} * Horario: {self.__horario}'
    
     
class Aeropuerto:
    '''La asignación de puertas y terminales se encuentra dentro de esta clase,recibe el dato
    de la puerta por medio de un randrange inportado del modulo 'random'.'''


    def __init__(self, puerta):
        self.__puerta = puerta
        self.__terminal = 0
        self.__vuelos = {}
        
    @property
    def puerta(self):
        return self.__puerta
    
    @property
    def terminal(self):
        return self.__terminal
    
    def term(self, vuelo):
        '''Aquí determinamos si el vuelo saldrá de la terminal 1 o 2, dependiendo si el destino se
        encuentra en la lista de los detinos t1 (estados de la República, nacionales).'''
        t1 = ['Aguascalientes', 'Baja California', 'Baja California Sur', 'Chiapas', 'Campeche', 'Chihuahua', 'Coahuila', 'Colima', 'Durango', 'Guanajuato', \
              'Hidalgo', 'Jalisco', 'Michoacan', 'Morelos', 'Nayarit', 'Nuevo Leon', 'Oaxaca', 'Puebla', 'Queretaro', 'Quntana Roo', 'San Luis Potosi', 'Sinaloa', \
              'Sonora', 'Tabasco', 'Tamaulipas', 'Veracruz', 'Yucatán', 'Zacatecas']
        
        if vuelo.destino in t1:
            self.__terminal = 1
        else:
            self.__terminal = 2
        return self.__terminal
       
    
    def agregar_vuelo(self, vuelo):
        ''' Aquí se recibe un vuelo y se agrega a un diccionario para que se mantenga un registro
        de los vuelos en existencia.'''
        self.__vuelos[vuelo] = vuelo
    
    def consultar_vuelos(self):
        '''Este metodo permite al usuario ver en un formato agradable los vuelos para un determinado
        día.'''
        print(f'Vuelos programados para hoy:')
        for v in self.__vuelos:
            print(v)    

class Equipaje:
    def __init__(self, peso):
        self.peso = peso
        
    def peso(self):
        return self.peso
    
    def __str__(self):
        return f'{self.peso} Kg'
    
#--------------------------------------------------------------------------------        
if __name__ == '__main__':
    u1 = Usuario('Brenda Vega', 'Chiapas', 'Aeromexico', Equipaje(20))
    u2 = Usuario('Juan Carlos', 'Durango', 'Volaris', Equipaje(20))
    v1 = Vuelos('Chiapas', 'Aeromexico', '3:10')
    v2 = Vuelos('Durango', 'Volaris', '3:30')
    a1 = Aeropuerto(r.randrange(11))
    a1.agregar_vuelo(v1)
    a1.agregar_vuelo(v2)
    print(u2)
    u1.escoger_vuelo(v1)
    print()
    print(u1)
    u1.escoger_vuelo(v2)
    print()
    u1.imprimir_pase(a1, v2)
    print()
    print(v2)
     