def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Kan inte dividera med noll")
    return a / b

if __name__ == "__main__":
    print("=== RebTech Miniräknare ===")
    print("1. Addera")
    print("2. Subtrahera")
    print("3. Multiplicera")
    print("4. Dividera")
    
    choice = input("Välj operation (1/2/3/4): ")
    num1 = float(input("Ange första talet: "))
    num2 = float(input("Ange andra talet: "))
    
    if choice == '1':
        print(f"Resultat: {add(num1, num2)}")
    elif choice == '2':
        print(f"Resultat: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Resultat: {multiply(num1, num2)}")
    elif choice == '4':
        try:
            print(f"Resultat: {divide(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("Ogiltigt val!")
