def convert():
    direction = input("Enter the conversion direction (1 : binary to decimal, octal, hexadecimal , 2 : decimal, octal, hexadecimal to binary): ")
    num = input("Enter the number: ")

    if direction == "1":
        num_type = input("Enter the type of the number to convert to (1 : decimal, 2 : octal, 3 : hexadecimal): ")
        if num_type == "1":
            return int(num, 2)
        elif num_type == "2":
            return oct(int(num, 2))[2:]
        elif num_type == "3":
            return hex(int(num, 2))[2:]
        else:
            return "Invalid type. Please enter either decimal, octal, or hexadecimal."
    elif direction == "2":
        num_type = input("Enter the type of the number to convert from (1 : decimal, 2 : octal, 3 : hexadecimal): ")
        if num_type == "1":
            return bin(int(num))[2:]
        elif num_type == "2":
            return bin(int(num, 8))[2:]
        elif num_type == "3":
            return bin(int(num, 16))[2:]
        else:
            return "Invalid type. Please enter either decimal, octal, or hexadecimal."
    else:
        return "Invalid direction. Please enter either 1 or 2."

print(convert())