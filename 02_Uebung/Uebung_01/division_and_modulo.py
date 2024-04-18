division_and_modulo.py

def main():

    print("Please enter the dividend (needs to be an integer):")
    dividend = int(input())  # Convert input to integer
    
    print("Please enter the divisor (needs to be an integer):")
    divisor = int(input())   # Convert input to integer
    
    # Perform division
    division_result = dividend / divisor
    print(f"Result of the division operation: {division_result}")
    
    # Perform modulo operation
    modulo_result = dividend % divisor
    print(f"Result of the modulo operation: {modulo_result}")

if __name__ == "__main__":
    main()
