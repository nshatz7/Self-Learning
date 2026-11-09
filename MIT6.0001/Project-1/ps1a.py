#initalize variables
monthly_salary = float(input("Enter your annual salary: ")) / 12.0 #takes their annual salary and divides by 12 for monthly
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ")) #percent saved per month
total_cost = float(input("Enter the total cost of your dream home: ")) #cost of their dream hoem
current_savings = 0 #current savings (where they are starting)
down_payment = total_cost * 0.25
monthly_saved = monthly_salary * portion_saved
num_months = 0

#math to find how many months
while current_savings < down_payment:
    current_savings += monthly_saved + ((current_savings * 0.04) / 12)
    num_months += 1

#print output
print(num_months)

