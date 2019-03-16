out_file = open("name.txt", "w")
name = input("What is thy name? ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
print("your name is ", name)
in_file.close()

in_file = open("numbers.txt", "r")
line1 = int(in_file.readline())
line2 = int(in_file.readline())
print(line1 + line2)
in_file.close()

# Quick Program 3 extended - sum of all numbers
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()
