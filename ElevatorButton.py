class ElevatorButton:
    """Boton de ascensor. Un pulsador biestable"""

    def __init__(self, label):
        self.estado = "off"
        self.label = label

    def setOff(self):
        self.estado = "off"

    def setOn(self):
        self.estado = "on"

    def toggle(self):
        if self.estado == "on":
            self.estado = "off"
        else:
            self.estado = "on"

    def __str__(self):
        return f"[{self.label}: {self.estado}]"


if __name__ == "__main__":

    eb = ElevatorButton("UP")

    print(eb)  # off

    eb.toggle()
    print(eb)  # on

    eb.setOn()
    print(eb)  # on

    eb.toggle()
    print(eb)  # off
    eb.setOff()
    print(eb)  # off

    # botoneras ... class ElevatorButtonBox ...

    ebU = ElevatorButton("UP")
    ebD = ElevatorButton("DOWN")

    wallButonBox = []
    wallButonBox.append(ebU)
    wallButonBox.append(ebD)

    cabinButtonBox = []
    cabinButtonBox.append(ElevatorButton("1"))
    cabinButtonBox.append(ElevatorButton("2"))
    cabinButtonBox.append(ElevatorButton("3"))
    
