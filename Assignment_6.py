#Problem 1: Program to print fibonacci sequence using recursion
#sol:
def fibon(n):
    fib_seq = []
    for i in range(n+1):
        if i <= 1:
            fib_seq.append(i)
        else:
            fib_seq.append(fib_seq[i-2] + fib_seq[i-1])
    return fib_seq

print(fibon)


#Problem 2: Program to find factorial of a number using recursion
#Sol:
def facto(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*facto(n-1)
print(facto(5))

#Problem 3: Program to find BMI
#Sol:
def BMI(height,weight):
    return weight/height*height


#Problem 4: Program to calculate natural logarithm of any number 
#sol:
import math
num = int(input("Enter the number: "))
if(num>1):
    print(math.log(num))


#Problem 5: Program to print cube of sum of first n natural numbers
#Sol:
def Cube(n):
    s = 0
    for i in range(1,n+1):
        s = s+(i**3)
    return s


