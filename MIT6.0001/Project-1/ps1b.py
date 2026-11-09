#initalize variables
annual_salary = float(input("Enter your annual salary: ")) #takes their annual salary
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) #percent saved per month
total_cost = float(input("Enter the total cost of your dream home: ")) #cost of their dream home
semi_annual_raise = float(input("Enter your semi-annual raise, as a decimal: "))
current_savings = 0 #current savings (where they are starting)
down_payment = total_cost * 0.25
monthly_saved = (annual_salary / 12) * portion_saved
num_months = 0

#math to find how many months
while current_savings < down_payment:
    current_savings += monthly_saved + ((current_savings * 0.04) / 12)
    num_months += 1
    if num_months % 6 == 0:
        annual_salary = annual_salary + (annual_salary * semi_annual_raise) #changing their annual salary after the raise
        monthly_saved = (annual_salary / 12) * portion_saved #changing the monthly saved because of the raise

#print output
print(num_months)
