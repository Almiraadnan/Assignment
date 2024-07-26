numbers = [12, 7, 9, 24, 18, 5, 3, 20]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers in the list:", even_count)
print("Number of odd numbers in the list:", odd_count)
