user_input = input("Enter the color of the traffic light: ").lower()

if user_input == "green":
    print("Car is allowed to go")
elif user_input == "red":
    print("Car has to stop")
elif user_input == "yellow":
    print("Car has to wait")
else:
    print("Invalid input")
