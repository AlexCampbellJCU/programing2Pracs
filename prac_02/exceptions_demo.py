try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator <= 0:
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?
#   When you type something other than a Number
# When will a ZeroDivisionError occur?
#   When denominator is 0
# Could you change the code to avoid the possibility of a ZeroDivisionError?
# While loop / Error check the denominator to prevent it getting to ZeroDivisionError
