# x=10    
# #Pedro tiene x años
# print('Pedro tiene', x, 'años.')
# print('Pedro tiene {} años' .format(x))
# print(f'Pedro tiene {x} años')
# print(type(x))
# x='Anthony'
# print(type(x))
# x=10

# #OPeradores matematicas
# x=10
# print(x)
# x = x+5
# x+=5
# print(x)
# x-=4
# x = x-4
# print(x)
# x=x/5
# x/=5
# print(x)
# x=x*3
# x*=3
# print(x)
# x=10
# x=x**2
# print(x)
# x=x//89 #cociente o division entero
# print (x)
# x= x%89 #residuo
# print(x)
# x=10
# x=10**0.5
# print(x)

# name=input('What\'s your name?')
# age=int(input('How old are you?'))
# print('Hi',name,'\b!')
# print('You are',age,'years old')
# print(type(name))
# print(type(age))

# if age >= 18 :
#     print('You are allow to pass')
# else :
#     print('You shall not pass.')

# if age<0:
#     print('Error! An age can\'t be negative')
#     elif age <18: #else if=elif
#         print('You shall not pass')
#     else:
#         print('You are allowed no pass')

# if age < 0:
#     print('Error! An age   ')

import math               
print('Calcular el area del circulo')
radio=float (input('Introduzca el radio:'))
if radio<0:
    print ('El radio no puede ser negativo')
elif radio==0:
 print('El area es 0')
else :
 A= (radio**2)*math.pi
 print('El area es', A ,'\bu2.')


