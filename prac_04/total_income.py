"""
CP1404/CP5632 Practical - Suggested Solution
Cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for int_months in range(1, months + 1):
        income = float(input("Enter income for month {!s}: ".format(int_months)))
        incomes.append(income)

    method_name(incomes, months)


def method_name(incomes, months):
    print("\nIncome Report\n-------------")
    total = 0
    for int_month in range(1, months + 1):
        income = incomes[int_month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(int_month, income, total))


main()