#Problem 1: Program to find LCM
#Sol:
def Lcm(num1,num2):
    a = num1
    b = num2
    while(b):
        a,b = b,a%b
    ans = (num1*num2)//a
    return ans
print(Lcm(2,12))


#Problem 2: Program to find Hcf
#Sol:
def Hcf(a,b):
    while(b):
        a,b = b,a%b
    return a
print(Hcf(53,33))


#Problem 3: Program to convert decimal to binary,octal and Hexadecimal 
#sol:
def convert(n):
    print("Binary :",bin(n))
    print("octal :",oct(n))
    print("hexadecimal :",hex(n))

#Problem 4: Program to find the ASCII vale of a character 
#Sol:
ch = input("Enter a character : ")
ans = ord(ch)
print(f"ASCII Value of {ch} is : {ans}")


#Problem 5: Program to make a calculator with 4 basic operation
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

while(True):
    print("For Addition:  +")
    print("For subtraction:  -")
    print("For Multiplication:  *")
    print("For division:  /")
    print("For Exit:  X")

    ch = input("\nEnter the operation you want to perform! : ")

    if(ch=="+"):
        result  = num1+num2
    if(ch=="-"):
        result  = num1-num2
    if(ch=="*"):
        result  = num1*num2
    if(ch=="/"):
        result  = num1/num2
    if(ch=="X"):
        break

    print("\n {} {} {} = {}".format(num1,ch,num2,result))
    response = input("Would you like to continue calculation! Yes or No: ")
    if(response=="No"):
        break
    else:
        continue



