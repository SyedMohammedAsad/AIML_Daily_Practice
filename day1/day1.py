print("hello world")
print('*' * 10)
##PROGRAM 1 : PROFILE 
name ="Syed Mohammed Asad"
age=20
branch='B.TECH AIML'
college ='malla reddy university'
city =' hyderabad'
print("--Captain Profile--")
print("Name:",name)
print("Age:",age)
print("branch:",branch)
print("collage",college)
print("City:",city)
## PROGRAM:2 BASIC MATH OPERATIONS
print("\n----- BASIC MATH OPERATIONS-----")
a=15
b=4
print('a = ',a)
print('b=',b)
print("Addition(a+b) = ",a+b)
print("Subtraction(a-b) = ",a-b)
print("Multiplicaion(a*b) = ",a*b)
print("Division(a/ b) = ",a/b)
print("Floor Division (a//b):",a//b)
print("Remainder/Modulus (a % b):",a%b)
print('*'*15)
##PROGRAM:3 TAKING USER INPUT
print("\---User Introduction Program----")
user_name=input("Enter your Name: ")
user_age=input("Enter your age: ")
user_city=input("Enter your city: ")
print("\n----User Details-----")
print("Name: ",user_name)
print("age: ",user_age)
print("City: ",user_city)
print("*"*15)
##PROGRAM:4 SMART CURRENCY CONVERTER
print("\n----Smart Currency Converter ---")
print("Choose Conversion Type: ")
print("1. INR to USD")
print("2. USD to INR")
choice=input("Enter your choice(1 or 2): ")
usd_rate= 83
if choice=="1":
    rupees=float(input("Enter amount in INR: "))
    dollars = rupees/usd_rate
    print("Amount in USD: ",dollars)
elif choice=="2":
    dollars=(float(input("Enter amount in USD: ")))
    rupees=dollars*usd_rate
    print("Amount in INR: ",rupees)
else:
    print("Invalid choice! please restart and choose 1 or 2.")
## PROGRAM:5 RECTANGLE CALCULATOR
print("\n----Rectangle Area and Perimeter Calculator---")
length=float (input("Enter the length of the rectangle: "))
width=float(input("Enter the width of the rectangle: "))
area=length*width
perimeter=2*(length+width)
print("Area of Rectangle:",area)
print("Perimeter of Rectangle: ",perimeter)