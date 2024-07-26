membership_status = input("Are you a member? (yes/no): ").lower()
purchase_amount = float(input("Enter the purchase amount: "))

if membership_status == "yes":
    if purchase_amount >= 50:
        print("Eligible for 10% discount")
    else:
        print("Eligible for 5% discount")
else:  
    if purchase_amount >= 100:
        print("Eligible for 5% discount")
    else:
        print("No discount")
