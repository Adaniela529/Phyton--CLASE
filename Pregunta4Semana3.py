class Producto:
    nombre=""
    pais=""
    lote=""
    anio=""
    def __init__(self,nombre,pais,lote,anio) -> None:
        self.nombre=nombre
        self.pais=pais  
        self.lote=lote  
        self.anio=anio  
        pass
    def __str__(self) -> str:
        return f"el producto {self.nombre} tiene el codigo {self.pais}-{self.lote}-{self.anio}"
      
product=Producto("Televisor","Argentina","00056","2023")
print(product)
