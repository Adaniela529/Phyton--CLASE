for i in range(10):
    print(i)
#sec=0.00001 =>0.00001*10
numero=int(input("identifica que el numero sea primo"))
es_primo=True
for num in range(2, numero):
    if numero % num == 0:
        es_primo=False
        break 

if es_primo:
    print("Son numeros primos")
else:
    print("No son numeros primos")
