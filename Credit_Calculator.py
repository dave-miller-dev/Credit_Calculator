import math

print('What do you want to calculate?')
print('type "n" - for count of months,')
print('type "a" - for count of annuity monthly payment,')
print('type "p" - for credit principal,')

choice = input()

if choice == 'n':
    print('Enter credit principal:')
    credit_principal = float(input())
    print('Enter annuity monthly payment:')
    monthly_payment = float(input())
    print('Enter credit interest:')
    credit_interest = (float(input()) / 100 / 12)
    base = 1 + credit_interest
    x = monthly_payment / (monthly_payment - credit_interest * credit_principal)
    count_of_months = math.log(x, base)
    if count_of_months > 12 and count_of_months % 12 != 0:
        years = count_of_months // 12
        months = count_of_months % 12
        if math.ceil(months) == 12:
            print('You need ', math.floor(years) + 1, 'years to repay this credit!')
        else:
            print('You need ', math.floor(years), ' years and ', math.ceil(months), ' months to repay this credit!')
    elif count_of_months > 12 and count_of_months % 12 == 0:
        years = count_of_months // 12
        print('You need ', round(years), 'years to repay this credit!')
    elif count_of_months < 12:
        print('You need ', count_of_months, ' months to repay this credit!')
elif choice == 'a':
    print('Enter credit principal:')
    credit_principal = float(input())
    print('Enter count of periods:')
    count_of_periods = float(input())
    print('Enter credit interest:')
    credit_interest = float(input()) / 100 / 12
    growth_count = (credit_interest * math.pow(1 + credit_interest, count_of_periods)) / (
                math.pow(1 + credit_interest, count_of_periods) - 1)
    monthly_payment = credit_principal * growth_count
    print('Your annuity payment = ', math.ceil(monthly_payment), '!')
if choice == 'p':
    print('Enter annuity monthly payment:')
    monthly_payment = float(input())
    print('Enter count of months:')
    count_of_periods = float(input())
    print('Enter credit interest:')
    credit_interest = float(input()) / 100 / 12
    growth_count = (credit_interest * math.pow(1 + credit_interest, count_of_periods)) / (
                math.pow(1 + credit_interest, count_of_periods) - 1)
    credit_principal = monthly_payment / growth_count
    print('Your credit principal = ', math.floor(credit_principal), '!')
