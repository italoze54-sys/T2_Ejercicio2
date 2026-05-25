def BuscarPo(lista, numero, i=0):
    
    if i == len(lista):
        return -1  
    
    if lista[i] == numero:
        return i   
    
    return BuscarPo(lista, numero, i + 1)

def RangoaSumar(lista, pi, pf):
    if pi > pf:
        return 0
    return lista[pi] + RangoaSumar(lista, pi + 1, pf)

tamaño = int(input("Ingrese el tamaño del arreglo: "))

elementos = []
for i in range(tamaño):
    num = int(input(f"Ingrese el elemento {i+1}: "))
    elementos.append(num)

valorInicio = int(input("Ingrese el valor inicial (PI): "))
valorFinal = int(input("Ingrese el valor final (PF): "))

Pi = BuscarPo(elementos, valorInicio)
Pf = BuscarPo(elementos, valorFinal)

if Pi != -1 and Pf != -1 and Pi < Pf:
    
    PI = Pi + 1
    PF = Pf - 1
    
    resultado = RangoaSumar(elementos, PI, PF)
    print("Resultado =", resultado)
else:
    print("Error: Valores no válidos o no encontraos en el orden correcto.")