class congelador:
    def __init__(self):
        pass

    def iniciar(self,estado='apagado'):
        if estado == 'encendido':
            self._encender_motor(input("estado del motor: "))
    
    def _encender_motor(self, motor):
        if motor == 'on':
            self._encender_ventilador(input("estado del ventilador: "))
        else:
            print("El motor no esta funcionando")

    def _encender_ventilador(self, ventilador):
        if ventilador == 'on':
            self._inyectar_gas(input("estado del inyector de gas: "))
        else:
            print("El ventilador no esta funcionando")

    def _inyectar_gas(self, gas):
        if gas == 'on':
            self._activar_termometro(input("estado del termometro: "))
        else:
            print("El sistema de inyectado de gas no esta funcionando")

    def _activar_termometro(self, termometro):
        if termometro == 'on':
            print('todo listo, conjelador funcionando correctamente')
        else:
            print("El termometro no esta funcionando")

if __name__ == '__main__':
    refri = congelador()
    refri.iniciar('encendido')