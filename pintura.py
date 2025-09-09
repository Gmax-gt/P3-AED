class Pintura:
    def __init__(self,codigo,tipo,cantidad,precio):
        self.codigo = codigo
        self.tipo = tipo
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return "Codigo:{:<4} / Tipo :{:<3} /  Cantidad :{:<3} / Precio :{<6}".format(self.codigo,self.tipo,self.cantidad,self.precio)
