"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
print("Enter Q to quit, enter any other key to calculate bonus.")
choice = input(">>> ").upper()
while choice != 'Q':
    sales = float(input("Enter sales: $"))
    if sales < 0:
        print("Invalid sales input.")
        pass
    elif sales < 1000:
        bonus = sales * 0.1
        print("The bonus is ${:.2f}".format(bonus))
    else:
        bonus = sales * 0.15
        print("The bonus is ${:.2f}".format(bonus))
    print("Enter Q to quit, enter any other key to calculate again.")
    choice = input(">>> ").upper()
print("Thank you")
