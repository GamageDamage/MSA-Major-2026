def main():
    print("Search For String\n---------")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    key_word = "dog"
    start_index = 0
    num_of_dogs = 0
    while True:
        dog_index = sentence.find(key_word, start_index)
        if dog_index == -1:
            break
        else:
            num_of_dogs += 1
            start_index = dog_index+ 1
    print(f"There are {num_of_dogs} {key_word} in the sentence")

    ''' my_name = "evin"
    print(f"My name is {my_name.capitalize()}")


    last_name = "GAMAGE"
    print(f"My full name in lowercase is {my_name.lower()} {last_name.lower()}")


    my_name_title_case = "Evin"
    if my_name_title_case.lower() == my_name.lower():
        print("The names are the same.")
    else:
        print("The names are different.")

    print("\nUsing the Startswith() Method\n----------")
    print(f"{my_name} starts with K or k: {my_name.startswith("K") or my_name.startswith("k")}")
    if not my_name.lower().startswith("evi"):
        print(f"You spelled {my_name} incorrectly.")
    else:
        print(f"You spelled {my_name} correctly. ")


    search_letter = "v"
    print(f"The letter {search_letter} is at index {my_name.find(search_letter)} in {my_name}")

    for i in my_name:
        print(i)

    for letter_index in range(0,len(ny_name)):
        print(f"Letter {letter_index}: {my_name[letter_index]}")'''

    
main()