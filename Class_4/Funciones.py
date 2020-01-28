#FUNCIONES
variable=27
print(variable)
def saludar(nombre, edad):
    global variable
    variable +=2
    print(variable)
    print(f'¡Hola {nombre} tiene {edad} años!')

def salir():
    print('Nos vemos!')
salir()
saludar('Ruben',27)
# saludar('Adan',18)
# saludar('Anthony',23)
# saludar('Fernando',17)


numero=27
print('Numero desde afuera:',numero)

def saludar(nombre,edad):
    global numero
    numero += 2 #numero= numero +2
    print('Numero desde saludar:',numero)
    #print(f'¡Hola {nombre} tiene {edad} años!)
    return numero #guarda el numero