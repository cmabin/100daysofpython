# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 1 yr = 365/52/12

# age_as_int = int(age)

age = int(age)

# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12
agedays = round(365 * age)
ageweeks = round(52 * age)
agemonths = round(12 * age)

olddays = round((365 * 90) - agedays)
oldweeks = round((52 * 90) - ageweeks)
oldmonths = round((12 * 90) - agemonths)

# message = (f"You have {olddays} days, {oldweeks} weeks, and {oldmonths} months left.")
# print(message)
print(f"You have {olddays} days, {oldweeks} weeks, and {oldmonths} months left.")