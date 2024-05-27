
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
​
def main():
    number = int(input("Enter a number: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {number} is {factorial(number)}")
​
if __name__ == "__main__":
    main()
    