totalamount = int(input("Total amount of a purchase :"))

if totalamount <= 100:
    print("No Discount")
elif totalamount > 100 and totalamount <= 500 :
    discount = totalamount*0.1
    print("The discount is:",totalamount-discount)
elif totalamount >500 :
    discount = totalamount*0.1
    print("The discount is:",totalamount-discount)

