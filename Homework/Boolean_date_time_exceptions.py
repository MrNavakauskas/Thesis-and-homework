# Write a program that:
# • Allow the user to enter the desired date and time (eg birthday)
# • Calculate and print the elapsed time since the entered date and time:
# • Years
# • Months
# • Days
# • Hours
# • Minutes
# • Seconds
# • Because only days and seconds, years, months, etc. can be accurately calculated. calculate approximately.

import datetime

inp = input("Enter the year (YYYY-MM-DD HH:MM:SS): ")

inp_data = datetime.datetime.strptime(inp, "%Y-%m-%d %X")
now = datetime.datetime.now()
difr = now - inp_data

print("Years have passed: ", difr.days // 365)
print("Months have passed: ", round(difr.days / 365 * 12))
print("Weeks have passed: ", difr.days // 7)
print("Days have passed : ", difr.days)
print("Hours have passed: ", round(difr.total_seconds() / 3600))
print("Minutes have passed: ", round(difr.total_seconds() / 60))
print("Seconds have passed: ", round(difr.total_seconds()))
