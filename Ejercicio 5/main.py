#Función que pueda decirme si un año es bisiesto o no

year = 2022 #año a comprobar

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Es bisiesto")

else:
    print("No es bisiesto")