import os

class pan:
    def __init__(self, harina, manteca, levadura, azucar) -> None:
        self.harina = harina
        self.manteca = manteca
        self.levadura = levadura
        self.azucar = azucar

    def mesclar_ingredientes(self): #self, ,mesclar?
        os.system("clear")
        print("<-----------Masa lista para comenzar a hacer pan------------>")
        print('''
                          ___
                       .-"   "-.
                     .'   . ;   `.
                    /    : . ' :  \
                   |   `  .-. . '  |
                   |  :  (   ) ; ` |
                   |   :  `-'   :  |
                    \   .` ;  :   /
                     `.   . '   .'
                       `-.___.-'
        ''')

class pan_dulce(pan):
    def __init__(self, harina, manteca, levadura, azucar, colorante, vainilla) -> None:
        super().__init__(harina, manteca, levadura, azucar)
        self.colorante = colorante
        self.vainilla = vainilla

class pan_de_sal(pan):
    def __init__(self, harina, manteca, levadura, azucar, sal) -> None:
        super().__init__(harina, manteca, levadura, azucar)
        self.sal = sal

if __name__ == '__main__':
    menu = int(input(''' 
----------------------------------
|       Estas listo para         |
|   comenzar a preparar pan?     |
----------------------------------

Elige que tipo de masa deseas preparar

1-Pan dulce
2-Pan de sal

Escoge una opcion: '''))
    if menu == 1:
        print('''
        ------------------------------------------------
        | Recuerda que las cantidades son en gramos    |
        | La vainilla y el colorante son en cucharadas |
        ------------------------------------------------
        ''')
        har = input('cuanta harina deseas agregar?')
        man = input('cuanta manteca deseas agregar?')
        lev = input('cuanta levadura deseas agregar?')
        azu = input('cuanta azucar deseas agregar?')
        col = input('cuanto colorante deseas agregar?')
        vai = input('cuanta vainilla deseas agregar?')
        concha = pan_dulce(har, man, lev, azu, col, vai)
        concha.mesclar_ingredientes()
        #print(vars(concha))
    if menu == 2:
        print('''
        ---------------------------------------------
        | Recuerda que las cantidades son en gramos |
        |          La sal es en cucharadas          |
        ---------------------------------------------
        ''')
        har = input('cuanta harina deseas agregar?')
        man = input('cuanta manteca deseas agregar?')
        lev = input('cuanta levadura deseas agregar?')
        azu = input('cuanta azucar deseas agregar?')
        sal = input('cuanta sal deseas agregar?')
        telera = pan_de_sal(har, man, lev, azu, sal)
        telera.mesclar_ingredientes()
        #print(vars(telera))