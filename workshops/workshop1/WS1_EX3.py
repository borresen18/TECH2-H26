import numpy as np


def tax(income):
    """
    Return the taxes owed for a given income.

    Parameters 
    ----------
    income
        gross income

    Returns
    -------
    Tax owed
    """

    if income < 300_000:
        t = 0
    elif income < 700_000:
        t = (income - 300_000)*0.2
    else:
        t = (400_000)*0.2 + 0.35 * (income - 700_000)

    return(t)

incomes = np.linspace(0,1200000,13)
taxes_loop = np.empty(13)

for i in range(13):
    taxes_loop[i] = tax(incomes[i])

net = incomes - taxes_loop

print("Gross Income |  Taxes  | Net Income")
print("-----------------------------------")
for i in range (13):
    print(f"{incomes[i]:12.0f} | {taxes_loop[i]:7.0f} | {net[i]:10.0f}")
