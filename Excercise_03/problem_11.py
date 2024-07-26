# Write a program that accepts 2 inputs from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10
# output should be 10 as this number is larger than 5

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))

if num1 > num2:
    print(num1," is larger than",num2)
elif  num1 < num2:
    print(num2," is larger than",num1)