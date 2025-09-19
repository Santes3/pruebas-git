print("programa para hacer sumas")
iterar = int(input("Cuantos numeros deseas agregar para la suma?"))
x = 0
for i in range(iterar):
    numX = int(input("Agrega un numero: "))
    x += numX
    print("Numero agregado")

print(f"Suma total: {x}")