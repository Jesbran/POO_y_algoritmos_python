from cgi import print_form


class Coordenadas:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff+y_diff)**0.5

if __name__ == '__main__':
    coord_1 = Coordenadas(3,30)
    coord_2 = Coordenadas(4,8)
    print(coord_1.distancia(coord_2))
    print(isinstance(coord_1, Coordenadas))
    print(isinstance("algo", str))#otro ejemplo de su funcionamiento
    '''isinstance comprueba que el primer parametro recibido sea una instacia de el segundo parametro,
    en este caso comprueba que coord_1 sea una instancia de Coordenadas. digamos que comprueba
    que el dato sea de un tipo en especifico'''