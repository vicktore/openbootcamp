print("¿Cul es su peso en kilogramos?")
peso = int(input())
print("¿Cul es su estatura?")
estatura = int(input())
print(round((peso/estatura),2))
ind_masa_corporal=round((peso/estatura),2)
print("tus datos son, ",{'peso': peso, 'estatura': estatura, 'ind_masa_corporal': ind_masa_corporal})