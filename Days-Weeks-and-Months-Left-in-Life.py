# This script is just created to test F-String :)

age = input("What is Your Current Age: ")

age_as_int = int(age)
average_age = 90
years_remaining = average_age - age_as_int

age_as_days = years_remaining * 365
age_as_weeks = years_remaining * 52
age_as_months = years_remaining * 12

print(f"You have {age_as_days} days, {age_as_weeks} weeks, and {age_as_months} month left in your life")