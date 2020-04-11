class User:  #class
    pass  #does nothing


user1 = User()  #object / instant of user class
user1.first_name = "Ena"  #field (data attatched to an object)
user1.last_name = "Suzuki"

print(user1.first_name)
print(user1.last_name)

user2 = User()
user2.first_name = "Kino"
user2.last_name = "Suzuki"

print(user1.first_name, user1.last_name)
print(user2.first_name, user2.last_name)

user1.age = 20
user2.hobby = "dance"

print(user1.age)
print(user2.hobby)


#init method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, my name is " + self.name)


p1 = Person("Ena", 20)
p1.myfunc()


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def function(self):
        print(self.name + " earned " + self.grade)


s1 = Student("Ena Suzuki", "A")
s1.function()


class Member:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def function2(self):
        print("Name: " + self.name + " Age:" + str(self.age) + " Gender:" +
              self.gender)


m1 = Member("Ena Suzuki", 20, "Female")
m1.function2()


#Exercise1
class Triangle:
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    number_of_sides = 3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return ("True")
        else:
            return ("False")


class Equilateral(Triangle):
    angle = 60

    def __init__(self):
        self.angle1 = self.angle2 = self.angle3 = self.angle


my_triangle = Triangle(90, 30, 60)

print(my_triangle.number_of_sides)
print(my_triangle.check_angles())


#Exercise2
class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for your_lyrics in self.lyrics:
            print(your_lyrics)


happy_bday = Songs(["Happy birthday to you", "!!!!"])

happy_bday.sing_me_a_song()  #don't forget the last ()


#Exercise3
class Lunch:
    def __init__(self, order):
        self.order = order

    def menu_price(self):
        if self.order == "menu 1":
            print("Your choice: " + self.order + "Price 12.00")
        elif self.order == "menu 2":
            print("Your choice: " + self.order + "Price 13.40")
        else:
            print("Error in menu")


Ena = Lunch("menu 1")  #dont forget to put the name of the class
Ena.menu_price()
"""
y = 5x + 10
x = 10... y = 60

def equation(x):
  return (5 * x) + 10

y = equation(10)
"""


class Dinner:
    def __init__(self, total):
        self.total = int(total)

    def Order(self, NewOrder):
        if NewOrder == 1:
            self.total += 12
            print("You order is set. Your order: Ramen")
        elif NewOrder == 2:
            self.total += 15
            print("You order is set. Your order: Curry")
        elif NewOrder == 3:
            self.total += 10
            print("You order is set. Your order: Gyudon")
        else:
            print("Your input is invalid, Please select 1 - 3.")

    def Total(self, NewOrder):
        if NewOrder == 1:
            self.total += 12
            print("Your total:" + str(self.total))
        elif NewOrder == 2:
            self.total += 15
            print("Your total:" + str(self.total))
        elif NewOrder == 3:
            self.total += 10
            print("Your total:" + str(self.total))
        else:
            print("Error")


Customer1 = Dinner(0)
activity = 0
"""
while activity != 9:
  activity = int(input("What do you want to do?\nPress 1 for new order\nPress 2 for see the total price\nPress 9 for quit\n"))
  if activity == 1:
    NewOrder = int(input("What would you like to order?\nPredd 1 for Ramen\nPress 2 for Curry\nPress 3 for Gyudon\n"))
    Customer1.Order(NewOrder)
  elif activity == 2:
    NewOrder = int(input("What would you like to order?\nPredd 1 for Ramen\nPress 2 for Curry\nPress 3 for Gyudon\n"))
    Customer1.Total(NewOrder)
  elif activity == 9:
    print("Thank you! Enjoy your meal!")
  else:
    print("There is an error with your input.")


def function_practice(msg, count):
  print (msg * count)

def function_practice2(msg1, msg2, msg3):
  print (msg1 + msg2 + msg3)
function_practice2("ai","u","eo")

input_1 = input("put 1 thing")
input_2 = input("put 1 thing")
input_3 = input("put 1 thing")

function_practice2(input_1, input_2, input_3)


def Name(fname, lname):
  print(fname + " " + lname)

fname = input("What's your first name?")
lname = input("What's your last name?")

Name(fname,lname)

"""
