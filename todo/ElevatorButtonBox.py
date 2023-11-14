#! /usr/bin/python3

import ElevatorButton


class ElevatorButtonBox:
    """Botonera para ascensores. interior o exterior"""

    def __init__(self, listaLabels):
        self.box = []
        for label in listaLabels:
            self.box.append(ElevatorButton(label))

    def __str__(self):
        pass

if __name__ == "__main__":

    labels = ["SUB","BAJ"]
    ElevatorButtonBox(labels)
    
    ebU = ElevatorButton("UP")
    ebD = ElevatorButton("DOWN")

    wallButonBoxLabels = ["",""]

    wallButonBox.append(ebU)
    wallButonBox.append(ebD)

    cabinButtonBox = []
    cabinButtonBox.append(ElevatorButton("1"))
    cabinButtonBox.append(ElevatorButton("2"))
    cabinButtonBox.append(ElevatorButton("3"))
