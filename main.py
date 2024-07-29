age = input("What is your current age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(f"You have {years_remaining} years, {months_remaining} months, {weeks_remaining} weeks, and {days_remaining} days left until you are 90 years old.")
