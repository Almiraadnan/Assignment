# Example of a while loop
numbers =[]
count = 0
x = 0
while count < 5:
    input_num = int(input("Enter any number :"))
    count+= 1
    numbers.append(input_num)
    x += input_num


print(x)