full_name = input("Enter your full name :")
full_name_upper =full_name.upper()
modified_sentence = full_name.replace(" ","-")
full_name_length =len(full_name)

print("Your full name in uppercase is: " + full_name_upper)
print("Modified sentence: " + modified_sentence)
print("The length of your full name is: " + str(full_name_length))
