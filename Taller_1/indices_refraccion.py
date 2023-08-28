
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
   material= fuente[2].split(".")[0]
   carpeta= "Taller_1/"+fuente[1]
   arreglo=xml_to_tuples(ruta_archivo)
   longitud_onda=arreglo[:,0]
   n=arreglo[:,1]
   n_promedio=np.mean(n)
   desviacion=np.std(n)
   
   plt.scatter(longitud_onda, n)
   plt.xlabel('Longitud de onda λ')
   plt.ylabel('índice de refracción n')
   plt.title('Índice de refracción vs longitud de onda para '+
             material+ "con indice de refracción promedio de "+str(n_promedio)+
             " y desviación estándar de "+str(desviacion))
   plt.grid(True)
   plt.show()
   plt.savefig(carpeta + "/"+ material+ '.png')

   return


