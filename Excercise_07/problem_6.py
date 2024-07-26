# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."


user_input = ""

while user_input != "END":
    user_input = input("Enter your name (enter 'END' to exit): ")
    print("You entered:", user_input)

print("I am done")

