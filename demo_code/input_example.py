#program to convert lbs to kilos
#INPUT (getting the data that will be processed)
#Prompt user to enter weight in lbs

#PROCESSING
#Calculate kg from given lbs

#OUTPUT
#Print kg

valid = False

pounds = input("Please enter weight in pounds.\n")
while valid == False:
    try:
        pounds = float(pounds)
        valid = True
    except:
        pounds = input("Please enter weight in pound AS A NUMBER.\n")



kilo = pounds*0.45359237
kilo =round(kilo,2)
print(pounds,"lbs in kilograms is",kilo,"kg.")