#<------------practicando decomposicion------------>

class refrigerador:
    def __init__(self, marca, modelo, capacidad) -> None:
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad
        self._temperatura = enfriado(motor='off', tipo='trifasico')
    
    def activar_motor(self, grados):
        if grados > 10:
            self._temperatura.cojelar('on')
        else:
            self._temperatura.cojelar('off')

class enfriado:
    def __init__(self, motor, tipo) -> None:
        self.motor = motor
        self.tipo = tipo


    def cojelar(self, estado):
        print(estado)

if __name__ == '__main__':
    refri = refrigerador('tororey', 'dak34', 300)
    refri.activar_motor(3)