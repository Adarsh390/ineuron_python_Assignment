# Problem 1: Program to find factorail of a number
# Sol:
num = int(input("Enter the number: "))

# iterative solution 
if(num>=2):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    print(fact)
elif(num==1 or num==0):
    print(1)
else:
    print("factorail of negative number is not possible!")


#Recursive Solution:
def facto(num):
    if(num<=1):
        return 1
    else:
        return num*facto(num-1)
print(facto(6))


# Problem 2: Program to print the multiplication table

num = int(input("Enter the number : "))
for i in range(1,11):
    print("{} x {} = {}".format(num, i, num*i))



# Problem 3: Program to print Fibonacci sequence
#Sol:
fibo_length = int(input("Enter a length: "))

a = 0
b = 1
print(a, end = ' ')
print(b, end = ' ')
while(fibo_length-2 > 0):
    nt = a + b
    print(nt, end = ' ')
    a = b
    b = nt
    
    fibo_length -= 1


#Problem 4: Program to print Armstrong Number
#Sol:

def Armstrong(n):
    l=len(str(n))
    temp = n
    s = 0
    while(temp!=0):
        last_digit = temp%10
        s+=last_digit**l
        temp = temp//10
    if(s==n):
        return 1
    else:
        return 0

print(Armstrong(1634))


#Problem 5: Program to print Armstrong number in an interval
# Sol:
start = int(input("Enter the start point : "))
end = int(input("Enter the start point : "))
for i in range(start,end+1):
    l=len(str(i))
    if(l>=2):
        temp = i
        s = 0
        ans = []
        while(temp!=0):
            last_digit = temp%10
            s+=last_digit**l
            temp = temp//10
        if(s==i):
            ans.append(i)
            print(ans)


#Problem 6: Program to print sum of natural numbers 

num = int(input("Enter the number : "))
s = 0
for i in range(1,num+1):
    s+=i
print(s)






