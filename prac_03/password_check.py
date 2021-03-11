min_pass_length = 4


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    for i in range(0, len(password)):
        print("*", end="")


def get_password():
    password = input("Enter Password: ")
    while len(password) < min_pass_length:
        print("Password is too short. Must be at least 4 characters. Please enter a different password.")
        input("Enter Password: ")
    return password


main()
