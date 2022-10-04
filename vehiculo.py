import pickle
from pickle import *

class Vehiculo:

    def __init__(self, color, rueda, puerta):
        self.color = color


    def __str__(self):
        return f"""
        Vehiculo
        Color: {self.color}


vehiculo = Vehiculo("Negro", 4, 4)
print(vehiculo)

file = open('vehiculo.json', 'wb')

pickle.dump(vehiculo, file, protocol=pickle.HIGHEST_PROTOCOL)
file.close()

file = open('vehiculo.json', 'rb')
load_vehiculo = pickle.load(file)
print(load_vehiculo)
