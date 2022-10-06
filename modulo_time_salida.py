##modulo time

import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print("hora de ir a casa")
else:
    print(f"faltan  {18 - int(hora)} horas y {59 - int(minutos)} minutos")