l1 = ['a', 'b', 'c', 'd']
l2 = ['e', 'b', 'g', 'd', 'f', 'h']


common_values = {}


for item1 in l1:
    count = 0  
    for item2 in l2:
        if item1 == item2:
            count += 1
    common_values[item1] = count

for item2 in l2:
    if item2 not in common_values:
        common_values[item2] = 1 
print(common_values)