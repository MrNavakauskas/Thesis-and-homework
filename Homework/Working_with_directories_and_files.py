# Create a mini-budget program that:
# • Allow the user to enter income or expenses (with a "-" sign)
# • Income and expenses would be stored in the list and the list in the pickle file
# (the entered data would not be lost after closing the program)
# • Display income and expenses already entered
# • Show the balance of entered income and expenses (add up all income and expenses)


import pickle

while True:
    try:
        with open("budget.pkl", "rb") as pickle_in:
            budget = pickle.load(pickle_in)
            ammount = 0
            print("--------List of entries :---------")
            for number, list1 in enumerate(budget):
                ammount += list1
                print(number + 1, list1)
            print("Budget balance", ammount)
            print("-------------------------------")
    except:
        print("The file could not be retrieved")
        budget = []
    print("To exit, leave the field blank and press ENTER")
    list2 = float(input("Enter income or expenses: "))
    if list2 == "":
        break
    budget.append(list2)

    try:
        with open("budget.pkl", "wb") as pickle_out:
            pickle.dump(budget, pickle_out)
    except:
        print("Failed to save file")
