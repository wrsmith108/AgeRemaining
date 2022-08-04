# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#set max values
max_years = 90
max_months = 90 * 12
max_weeks = 90 * 52
max_days = 90 * 365

#calculate current values
age_months = int(age * 12)
age_weeks = int(age * 52)
age_days = int(age * 365)

print(f"You have {int(max_years - age)} years, {int(max_weeks - age_weeks)} weeks, and {int(max_months - age_months)} months left.")



