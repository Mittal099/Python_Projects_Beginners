"""
Inputs we need from user
Total rent
Total food ordered for snacking
Electricity units spend
Charge per unit
Person living in room/flat


Output
Total amount you've to pay is
"""

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amont of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each persons will pay = ", output)
