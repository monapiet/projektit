from datetime import date

# Ask the user the year,month and the day they were born
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))

# User birthday
birthday = date(birth_year, birth_month, birth_day)

# Today
today = date.today()

# Calculate total days
age_days_total = (today - birthday).days

# Convert age to years, months and days
age_years = age_days_total // 365
age_months = (age_days_total % 365) // 30
age_days = (age_days_total % 365) % 30

# Print the age
print(f"You are {age_years} years, {age_months} months and {age_days} days old.")
