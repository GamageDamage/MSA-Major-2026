#program to convert lbs to kilos
#INPUT (getting the data that will be processed)
#Prompt user to enter weight in lbs
#Validate that input is float
#if input is invalid, then reprompt until the input is valid

#PROCESSING
#Calculate kg from given lbs

#OUTPUT
#Print kg


pounds = input("Please enter weight in pounds.\n")

while True:
    try:
        pounds = float(pounds)
        #check if weight is les than or equal to 0
        if pounds <= 0:
            print("ERROR: Enter a number greater that zero.\n")
            continue
        break
    except:
        pounds = input("Please enter weight in pound AS A NUMBER.\n")



kilo = pounds*0.45359237
kilo =round(kilo,2)
print(pounds,"lbs in kilograms is",kilo,"kg.")