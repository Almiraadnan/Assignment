# Write a program that accepts 3 input from user and check the second largest.
# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 10 as this number is larger than 5 and smaller than 15

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

if (num1 >= num2 >= num3) or (num3 >= num2 >= num1):
    print(num2, "is the second largest")
elif (num2 >= num1 >= num3) or (num3 >= num1 >= num2):
    print(num1, "is the second largest")
else:
    print(num3, "is the second largest")
