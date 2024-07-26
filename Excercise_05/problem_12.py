
# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop compare the variable x with the local variable of loop

largest_number = [3, 5, 2, 1, 4]
number = 0

for i in largest_number:
    if i > number:
     number = i
 

print("The largest number in the list is:",number)