# while True:
#     try:
#         number=int(input('Type a number: '))
#     except ValueError:
#         print('The number you\'ve just typed is not an integer.')
#     else:
#         print(number)
#         break
#     finally:
#         print('I\'m being always executed')

#Implementar un algoritmo que calcule el area de un triangulo usando heron
#Heron:Area=((s-a)(s-b)(s-c)s)*0.5
#s=a+b+c/2

triangle= [0]*3 #triangle=[0,0,0]
validator= ''
p=0
aux=0
#ERROR CODES:
#1 -> numero correcto
#2 -> no es un numero
#3 -> el ingresado es negativo o 0

def positive_number(number):
    if number <=0:
        return 3
    else:
        return 1


def validate_number(possible_number):
    try:
        possible_number= float(possible_number)
    except ValueError:
        print('The value you just typed is not a number')
        return 2
    else:
        return positive_number(possible_number)

def validate_triangle(triangle):
    if math.fabs(triangle[0]-triangle[1])<triangle[2]\
        and triangle[2]<triangle[0]+triangle[1]:

         if math.fabs(triangle[1]-triangle[2])<triangle[0]\
             and triangle[0]<triangle[1]+triangle[2]:

              if math.fabs(triangle[0]-triangle[2])<triangle[1]\
                  and triangle[1]<triangle[0]+triangle[2]:

                  return True
    return False

triangle= [0]*3 #triangle=[0,0,0]
validator= ''

def heron():
    global p

 for index in range(0,len(triangle)):
    while True:
        
      triangle[index]=input('Type a number: ')
      validator= validate_number(triangle[index])
       if validator==1:
         triangle[index]=float(triangle[index])
         break
       elif validator==2:
          print('The value you just typed is not a  number')
       else:
          print('The number is negative or 0')

    result= validate_triangle(triangle)

    if result:
        print('It is a triangle')
        for i in range(0,3):
            p += triangle[i]
        p/=2
        aux=p
        for i in range(0,3):
            p*= (aux-triangle[i])

        return math.sqry(p)
    else:
        print('It isnt a triangle. Try again:' )

print(f'The triangle area is: {heron(): .5f}u2.'

#paso por referencia y paso por valor
#estudiar funciones