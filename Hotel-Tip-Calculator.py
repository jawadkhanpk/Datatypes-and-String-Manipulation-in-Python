print("Welcome to Hotel Tip Calculator!")
total_bill = float(input("What is the Total Bill? $"))
tip = int(input("What tip_percentage would you like to give? 10, 12, or 15? "))
number_of_people_to_split_bill = int(input("How many people to split the bill? "))

tip_percentage = (tip * 100) / total_bill

bill_with_tip = total_bill + tip_percentage

bill_per_person = bill_with_tip / number_of_people_to_split_bill

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
