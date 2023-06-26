import datetime
print("----------------------------------")
print("agecalculator version 1.0")
print("----------------------------------")

# Get the
# user's birthday
myDay = input("Please enter the Day you were born: ")
myMonth = input("Please enter the Month you were born: ")
myYear = input("Please enter the Year you were born: ")

print("Your birthday is on " + str(myDay) + "-" + str(myMonth) + "-" + str(myYear))

# Calculating the user's age
myBirthday = datetime.date(int(myYear), int(myMonth), int(myDay))
today = datetime.date.today()
dayDiff = (today - myBirthday)

# Print the user's age
print("Your age is " + str(int(dayDiff.days / 365.25)) + " Years")
