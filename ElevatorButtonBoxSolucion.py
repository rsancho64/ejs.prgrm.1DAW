import ElevatorButton

class ElevatorButtonBOX:

    def __init__(self, tamMax) -> None:
        self.capacity = tamMax
        self.lista = []  # None] * tam

    def __str__(self) -> str:
        # respuesta = "BX: ["
        # ## ... ++ cada boton de la lista...
            hace falta un bucle y usar range()
        # respuesta += "]"
        # return respuesta

    def add(self, aButton) -> bool:
        if len(self.lista) < self.capacity:
            self.lista.append(aButton)
            return True
        return False

if __name__ == "__main__":

    ebUP = ElevatorButton("UP")
    ebDOWN = ElevatorButton("DOWN")
    print(ebUP)
    print(ebDOWN)

    # botonera = []
    # botonera.append(ebUP)
    # botonera.append(ebDOWN)

    # print(botonera)

    bbx = ElevatorButtonBOX(2)
    print(bbx)

    bbx.add(ebUP)
    print(bbx)

    bbx.add(ebDOWN)
    print(bbx)

    if not bbx.add(ElevatorButton("666")):
        print("entrada no realizada")
        
    print(bbx)

    # print(bbx)
