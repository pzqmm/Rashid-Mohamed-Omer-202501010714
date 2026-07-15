import utils

def main():
    name = input("Customer name: ")
    coffee = int(input("Coffee quantity: "))
    tea = int(input("Tea quantity: "))
    sandwich = int(input("Sandwich quantity: "))

    total = utils.calculate_total(coffee, tea, sandwich)
    
    utils.print_receipt(name, coffee, tea, sandwich, total)

if __name__ == "__main__":
    main()
