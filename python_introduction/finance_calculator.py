# User input for financial details
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings
rate = 0.05
# Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * rate)

# Output Results
print("Your monthly savings are $" + str(monthly_savings))
print("Projected savings after one year, with interest, is: $" + str(projected_savings))
