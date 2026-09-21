# Please write a program which estimates a user's typical food expenditure.
# The program asks the user how many times a week they eat at the student cafeteria.
#  Then it asks for the price of a typical student lunch, and for money spent on groceries during
#  the week.
# Based on this information the program calculates the user's
#  typical food expenditure both weekly and daily.

weekly_cafeteria_lunch = int(input("How many times a week do you eat at the student cafeteria?"))
lunch_price = float(input("The price of a typical student lunch?"))
groceries_spends = float(input("How many money do you spend on groceries in a week?"))
print(f"Average food expenditure:\nDaily: {(weekly_cafeteria_lunch/7)*lunch_price + (groceries_spends/7)} euros\nWeekly: {(weekly_cafeteria_lunch*lunch_price)+groceries_spends} euros")
