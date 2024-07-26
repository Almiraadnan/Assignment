age = int(input("Enter your age :"))

if age <= 13:
    print("Child")
elif age >= 13 or age < 19:
    print("Teenager")
elif age >= 20 and age < 65:
    print("Adult")
elif age >= 65:
    print("Senior")