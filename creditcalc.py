from math import ceil


def payment(principal, months):
    return ceil(principal / months)


def number_monthly_payments(principal, pay):
    return ceil(principal / pay)


def last_payment(principal, periods, pay):
    return principal - (periods - 1) * pay


def countable(num):
    if num == 1:
        return 'month'
    return 'months'


loan_principal = float(input("Enter the loan principal: "))
type_step = input("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment: """)

if type_step == 'm':
    loan_monthly_payments = float(input("Enter the monthly payment: "))
    nmp = number_monthly_payments(loan_principal, loan_monthly_payments)
    print()
    print(f"It will take {nmp} {countable(nmp)} to repay the loan")
elif type_step == 'p':
    periods = int(input("Enter the number of months: "))
    monthly_payments = payment(loan_principal, periods)
    if loan_principal % periods == 0:
        print(f"Your monthly payment = {monthly_payments}")
    else:
        last_payment = last_payment(loan_principal, periods, monthly_payments)
        print(f"Your monthly payment = {monthly_payments} and the last payment = {last_payment}.")
