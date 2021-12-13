# Create an application that:
# • Allow the user to enter the year
# • Print "Lifting Year", if applicable
# • Print “Non-Traversing Year,” if applicable
# The leap year is every 4 years, except for the last age, which is lifted only every 400 years

years = int(input("Enter year: "))

if years % 400 == 0:
    print("Lifting year")
elif years % 100 == 0:
    print("Fixed year")
elif years % 4 == 0:
    print("Lifting year")
else:
    print("Fixed year")
