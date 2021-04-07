# Problem Set 1 ps1a
# Name: Yuyang Liu
# Collaborators:
# Time spent:


# Part A: House Hunting


annual_salary = float(input('Enter your annual salary: '))
# portion_saved 每个月固定留下的百分比月工资
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
# monthly_savings 每个月实际留下来的钱
monthly_savings = (annual_salary / 12) * portion_saved

total_cost = float(input('Enter the cost of your dream home: '))
portion_down_payment = 0.25 #25%
# down_payment 最低实付款
down_payment = total_cost * portion_down_payment

annual_return = 0.04
current_savings = 0.0

number_of_months = 0

while current_savings < down_payment:
    current_savings += monthly_savings + ((current_savings * annual_return) / 12)
    number_of_months += 1

print('Number of months: {}'.format(number_of_months))