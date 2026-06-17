import random

LEVELS = {"1":[0,9],"2":[10,99],"3":[100,999]}

#GOOD
def difficulty(levels):
    diff = input("Enter Level 1, 2, 3: ")
    while diff not in levels:
        print("Error: Invalid input!\n")
        diff = input("Enter Level 1, 2, 3: ")
    return diff

#GOOD
def num_of_questions():
    while True:
        try:
            questions = int(input("Enter number of questions to ask: 3 to 10: "))
            if questions <= 10 and questions >= 3:
                return questions
            print("ERROR: Please enter an integer value between 3 and 10!\n")
        except:
            print("ERROR: Please enter an integer value between 3 and 10!\n")

#GOOD
def create(levels,hardness):
    num = random.randint(levels[hardness][0], levels[hardness][1])
    return num

#GOOD
def check(num1,num2):
    for i in range(3):
        try:
            user = int(input(f"{num1} + {num2} = "))
            if num1+num2 == user:
                return "CORRECT!!!\n",1
            print("WRONG!!!\n")
        except:
            print("WRONG!!!\n")
    return f"Correct Answer: {num1} + {num2} = {num1+num2}\n",0


def main(levels):
    score = 0
    level = difficulty(levels)
    amount = num_of_questions()
    for i in range(amount):
        num1 = create(levels,level)
        num2 = create(levels,level)
        output,correct = check(num1,num2)
        print(output)
        score += correct
    print(f"You got {score} out of {amount} questions correct: {100*score/amount:.2f}%")
        


main(LEVELS)
