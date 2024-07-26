# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.
# for example
# input1 is 10
# output should be "10 is only divisible by 2"
# input1 is 9
# output should be "9 is only divisible by 3"
# input1 is 12
# output should be "12 is divisible by 2 and 3"

number = int(input("Enter any number:"))

if number % 2 == 0 and number % 3 == 0:
    print(number,"It is divisibe by 2 and 3 both!")
elif number % 2 == 0:
    print(number,"It is divisibe by 2")
elif number % 3 == 0: 
    print("It is divisible by 3!")