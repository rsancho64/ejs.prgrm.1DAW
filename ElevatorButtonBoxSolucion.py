from ElevatorButton import ElevatorButton

class ElevatorButtonBOX:

    def __init__(self, tamMax=30) -> None:
        self.capacity = tamMax
        self.lista = []  # None] * tam

    def __str__(self) -> str:
        respuesta = "BX: ["
        for i in range(len(self.lista)):
            respuesta += str(self.lista[i])
        respuesta += "]"
        return respuesta

    def add(self, aButton) -> bool:
        if len(self.lista) < self.capacity:
            self.lista.append(aButton)
            return True
        return False

if __name__ == "__main__":

    bbxWall = ElevatorButtonBOX(2)
    print(bbxWall)

    bbxWall.add(ElevatorButton("UP"))
    print(bbxWall)

    bbxWall.add(ElevatorButton("DOWN"))
    print(bbxWall)

    if not bbxWall.add(ElevatorButton("666")):
        print("bbxWall: button NOT added!!")

    print(bbxWall)

    bbxCabin = ElevatorButtonBOX()
    print(f"capacidad: {bbxCabin.capacity}")
    bbxCabin.add(ElevatorButton("-1"))
    bbxCabin.add(ElevatorButton("calle"))
    bbxCabin.add(ElevatorButton("1"))
    bbxCabin.add(ElevatorButton("2"))
    bbxCabin.add(ElevatorButton("3"))
    bbxCabin.add(ElevatorButton("4"))

    print(bbxCabin)
