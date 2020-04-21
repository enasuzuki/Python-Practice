
"""
#Class Object

  def __init__(self,radius,color):
    self.radius = radius;
    self.color = color;
  
  def add_radius(self,r):
    self.radius += r;
    return(self.radius)

C1 = Circle(1,"Red")
print(C1.radius)
print(C1.color)

C1.radius = 5 #can be changed
print(C1.radius)

C1.add_radius(4) #function
print(C1.radius) 

class Rectangle(object):
  def __init__(self, width, height, color):
    self.width = int(width);
    self.height = int(height);
    self.color = color;
  
  def add_width(self,w):
    self.width += int(w)
  
  def add_height(self,h):
    self.height += int(h)

  def Print(self):
    print("Width: " + str(self.width) + " Height: " + str(self.height) + " Color: " + (self.color))

Rec1= Rectangle(1,34,"yellow")
Rec1.Print()
"""




"""
#2 Read File
with open("sample.txt","r") as Sample:
  #FileContent = Sample.read #all
  i = 1
  for line in Sample:
    print("line" + str(i) + ": " + line)
    i += 1

Sample.closed

#writefile
line = ["Hello\n", "Good evening!\n"]
with open ("sample.txt","w") as File1:
  for Line in line:
    File1.write(Line)

File1.closed

with open("sample.txt", "r") as File1:
  print(File1.read())

"""
"""
#3.numpy


import numpy as np 
a = np.array(['banana','apple','berry'])

print(a)
for b in a:
  print(b)

a2 = np.array([[1,2,3,4,5],[4,5,6,7,8]])
for b2 in a2:
  print(b2)

#only nbumbers inside
for x in a2: 
  for y in x:
    print(y) 

#same as the avobe
for x1 in np.nditer(a2):
  print(x1)

#change the dimention
new_a2 = a2.reshape(-1)
print(new_a2)

#ndenummerate can be used to show(demention,position) and the order
for idx, x in np.ndenumerate(a2):
  print(idx,x)

x = np.array([1,2,3,4])
y = np.array([4,4,7,8])
z = np.hstack((x,y))
print(x)
print(y)
print(z)
#hstack for row, vstack for column, and dstack for height

#3分の１　
new_z = np.array_split(z,3)
print(new_z)

new_z2 = np.array_split(z,4)
print(new_z2)

whereis4 = np.where(z == 4)
print(whereis4)

print(np.sort(a)) 


#Create a filter array yjay will return only values higher than 42

arr = np.array([20.30,50,54,33,43,46])
filter_arr = []

for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
  
newarray = arr[filter_arr]

print(filter_arr)
print(newarray)




#create a filter array that will return only even elements from the original array
import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9,10])
filter_array = []

for element in array:
  if element % 2 == 0:
    filter_array.append(True)
  else:
    filter_array.append(False)

new_array = array[filter_array]

print(filter_array)
print(new_array)

#or

import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9,10])

filter_array = array % 2 == 0
new_array = array[filter_array]

print(filter_array)
print(new_array)

#random numbers 

from numpy import random

x = random.randint(100) #random int from 0 to 100
print(x)

x = random.rand() #random flat between 0 and 1
print(x)

from numpy import random
x = random.randint(100,size=(5)) #random 5 ints bet 0 to 100
print (x)

x = random.randint(100,size=(3,5))
print(x)

x = random.rand(5) #5 * float bet 0 and 1
print(x)

#randomchoicefromarray

from numpy import random
x = random.choice([1,2,3,4,5,6,7,8,9],size=(3,20))
print(x)

from numpy import random
x = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0],size=(3,5)) #p means probability
print(x)

"""
