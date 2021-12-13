# Write a program that:
# • Allows you to enter a number
# • Display “Number is Even” if present
# • Display “Number is Odd” on the screen, if it is
# • Display “Number divided by 3” if the number is divided by three

nm = int(input("Enter number: "))

if nm % 2 == 0:
    print("The number entered is even!")
else:
    print("The number entered is odd!")

if nm % 3 == 0:
    print("Number entered divided by three")
