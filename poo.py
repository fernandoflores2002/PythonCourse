

#Clase:
# -> Son abstracciones de las cosas de la vida cotidiana
# -> Moldes o plantillas para crear objetos
#Objeto: entidades de la vida real
# ->Un ejemplar de una clase particular
# ->Una instancia de una clase
# -> SE usan metodos

#MEtodos:
#

# class Person():

#     #Constructor
#     def __init__(self,name, last_name, age):
#         #Atributes
#         self.name = name
#         self.last_name = last_name
#         self.age = age

#     #Method
#     def greet(self):
#         return 'Hi! My name is ' + self.name + ' '+self.last_name + ', I am ' + str(self.age)+' years old.'

# person_1= Person('Anthony','Luzquiños',23)
# person_2= Person('Ruben','Ricapa',15)

# print(person_1.greet())
# print(person_2.greet())

# class Car():
#     def __init__(self,color,velocity,state):
#      self.color = color
#      self.velocity = velocity
#      self.state = state

#     def turn_on(self):
#         self.state = 'on'
#         return 'The car is on'
#     def brake(self):
#         self.velocity= 0
#     def speed_up(self):
#         self.velocity += 10
#     def turn_off(self):
#         self.state ='off'
#         return' the car is off'

# Mi_carrito = Car('Negro',0,'off')
# print(Mi_carrito.color, Mi_carrito.velocity, Mi_carrito.state)
# print(Mi_carrito.turn_on())
# print(Mi_carrito.color, Mi_carrito.velocity, Mi_carrito.state)

#str sirve para castear, pero en objetos para imprimir
class Car():
    def __init__(self, model, brand): #init es un metodo especial definido por python, y ponemos los parametros
        self.model = model
        self.brand = brand
        self.speed = 0
        self.status = 'off'

    def turn_on(self):
        if self.status == 'on':
            print('The car is already turned on.')
        else:
            self.status='on'
            print('The car is now turned on.')
    def acelerate(self):
        if self.status == 'on':
         self.speed += 10
         print('Now, the speed is:', self.speed)
        else:
            print('The car is turn off, you must turn on it')
    def brake(self):
        self.speed = 0
        print('Now, the car has stopped')
    def turn_off(self):
        if self.status== 'off':
            print('The car is already turned off.')
        else:
            # self.speed = 0
            self.status= 'off'
            print('The car is now  turned off')

    def _str_(self):
        return 'MOdelo: ' + self.model + ' \nMarca: ' + self.brand
    
car_1 = Car('Grand Prix', 'Pontiac')
# car_2 = ('Fiesta', 'Ford')
print(car_1)
car_1.turn_on()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.acelerate()
car_1.brake()
car_1.turn_off()
