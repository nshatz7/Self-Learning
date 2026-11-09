#initalize variables
starting_salary = float(input("Enter your starting salary: "))
semi_annual_raise = 0.07
annual_investment_return = 0.04
cost = 1000000
down_payment = cost * 0.25
epsilon = 100 #margin of error
savings = 0

#testing if possible
savings = 0
salary = starting_salary

for i in range(1,37):
    savings+= savings * (annual_investment_return / 12)      
    savings+= salary / 12
    if i % 6 == 0:
        salary += salary * semi_annual_raise

if savings < down_payment - epsilon:
    print("Not possible in 36 months")
    quit()

#bisection search
count = 0
low = 0
high = 10000
work = False

while not work:
    count+= 1
    mid = (low + high) // 2 #integer division
    mid_percentage = ((low + high) / 2) * 0.0001
    savings = 0
    salary = starting_salary

    for i in range(1,37):
        savings+= savings * (annual_investment_return / 12)      
        savings+= (salary / 12) * mid_percentage

        if i % 6 == 0:
                    salary += salary * semi_annual_raise

    if savings < down_payment - epsilon:
        low = mid
    elif savings > down_payment + epsilon:
        high = mid
    else: #everything works, so print outcome
        work = True
        print("Best savings rate: ", f"{mid_percentage: .4f}")
        print("Steps in bisection search: ", count)

        



        





