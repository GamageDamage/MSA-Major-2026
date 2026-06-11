def main():
    a = 7
    b = 4

    if a > b:
        print(f"a = {a} is greater than b = {b}.")
    elif b> a:
        print(f"b = {b} is greater than a = {a}.")
    else:
        print(f"a = {a} and b = {b} are equal.") 
    #print the appropriate letter grade based on a test score
    #A 100 - 90, B 89 - 80, C 79 - 70, D 69 - 60, F less than 60

    test_score = 83
    print("\nGrade decision: ")
    if test_score <= 100 and test_score >= 90:
        print(f"{test_score} --> A")
    elif test_score < 90 and test_score >= 80:
        print(f"{test_score} --> B")
    elif test_score < 80 and test_score >= 70:
        print(f"{test_score} --> C")
    elif test_score < 70 and test_score >= 60:
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")

    print("\nGrade decision 2: ")
    if test_score >= 90:
        print(f"{test_score} --> A")
    elif test_score >= 80:
        print(f"{test_score} --> B")
    elif test_score >= 70:
        print(f"{test_score} --> C")
    elif test_score >= 60:
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")
main()