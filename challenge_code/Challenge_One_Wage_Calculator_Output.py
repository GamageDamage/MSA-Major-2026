#INPUTS: hourly wage and hours worked daily

#CALCULATE:
#WAGES before taxes
#TAXES
#WAGES after taxes

def get_input(user,max):
    while True:
        try:
            hours = float(input(f"Enter the {user}: "))
            if hours > max or hours < 0:
                print("Please enter a valid amount.\n")
                continue
            return hours
        except:
            print("Please enter in number form.\n")


hours = get_input("number of hours worked daily",24)
wage = get_input("hourly wage",float('inf'))


wage_before = round(wage*hours*350,2)
taxes = round(wage_before*.12,2)
wage_after = round(wage_before-taxes,2)

print(f"\nPay Advice\n-------------\nHours Worked: {hours}\nHourly Wage: ${wage}\nWages Befopre Taxes: ${wage_before}\nTax Amount: ${taxes}\nAnnual Wage After Taxes: ${wage_after}")







