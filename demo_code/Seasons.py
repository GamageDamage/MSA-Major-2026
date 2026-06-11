#Create a decision structure to determine the season:
# Winter, spring summer, fall
#Ask the user to enter the number of the month. Month must be 1 - 12
#output the season

#Winter:december, january, febuary. Spring:march, april, may.Summer: june, july, augest. Fall: sectember, october, november

def main():
    seasons = {
            12:"Winter",
            1:"Winter",
            2:"Winter",
            3:"Spring",
            4:"Spring",
            5:"Spring",
            6:"Summer",
            7:"Summer",
            8:"Summer",
            9:"Fall",
            10:"Fall",
            11:"Fall"
            
                    }
    while True:
        try:
            month = int(input("Enter the number of the month: \n"))
            if month > 12 or month < 1:
                print("Please enter a valid number.")
                continue
            break
        except:
            print("Please enter a number.")

    
    print(f"In month {month}, the season is {seasons[month]}.")
        



main()