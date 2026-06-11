'''
print the initial outputs:"Vending machine"

create a list holding valid values:1,5,10,25
have a while loop until amount due is zero or less than it.

withen the loop:
    create a try statement for a valid input thats an int
        take the input of the coin,
        have an if statement checking if the coin is valid:
            if its valid subtract from the amount due

output change





'''
def main():
    due = 50
    #Use curly braces instead of brackets it's more optimized
    # Also I can't talk now
    valid = {1, 5, 10, 25}
    print("Vending Machine\n----------------")
    while due > 0:
        print(f"Amount Due: {due}")
        try:
            coin = int(input("Insert Coin:\n")) 
            if coin in valid:
                due -= coin
        except:
            continue
    print(f"Change Owed: {-1 * due}")

main()