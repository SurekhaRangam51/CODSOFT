#Python code for Calculator
def add(input1,input2):
    return input1 + input2
def sub(input1,input2):
    return input1-input2
def mul(input1,input2):
    return input1*input2
def div(input1,input2):
    return input1/input2
def power(input1,input2):
    return input1**input2

print("Welcome to Calculator")
print("1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Power \n ")
operator=int(input("Enter the operator:"))
if(operator>5):
    print("Enter the valid operator")
else:
    input1=int(input("Enter the First Number:"))
    input2=int(input("Enter the Second Number:"))
    if operator==1:
        add=add(input1,input2)
        print("Addition of Two Numbers is",add)
    elif operator==2:
        sub=sub(input1,input2)
        print("Subtraction of Two Numbers is",sub)
    elif operator==3:
        mul=mul(input1,input2)
        print("Multiplication of Two Numbers is",mul)
    elif operator==4:
        if input2==0:
            print("Infinity")
        else:
            div=div(input1,input2)
            print("Division of Two Numbers is",div)
    elif operator==5:
        power=power(input1,input2)
        print(f"{input1} power of {input2} is",power)

