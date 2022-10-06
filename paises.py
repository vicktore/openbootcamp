
paises=input("Digite el nombre del paises separados por coma:")

set_paises=[pais for pais in paises.split(",")]


print(sorted((set_paises)))