# Write a program that accepts 2 inputs from user and check which number is largest.
# for example:
# input1 is 5 and input2 is 10
# output should be 10 as this number is larger than 5

num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))
num3 = int(input("enter third number :"))

if num1 > num2 and num1 > num3:
    print(num1,"is larger than",num2,"and" ,num3)
elif num2 > num1 and num2 > num3:
    print(num2,"is larger than",num1 ,"and" ,num3)
else:
    print(num3,"is larger than" ,num2 ,"and" ,num1)