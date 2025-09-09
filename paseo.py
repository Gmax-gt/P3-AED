class Paseo:
    def __init__(self,identificacion,nombre,tipo,monto):
        self.identificacion = identificacion
        self.nombre = nombre
        self.tipo = tipo
        self.monto = monto

    def __str__(self):
        return ("Id: {:<4} / Nombre: {:<7} / tipo: {:<2} / monto: $ {:<6}". format(self.identificacion,self.nombre,self.tipo,round(self.monto,2)))
