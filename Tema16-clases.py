import os
class Operasbas():
    # Propiedades de clase
    num1 = 0
    num2 = 0
    res = 0

    # Contructor de la clase
    def __init__(self):
        self.num1=0
        self.num2=0

    def suma(self):
        self.res=self.num1+self.num2

def main():
    os.system('cls')
    obj = Operasbas()
    obj.suma()
    print("La suma es: {} ".format(obj.res))

if __name__=='__main__':
    main()

    # Metodos de clase

