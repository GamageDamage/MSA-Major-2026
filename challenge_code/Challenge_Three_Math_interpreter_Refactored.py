#get the input
#Validate the expression format
#Validate that x and z are int
#validate that y is an acceptable operater
#validate when y is division z isnt zero
#split the input based off of spaces
#have a list to 


#output
#print output as float


def main():
    repeat = "y"

    while repeat.lower() == "y":
        equation = input("Enter x,y, and z, where x and z are integers, and y is a math opperator, and all are seperated by spaces.\n")
        try:
            spaces = equation.split(" ")
            solution = float(eval(equation))
            print(solution)
            repeat = input("Would you like to continue(y/n):\n")
        except:
            print("ERROR: please seperate inputs with spaces, not input z as zero if using the division symbol, make sure x and z are both integers and/or enter a vlaid equation.")

main()