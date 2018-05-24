#This program will ask the user to input monthly investment,interest rate , and number of years.The program output future amount.

import locale
result = locale.setlocale(locale.LC_ALL, '')
if result == "C":
    locale.setlocale(locale.LC_ALL, 'en_US')
print("Welcome to the Future value calculator!")
print()
choice = "y"
while choice.lower()== "y":
    #Get input from the user
    monthlyInvestment = float(input("Enter monthly investment: \t"))
    yearly_interest_rate = float(input("Enter yearly interst : \t "))
    years = int(input("Enter number of years : "))

    #convert yearly values to monthly values
    monthly_interst_rate = yearly_interest_rate/12/100
    months = years* 12

    #Calculate the Future Value
    future_value = 0
    for i in range(months):
        future_value = future_value + monthlyInvestment
        monthly_interst_amount = future_value * monthly_interst_rate
        future_value = future_value + monthly_interst_amount
        print(future_value)


    #Format and display the result
    print("Future value : \t\t\t"+ locale.currency(future_value, grouping=True))
    print()

    choice = input("Continue ? (y or n)")
    print()

print("Good BYE!!!!!!!!")
