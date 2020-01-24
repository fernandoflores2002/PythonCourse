#SIMULAR UNA AGENDA DE CALULAR QUE GUARDE NOMBRES Y CELULARES
#AGREGAR,ELIMINAR Y MOSTRAR 936962826
#For: recorrer un elemento que es iterable

# agregarContacto -> camell case >javascript,java
# AgregarContacto -> camell upper case
# agregar_contacto -> 
dic={}

def agregar_contacto(nombre):
    # dic['Alvaro']=['Plasencia','987654320','alvaro.plasencia@uni.pe']
    apellido = input('Ingresar apellido: ')
    cell = input('Ingresa celular: ')
    correo = input('Ingresa correo:')
    dic[nombre] = [apellido,cell,correo]

def buscar_contacto(nombre):
    if nombre in dic:
        print('Contacto encontrado:')
        print(nombre, dic[nombre])
    else:
        print('No existe el contacto')
    print()

def eliminar_contacto(nombre):
    
    dic.pop(nombre)
    mostrar_contacto()

def mostrar_contacto(nombre):
    print('Contactos: ')
    for position,key in enumerate(dic):
        print(position+1,key, dic[key])
        print()


while True:
    print('Menu')
    print('1) Agregar contacto')
    print('2) Eliminar contacto')
    print('3) Mostrar contacto')
    print('4) Buscar contacto')
    print('5) Salir')
    number= int(input('Ingrese una opcion:'))
    if number==5:
        break
    elif number!=1 and number!=2 and number!=3 and number!=4 :
        print("Ingrese un numero valido")
        number=int(input('Ingrese una opcion:'))
    else:
        if number==1:
            nombre= input('Nombre: ')
            agregar_contacto()
        if number==2:
            nombre= input('Nombre: ')
            eliminar_contacto()
        if number==3:
            nombre= input('Nombre: ')
            mostrar_contacto()
        if number==4:
            nombre= input('Nombre')
            buscar_contacto()
        
         

        
# redondeo
#x=2/3
#print(f'{x:.5f})