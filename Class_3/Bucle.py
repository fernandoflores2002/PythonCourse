#BUCLES

#WHILE

# number=10
# contador=0

# while contador < 10:
#print(number)
#contador+=1

# print('Salir',contador)

# answer = ''
# num=0
# factorial=1
# aux=num
# while True:
#     num=int(input('Ingrese un numero: '))
#     if num<0:
#        print('Error! The number must be positive or 0')
#     else:
#         aux=num
#         while num>0:
#             factorial *= num #factorial=factorial*num
#             num-=1
#             print(f'{aux} != {factorial}')
#         while answer !='y' or answer != 'n':
#             answer = input('Have you finished? (y/n)')
#             if answer != 'y' and answe != 'n':
#                 print('Error! The value must be y or n.')
#             else:
#                 break 
#         if answer= 'y'
#         break
#         else:
#             factorial=1

#FOR

#range(x) -> devuelve una lista de 0 (<=) hasta x (<)
#range (x,y) -> devuelve una lista de x (<=) hasta y (<)
#range(x,y,z) -> devuelve una lista una lista de x (<=) hasta y (<) de z en z

#LISTA

lista=[1,2,3.0,True, 'Anthony', False, [1,0,1.9]]
print(lista)
print(type(lista))
print(len(lista))

lista2=lista[-1:-5:-1]
print(lista2)
lista.append('hola')
print(lista)
# lista.pop() #Me quita el ultimo valor por defecto
# print(lista)
lista.pop(3)
print(lista) #ME quita el booleano true
for value in lista:
    print (value), end=''
print (lista)




#TUPLAS no se puede modificar los valores
tupla=(1,2.0, 'Anthony ', True,1,1,1,1)
for value in tupla:
    print (value,end='')
print()
print(tupla.index(1))
print(tupla.count(2.0)) 
print(tupla)
lista= list (tupla)
lista=tuple(lista)
print(lista)


#CONJUNTO

conjunto= set()
conjunto={1,2,3,1,2,3,4,5,4,5}
print(conjunto)
conjunto.add(6)
print(conjunto)
conjunto.discard(1)
print(conjunto)
conjunto.discard(1)
print(conjunto)
conjunto.remove(1)
print(conjunto)

A={1.2.3.4.5}
B=set()
B={4,5,6,7}







#Diccionarios tienen llaves que organizan valores
dic={'Anthony':'Luzquiños','ALvaro':'Plasencia','Ruben':'Ricapa'}
 print(dic)
 keys= list(dic.keys())
 values=list(dic.values())
 print(keys)
 print(values)
 
dic['Carlos']= 'Bazan'
print(dic)
dic.pop('Alvaro')
print(dic)



#SIMULAR UNA AGENDA DE CALULAR QUE GUARDE NOMBRES Y CELULARES
#AGREGAR,ELIMINAR Y MOSTRAR