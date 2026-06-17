def add_numbers(num_1:int,num_2:int,num_3:int) -> int:
    total = num_1+num_2+num_3
    return total


def main():
    a = 5 
    b = 4
    c = 3
    total = add_numbers(a,b,c)
    print(total)    
main()