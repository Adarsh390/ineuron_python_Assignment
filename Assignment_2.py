# 1:-Program to convert kilometers to miles?
km = int(input("Enter the kilometer"))
miles = km/1.60934
print(f"For {km}km equivalent distance in miles = {miles}")

#2:-Program to convert celsius to fahrenheit
c = float(input("Enter celsius"))
f = (9*c/5)+32
print(f"value of {c}celsius in fahrenheit = {f}")


#3:-Program to Display calendar
import calendar
year = 2021
month = 11
print(calendar.month(year,month))

# 4:-Program to solve the quadratic equation?
import math
print("Quadratic equation form = ax^2+bx^1+c")
print("Enter the value for the coffecient of a,b and cosntant c")
a = int(input("Enter the value of coffe a:- "))
b = int(input("Enter the value of coffe b:- "))
c = int(input("Enter the value of constant c:- "))
d = ((b**2)-4*a*c)
x1 = ((-1*b)+(math.sqrt(d)))/(2*a)
x2 = ((-1*b)-(math.sqrt(d)))/(2*a)
print(x1,x2)
print(d) 

#5:-Program to swap two variable without using the third variable
num1 = int(input("Enter the 1st no:- "))
num2 = int(input("Enter the 2nd no:- "))
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print("After swap value of two number are {},{}".format(num1,num2))


