##modulo time

import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print("hora de ir a casa")
else:
<<<<<<< HEAD
    print(f"faltan  {18 - int(hora)} horas y {59 - int(minutos)} minutos")
=======
    print(f"faltan  {18 - int(hora)} horas y {59 - int(minutos)} minutos")
>>>>>>> 60da5a7b543532f288b32bb6cb607923a37bf6d3
