print("Welcome to the tip calculator.")

total_bill_sum = float(input("What was the total bill?\n$"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15?\n%"))
people = int(input("How many people to split the bill?\n"))
sum_per_person_plus_tip = round(total_bill_sum/people + total_bill_sum/people*tip_percentage/100, 2)

print(f"Each person should pay: ${sum_per_person_plus_tip}")