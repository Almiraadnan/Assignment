# 9. consider the list ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
# use for loop and find the count that how many times the word "hi" present in list.
# output should be 3

list = ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']

for i in range(len(list)):
    count =  list.count('hi')
    
print(count)