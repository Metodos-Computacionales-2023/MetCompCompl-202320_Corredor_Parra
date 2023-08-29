
import csv
import numpy as np
import matplotlib.pyplot as plt

from Taller_1.Mineral import Mineral

class ExpansionTermicaMineral(Mineral):

    import matplotlib.pyplot as plt

    def __init__(self, nombre, dureza, lustre,
                  rompimiento_por_fractura, color, 
                  composicion, sistema_cristalino, 
                  specific_gravity, archivo):
        
        super().__init__(nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, sistema_cristalino, specific_gravity)

  
        temperatura_l=[]
        volumen_l=[]
        with open(archivo, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader) 
            
            for i in csv_reader:

                temperatura_l.append(float(i[0])+273.15)
                volumen_l.append(float(i[1])/1000000)

        self.temperaturas = temperatura_l

        self.volumenes = volumen_l


     #extraido de las notas de clase

    def DerivadaCentral(f,x,h):
    
            d = 0.
            
            if h != 0:
                d = (f(x+h) - f(x-h))/(2*h)
                
            return d           

    def coeficiente(self):
         
        alpha=[]
        error=0

        for i in range(len(self.temperaturas)):
              
              a= (1/self.volumenes[i])*self.DerivadaCentral(self.volumenes[i],self.temperaturas[i],0.01)             
              alpha.append(a)

        fig=plt.figure(figsize=(10, 6))


        plt.subplot(1, 2, 1)
        plt.plot(self.temperaturas, self.volumenes)
        plt.xlabel('Temperatura (K)')
        plt.ylabel('Volumen (m^3)')
        plt.title('Volumen vs Temperatura')

        plt.subplot(1, 2, 2)
        plt.plot(self.temperaturas, alpha)
        plt.xlabel('Temperatura (K)')
        plt.ylabel('Alpha (1/K)')


        plt.tight_layout()

        return (alpha[0], error, fig)


        
