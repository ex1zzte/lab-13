print ("Задача 1")
girls=["Ивента","Виолетта","Касандра","Вирджиния","Амелия","Розамунда","Янина","Беатриса"]
print (girls[1:5])
print (girls[3:8])
print ([girls[0],girls[1],girls[3],girls[4]])
print ([girls[2],girls[3],girls[5]])
print ("Задача 2")
import math 
L= [12,3,8,125,10,98,54,199]
for item in L:
    print (item)
for item in L:
    print (math.log(item))
L[4]=0
for item in L:
    print (item)
for item in L:
    if item > 0:
        print(math.log(item))
    else:
        print("Логарифм от 0 не определен")
print ("Задача 3")
age = [24,35,42,27,45,48,33]
age2 =[]
for a in age:
    age2.append(a**2)
print(age2)
print ("Задача 4")
a=input ("Введите число от 1 до 10:")
numbers = [1,5,6,8,10,21,1,0,-9,9]
print (numbers[int(a)-1])