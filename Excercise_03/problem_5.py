marks = int(input("Enter your marks :"))

if (marks > 90 and marks <= 100):
    print("your grade is  A+")
elif(marks > 80 and marks <= 90):
    print("your grade is  A")
elif(marks > 80 and marks <= 70):
    print("your grade is  B")
elif(marks > 70 and marks <= 60):
    print("your grade is  C")
elif(marks > 60 and marks <= 50):
    print("your grade is  D")
else :
    print("you are failed")