lists = []

for i in range (0, 101):
    if i > 80:
        break
    if i > 30 and i < 50:
        continue
    if i % 5 == 0:
      lists.append(i)

    print(lists)