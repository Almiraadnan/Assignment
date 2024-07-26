Card = input("Do u have a affiliated card ? (yes/no)")
age =int(input("Enter your age")) 
senior_citizen = input("Are you a senior citizen? (yes/no)")
govt_employe = input("Are you goverement employe? (yes/no)")

if Card == "yes" and age < 60:
     print("Transactions allowed")
     if senior_citizen == "yes":
         print("Transactions allowed")
         if govt_employe == "yes":
             print("Transactions allowed")
elif age<=18:
    print("You got extra 10rs at you transaction")
else:
    print("Transaction denied.")

