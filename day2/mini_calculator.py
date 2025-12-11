choice=int(input("choose Operations:" \
"1.Addition" \
"2.Subtracton" \
"3. Multiplication." \
"4.Division. "))
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if (choice==1):
    print(f"The sum of {a} and {b} is: {a+b}")
elif(choice==2):
    print(f"The Difference of {a} and {b} is : {a-b}")
elif(choice==3):
    print(f"The product of {a} and {b} is: {a*b}")
elif(choice==4):
    if b==0:
        print("Division by zero is not allowed.")
    else:
        print(f"The division of {a} and {b} is: {a/b}")
else:
    print("Please select the choice from 1-4.")