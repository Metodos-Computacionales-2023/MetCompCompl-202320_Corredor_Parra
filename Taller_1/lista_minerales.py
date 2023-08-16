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


