"""Alexander Campbell"""


def main():
    min_length = 5
    password = get_password(min_length)
    stars = star_func(password)
    print(stars)


def star_func(password):
    stars = "*" * len(password)
    return stars


def get_password(min_length):
    password = input("Please enter a password with a minimum of 5 Characters- ")
    while len(password) < min_length:
        password = input("Please enter a password with a minimum of 5 Characters- ")
    return password


main()
