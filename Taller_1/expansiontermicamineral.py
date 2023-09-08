
import csv
import numpy as np
import matplotlib.pyplot as plt

from Mineral import Mineral

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


          

    def coeficiente(self):
         
        alpha=[]
        t=np.array(self.temperaturas)
        v=np.array(self.volumenes)
        dv= np.diff(v)
        dt= np.diff(t)
        dvdt= dv/dt
        
        derivada= np.empty_like(t,dtype=float)
        derivada[0]=(v[1]-v[0])/(t[1]-t[0])
        derivada[-1]=(v[-1]-v[-2])/(t[-1]-t[-2])
        derivada[1:-1]=(dvdt[:-1]+dvdt[1:])/2
        
        h1=0.001
        h2=0.01
        dvdt1= np.gradient(v,h1)
        dvdt2=np.gradient(v,h2)
        abserr=np.abs(dvdt1-dvdt2)
        error=np.mean(abserr)
   

        for i in range(len(self.temperaturas)):
            
              
              a= (1/self.volumenes[i])* derivada[i]         
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
        plt.title('Alpha vs Temperatura')

        plt.tight_layout()
        
      

        return (alpha[0], error, fig)
