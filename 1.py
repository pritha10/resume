def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

def NAND(a, b):
    return not (a and b)

def NOR(a, b):
    return not (a or b)

def XOR(a, b):
    return a != b

def XNOR(a, b):
    return a == b

# Display menu and take inputs
print("Logical Gates Simulation")
print("1. AND\n2. OR\n3. NOT\n4. NAND\n5. NOR\n6. XOR\n7. XNOR")
choice = int(input("Choose a gate to simulate (1-7): "))

# Handle different cases
if choice == 1:
    a = int(input("Enter     first input (0 or 1): "))
    b = int(input("Enter second input (0 or 1): "))  
    print(f"AND({a}, {b}) = {int(AND(a, b))}")
elif choice == 2:
    a = int(input("Enter first input (0 or 1): "))
    b = int(input("Enter second input (0 or 1): "))
    print(f"OR({a}, {b}) = {int(OR(a, b))}")
elif choice == 3:
    a = int(input("Enter input (0 or 1): "))
    print(f"NOT({a}) = {int(NOT(a))}")
elif choice == 4:
    a = int(input("Enter first input (0 or 1): "))
    b = int(input("Enter second input (0 or 1): "))
    print(f"NAND({a}, {b}) = {int(NAND(a, b))}")
elif choice == 5:
    a = int(input("Enter first input (0 or 1): "))
    b = int(input("Enter second input (0 or 1): "))
    print(f"NOR({a}, {b}) = {int(NOR(a, b))}")
elif choice == 6:
    a = int(input("Enter first input (0 or 1): "))
    b = int(input("Enter second input (0 or 1): "))
    print(f"XOR({a}, {b}) = {int(XOR(a, b))}")
elif choice == 7:
    a = int(input("Enter first input (0 or 1): "))
    b = int(input("Enter second input (0 or 1): "))
    print(f"XNOR({a}, {b}) = {int(XNOR(a, b))}")
else:
    print("Invalid choice. Please choose a number between 1 and 7.")