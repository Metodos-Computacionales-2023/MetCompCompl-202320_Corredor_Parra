class Mineral:
    
    import matplotlib.pyplot as plt

    
    def __init__(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, sistema_cristalino, specific_gravity):
        self.nombre = nombre
        self.dureza = dureza
        self.lustre = lustre
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.composicion = composicion
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = specific_gravity
        
    #comentario
    def silicato(self):
        respuesta = False
        compo = self.composicion
        
        if "Si" in compo and "O" in compo:
            not respuesta
            
        return respuesta        
    
    def densidad(self):
        dens = self.specific_gravity
        
        valor = dens*997
        respuesta = "Su densidad es " + string(valor) + " Kg/m^3"
        
        return respuesta
    
    def color(self):
        col = self.color

        fig, ax = plt.subplots()

        recta = plt.Rectangle((0, 0), 1, 1, color=col)
        ax.add_patch(recta)

        # Configura los límites de los ejes y desactiva los ticks
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xticks([])
        ax.set_yticks([])

        # Muestra la figura
        plt.show()
        
    def info(self):
        dureza = self.dureza
        rompimiento = ""
        if self.rompimiento_por_fractura:
            rompimiento = "por fractura"
        else:
            rompimiento = "por escision"
        sistema = self.sistema_cristalino
        
        print("El mineral tiene las siguientes caracteristicas: ")
        print("Duerza: " + str(dureza))
        print("Rompimiento: " + rompimiento)
        print("Sistema de organizacion de los atomos " + str(sistema))

    

            
            