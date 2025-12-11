marks=int(input("Enter your marks out of 100: "))
if (marks>=90 and marks<=100):
    print("You got a grade A.")
elif(marks<90 and marks>=75):
    print("You got a grade B.")
elif(marks>=60 and marks<75):
    print("You got a grade C.")
else:
    print("You are Fail.")