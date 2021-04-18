from prac_06.guitar import Guitar
guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]
print("My guitars!")
while True:
    name = input("Name: ")
    if name == "":
        break
    year = input("Year: ")
    cost = input("Cost: ").strip("$")
    next_guitar = Guitar(name, int(year), float(cost))
    guitars.append(next_guitar)
    print("{} added".format(next_guitar))
    print()
print()
print("... snip ...")
print()
print("These are my guitars: ")
for i, guitar in enumerate(guitars, 1):
    print("Guitar {}: {} ({}), worth $ {:10,.2f} {}".format(i, guitar.name, guitar.year, guitar.cost,
                                                            "(vintage)" if guitar.is_vintage() else ""))
