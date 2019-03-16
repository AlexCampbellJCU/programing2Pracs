"""Alexander Campbell"""
min_length = 5
password = input("Please enter a password with a minimum of 5 Characters- ")
while len(password) < min_length:
    password = input("Please enter a password with a minimum of 5 Characters- ")
stars = "*" * len(password)
print(stars)