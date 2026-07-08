# Import the function from the other file
from food_order import calculate_total

def main():
    try:
        price = float(input("Price (RM): "))
        quantity = int(input("Quantity: "))

        # Call the function and store the result
        total = calculate_total(price, quantity)

        # Check if the result is a string (error message) or a number to print
        if isinstance(total, str):
            print(total)
        else:
            print(f"Total Payment = RM {total:.2f}")
    except ValueError:
        print("invalid input")

if __name__ == "__main__":
    main()
