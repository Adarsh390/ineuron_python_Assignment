#Problem 1: Program to check number is +ve,-ve,zero ?
#Sol:
num = int(input("Enter any number : "))

if(num > 0):
    print(num, "is Positive")
elif(num < 0):
    print(num, "is Negative")
else:
    print(num, "is Zero")

#Problem 2: Program to check if a number is odd or even ?
#Sol:
num = int(input("Enter a number: "))

if(num % 2 == 0):
    print(num, "is a Even Nummber")
else:
    print(num, "is an Odd Number")


#Problem 3: Program to check Leap Year?
#Sol:
year = int(input("Enter the year: "))
if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print("Leap Year")
else:
    print("Not a Leap Year")

#Problem 4: Program to check Prime Number ?
#Sol:
num = int(input("Enter the number : "))
if(num<=1):
    print(f"{num} is neither prime nor composite.")
else:
    for i in range(2,num):
        if(num%i==0):
            print(f"{num} is not prime ")
            break
    else:
        print(f"{num} is a prime number")

#problem 5: Program to print all number in interval 1 to 10000
#sol:
for i in range(1,10001):
    print(i)



