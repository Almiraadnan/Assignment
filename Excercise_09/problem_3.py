# Write a program that takes a birth year as input and calculates the age of a person.


# The program should prompt the user to enter their birth year and then display their current age in years, months, and days.

from datetime import datetime

birth_year = int(input("Enter your birth year: "))
today = datetime.now()
current_year = today.year
age_in_years = current_year - birth_year

print("Your current age is", age_in_years, "years")





