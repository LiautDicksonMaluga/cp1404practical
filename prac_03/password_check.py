MIN_LENGTH = 4


def main():
    password = get_password()
    print_password(password)


def get_password():
    password = str(input("What is your password: "))
    while len(password) < MIN_LENGTH:
        print("Password does not meet the minimum requirements")
        password = input("what is your password: ")
    return password


def print_password(password):
    for i in range(0, len(password)):
        print("*", end="")


main()
