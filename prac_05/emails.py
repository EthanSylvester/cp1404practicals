email = input("Email: ")
email_and_names = {}
while email != "":
    name = email.split("@")[0].split(".")
    name = " ".join(name)
    name = name.title()
    confirm = input("Is your name {}? (Y/n) ".format(name)).lower()
    if confirm == "n":
        name = input("Name: ").title()
    elif confirm == "no":
        name = input("Name: ").title()
    email_and_names[name] = email
    email = input("Email: ")
for name, email in email_and_names.items():
    print("{} ({})".format(name, email))
