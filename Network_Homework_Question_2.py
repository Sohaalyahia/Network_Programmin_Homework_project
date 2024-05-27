def binary_to_decimal(binary_str):
    # Initialize decimal value
    decimal_value = 0
    
    # Convert the binary string to decimal
    for digit in binary_str:
        decimal_value = decimal_value * 2 + int(digit)
    
    return decimal_value
​
def main():
    # Read the binary number from the user
    binary_str = input("Enter a binary number: ")
    
    # Validate the input to ensure it's a binary number
    if not all(char in '01' for char in binary_str):
        print("Invalid binary number.")
        return
    
    # Calculate the decimal equivalent
    decimal_value = binary_to_decimal(binary_str)
    
    # Display the result
    print(f"The decimal equivalent of binary {binary_str} is {decimal_value}")
​
if __name__ == "__main__":
    main()