salary = int(input("Enter you salary :"))
years = int(input("Enter your years of services :"))

if years <= 5:
    print("No bonus")
elif years > 5 and years <= 10:
    print("The  bonus is:",salary*0.10)
elif years <= 11 and years >= 20:
    print("The  bonus is:",salary*0.20)

