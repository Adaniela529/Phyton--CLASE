class Product:
    id=""
    nombre=""
    precio=""
    tipo=""
    stock=""
    release=""
    def __init__(self,id,nombre,precio,tipo,stock,release) -> None:
        self.id=id
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        self.stock=stock
        self.release=release
        pass

class Catalogo:
    def __init__(self):
        self.listaProductos=[]
        self.precioTotal=0
    def agregarProducto(self,product:Product,cantidad=1):
        if self.validarStock(product):
            print("agregando producto")
            self.listaProductos.append(product)
            product.updateStock(product.stock-1)
        else:
            print("el producto no tienen stock")
         
    def mostrarProductos(self):
        print(len(self.listaProductos))
        if len(self.listaProductos)>0:
            for i in self.listaProductos:
                print(i)
        else:
            print("Datos incorrecto del producto")

message="""
    1)Agregar Producto
    2)Mostrar Productos
    3)Salir
"""
id=0
Clase1=Catalogo()
while True:

    print(message)
    opcion=int(input("ingrese la opcion a realizar:"))
    if opcion==1:
        try:
            id=id+1
            name=input("ingrese el nombre del producto:")
            precio=float(input("ingrese el precio del producto:"))
            tipo=input("ingrese el tipo del producto:")
            stock=int(input("ingrese el stock del producto:"))
            release=int(input("ingrese el release del producto:"))
            px=Product(id,name,precio,tipo,stock,release)
            Clase1.agregarProducto()
        except Exception as Error:
                print("sucedio un error")
        else:
            print("agregando en el menu")
    if opcion==2:
        Clase1.mostrarProductos()
    if opcion==3:
        break


