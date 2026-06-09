def get_positve_float_input():
    while True:
        user = input("Please enter weight in pounds.\n")
        try:
            user = float(user)
            #check if weight is les than or equal to 0
            if user <= 0:
                print("ERROR: Enter a number greater that zero.")
                continue
            return user
        except:
            user = input("Please enter weight in pound AS A NUMBER.\n")



def main():
    pounds =  get_positve_float_input()
    kilo = pounds*0.45359237
    kilo =round(kilo,2)
    print(pounds,"lbs in kilograms is",kilo,"kg.")

main()