class Mineral:
    
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors
    
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
        
        rgb_Color = mcolors.to_rgba(col)
        color = mcolors.rgb2hex(rgba_color)
        
        return color
    
    