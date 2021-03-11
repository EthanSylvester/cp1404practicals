min_pass_length = 4
password = input("Enter Password: ")
while len(password) < min_pass_length:
    print("Password is too short. Must be at least 4 characters. Please enter a different password.")
    input("Enter Password: ")
for i in range(0, len(password)):
    print("*", end="")
