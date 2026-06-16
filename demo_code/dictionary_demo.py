def main():
    car_1 = {
        "make":"Ferrari",
        "model":"F-50"
        "year":2024
        "value":500000
        "engine size":4.8
    }
    print(f"\nGet all car info\n----------------")
    for key, value in car_1.items():
        print(f"{key}: {value}")

    car_2 = {"make":"Honda",
        "model":"Accord"
        "year":2024
        "value":18000
        "engine size": 2.4}

    dict_list = [car_1,car_2]

    print("\nDisplay information for all cars\n---------------------")

    for car in dict_list:
        for key, value in car.items():
            print(f"{key}: {value}")
        print("\n") 
    
    car_dict = {"Ferrari":car_1,"Accord":car_2}

    for make, car in car_dict.items():
        print(f"\n{make}")
        for key, value in car.items():
            print(f"{key}: {value}")
    print(f"{car_1}")

    key = "model"
    car_1.keys()
    print("Using try")
    try:
        print(f"{car_1[key]}")
    except:
        print(f"ERROR: Key '{key}' does not exist in the dictionary")

    print("Using if")
    if key not in car_1.keys():
        print(f"ERROR: Key '{key}' does not exist in the dictionary")
    else:
        print(f"{car_1[key]}")
    }