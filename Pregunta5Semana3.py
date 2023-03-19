import os
from Ejercicios_Semana3.Pregunta4 import Producto
try:
   product=Producto("Televisor","Argentina","00056","2023")
   print(product)
except:
    print("ingrese un valor correcto")
else:
    cwd = os.getcwd() 
    print("Ruta de directorio: ",cwd)
finally:
    print("Proceso Terminado")
