minerales_list = []
centinela = False
import Mineral

with open("Taller_1/minerales.txt") as archivo:
    
    lista = archivo.readlines()
    
    for linea in lista:
        i = linea.split("	")
        
        if centinela:
            mineral = Mineral.Mineral(i[0], float(i[1]), i[5], bool(i[2]), i[3], i[4], i[7], i[6])
            minerales_list.append(mineral)
        
        else:
            centinela = True 
        
    archivo.close()

def num_silicatos(lista):

    num = 0
    
    for mineral in lista:
        if mineral.silicato():
            num += 1
    
    return num

def densidad_promedio(lista):
    
    suma = 0
    
    for mineral in lista:
        suma += mineral.densidad()
    
    promedio = suma/len(lista)
    
    return promedio

