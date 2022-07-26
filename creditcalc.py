from math import ceil, pow, log


def annuity_payment(p: int, n: int, i: float) -> int:
    """
    Returns the monthly annuity payment
    :param p: Loan principal
    :param n: Number of payments. This is usually the number of months in which repayments will be made
    :param i: Nominal (monthly) interest rate
    :return a: Monthly annuity payment
    """
    a = (i * pow((1 + i), n)) / (pow((1 + i), n) - 1) * p
    return ceil(a)


def loan_principal(a: float, n: int, i: float) -> int:
    """
    Returns the loan principal
    :param a: Monthly annuity payment
    :param n: Number of payments. This is usually the number of months in which repayments will be made
    :param i: Nominal (monthly) interest rate
    :return p: Loan principal
    """
    p = a / (i * pow((1 + i), n) / (pow((1 + i), n) - 1))
    return ceil(p)


def number_payments(p: int, a: int, i: float) -> int:
    """
    Returns the number of payments
    :param p: Loan principal
    :param a: Monthly annuity payment
    :param i: Nominal (monthly) interest rate
    :return n: Number of payments
    """
    n = log((a / (a - i * p)), (1 + i))
    return ceil(n)


def converted_months(m: int) -> tuple:
    """
    Returns the converted number of months in years and months
    :param m: Number of months
    :return y: Number of years and months
    """
    if m % 12 == 0:
        y = m / 12,
    else:
        y = m / 12, m % 12

    return y


def singular_plural(num: int, word: str) -> str:
    """
    Returns the correct form of a noun
    :param num: Number of months or years
    :param word: 'Month' or 'year'
    :return: Correct word form
    """
    if num == 1:
        return word
    return word + 's'


type_ = input("""What do you want to calculate?
type "n" - for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" - for loan principal: """)

# calculating the number of monthly payments
if type_ == 'n':
    p_ = int(input("Enter the loan principal: "))
    a_ = int(input("Enter the monthly payment: "))
    i_ = float(input("Enter the loan interest: ")) / 12 / 100

    n_ = number_payments(p_, a_, i_)

    if n_ < 12:
        print(f'It will take {n_} {singular_plural(n_, "month")} to repay this loan!')

    else:
        y_ = converted_months(n_)
        if len(y_) == 1:
            print(f'It will take {y_[0]} {singular_plural(n_, "year")} to repay this loan!')
        else:
            year = f'{int(y_[0])} {singular_plural(n_, "year")}'
            month = f'{int(y_[1])} {singular_plural(n_, "month")}'
            print(
                f'It will take {year} and {month} to repay this loan!')

# calculating the monthly payment (the annuity payment)
elif type_ == 'a':
    p_ = int(input("Enter the loan principal: "))
    n_ = int(input("Enter the number of periods: "))
    i_ = float(input("Enter the loan interest: ")) / 12 / 100

    a_ = annuity_payment(p_, n_, i_)

    print(f'Your monthly payment = {a_}!')

# calculating the loan principal
elif type_ == 'p':
    a_ = float(input("Enter the annuity payment: "))
    n_ = int(input("Enter the number of periods: "))
    i_ = float(input("Enter the loan interest: ")) / 12 / 100

    p_ = loan_principal(a_, n_, i_)

    print(f'Your loan principal = {p_}!')
