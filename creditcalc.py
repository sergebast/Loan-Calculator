from math import ceil, pow, log, floor
import argparse
from sys import argv


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
    return floor(p)


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


def differentiated_payment(p: int, n: int, i: float) -> list:
    """
    Returns the calculating differentiated payments
    :param p: Loan principal
    :param n: Number of payments. This is usually the number of months in which repayments will be made
    :param i: Nominal interest rate
    :return: Calculating differentiated payments
    """
    return [ceil(p / n + (i * (p - (p * (k - 1) / n)))) for k in range(1, n + 1)]


def overpayment(p: int, sum_p: float) -> int:
    """
    Returns the calculating overpayment
    :param p: Loan principal
    :param sum_p: The sum of all payments
    :return: Calculating overpayment
    """
    return int(sum_p - p)


def err():
    """
    Returns an error
    :return: String "Incorrect parameters"
    """
    print("Incorrect parameters")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(exit_on_error=False)

    parser.add_argument('--type', choices=['diff', 'annuity'])
    parser.add_argument('--principal', type=int, default=0)
    parser.add_argument('--periods', type=int, default=0)
    parser.add_argument('--interest', type=float)
    parser.add_argument('--payment', type=int, default=0)

    try:
        args = parser.parse_args()

    except (argparse.ArgumentError, argparse.ArgumentTypeError, TypeError, ValueError):
        err()

    else:
        if all([args.interest is not None, len(argv) == 5]):
            i_ = args.interest / 12 / 100  # Nominal interest rate
            all_payment = 0

            if all([args.type == 'diff', args.payment == 0]):

                # calculating differentiated payments
                if all([args.principal > 0, args.periods > 0]):
                    ind = 1
                    D = differentiated_payment(args.principal, args.periods, i_)
                    for el in D:
                        print(f'Month {ind}: payment is {el}')
                        ind += 1
                    print()
                    all_payment = sum(D)

            elif args.type == 'annuity':
                # calculating the loan principal
                if all([args.payment > 0, args.periods > 0]):
                    args.principal = loan_principal(args.payment, args.periods, i_)
                    print(f'Your loan principal = {args.principal}!')
                    all_payment = args.payment * args.periods

                # calculating the monthly payment (the annuity payment)
                elif all([args.principal > 0, args.periods > 0]):
                    a_ = annuity_payment(args.principal, args.periods, i_)
                    print(f'Your annuity payment = {a_}!')
                    all_payment = a_ * args.periods

                # calculate how long it will take to repay a loan
                elif all([args.principal > 0, args.payment > 0]):
                    n_ = number_payments(args.principal, args.payment, i_)

                    if n_ < 12:
                        print(f'It will take {int(n_)} {singular_plural(n_, "month")} to repay this loan!')

                    else:
                        y_ = converted_months(n_)
                        if len(y_) == 1:
                            print(f'It will take {int(y_[0])} {singular_plural(n_, "year")} to repay this loan!')
                        else:
                            year = f'{int(y_[0])} {singular_plural(n_, "year")}'
                            month = f'{int(y_[1])} {singular_plural(n_, "month")}'
                            print(
                                f'It will take {year} and {month} to repay this loan!')

                    all_payment = args.payment * n_

            else:
                err()

            if all_payment > 0:
                op = overpayment(args.principal, all_payment)
                print(f'Overpayment = {op}')

        else:
            err()
