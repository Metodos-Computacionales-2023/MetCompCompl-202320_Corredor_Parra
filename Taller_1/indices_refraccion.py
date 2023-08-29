
import numpy as np
import yaml
import matplotlib.pyplot as plt

def xml_to_tuples(ruta_archivo):

   arreglo=np.array(([1.0, 0.0]), dtype=float)

   with open(ruta_archivo, 'r') as yaml_file:
   
      data = yaml.safe_load(yaml_file)

      parejas=data["DATA"][0]["data"].split("\n")


      for i in parejas:
         lista=i.split(" ")
         for j in range(0, len(lista)):
            if lista[j]!="":
               lista[j]=float(lista[j]) 

         if lista[0]!="":
        
            arreglo2=np.array(tuple(lista), dtype=float)
            arreglo=np.vstack((arreglo, arreglo2))
         
      
   arreglo = arreglo[1:]

   return arreglo


def grafica(ruta_archivo):

   fuente= ruta_archivo.split("/")
   material= fuente[9].split(".")[0]
   carpeta= "Taller_1/"+fuente[8]
   arreglo=xml_to_tuples(ruta_archivo)
   longitud_onda=arreglo[:,0]
   n=arreglo[:,1]
   n_promedio=np.mean(n)
   desviacion=np.std(n)
   
   plt.figure(figsize=(10, 8))
   plt.plot(longitud_onda, n)
   plt.xlabel('Longitud de onda λ')
   plt.ylabel('índice de refracción n')
   plt.title('Índice de refracción vs longitud de onda\n para '+
             material+ " con indice de refracción \n promedio de: "+str(n_promedio)+
             " \n y desviación estándar de: "+str(desviacion))
   plt.grid(True)
   
   plt.savefig("C:/Users/Angie/OneDrive/Documentos/GitHub/MetCompCompl-202320_Corredor_Parra/"+carpeta + "/"+ material+ '.png')
   plt.show()

   return


import csv



csv_file_path = "C:/Users/Angie/OneDrive/Documentos/GitHub/MetCompCompl-202320_Corredor_Parra/Taller_1/indices_refraccion.csv"

with open(csv_file_path, "r") as csv_file:
   
    csv_reader = csv.reader(csv_file) 

    for row in csv_reader:
        
        if row[1]!="Fabricante" :
            
     
            categoria= row[0]
            material= row[2]
            
            if categoria=="Materia InorgÃ¡nica":
                categoria="Materia Inorgánica"
                
            elif categoria=="Materia OrgÃ¡nica":
                categoria="Materia Orgánica"
                
            elif categoria=="PlÃ¡sticos Comerciales":
                categoria="Plásticos Comerciales"
                
            elif categoria=="Adhesivos Ã“pticos":
                categoria="Adhesivos Ópticos"
            
            ruta="C:/Users/Angie/OneDrive/Documentos/GitHub/MetCompCompl-202320_Corredor_Parra/Taller_1/"+ categoria+ "/"+material+".yml"
            
            grafica(ruta)
            