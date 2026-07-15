# 1. Answer below questions:

**1.1. Define the problem statement**
To build a Python program that automatically calculates a customer's bill for a cafe, replacing the current manual calculation process.

**1.2. What are the Inputs?**
* Customer name (string)
* Quantity of Coffee (integer)
* Quantity of Tea (integer)
* Quantity of Sandwich (integer)

**1.3. What are the outputs?**
A formatted receipt displaying the customer's name, item quantities, and the total bill in RM.

**1.4. What would be the typical process flow?**
Start -> Input customer details and quantities -> Calculate total amount based on fixed prices -> Print formatted receipt -> End.

**1.5. What are the constraints?**
* Input quantities must be integers (whole numbers).
* Prices for items are fixed (Coffee: 8.50, Tea: 6.00, Sandwich: 12.00).

# 2. How do you decompose the problem into smaller tasks?
* Task 1: Create a function to handle mathematical calculations for the total price.
* Task 2: Create a function to format and print the receipt.
* Task 3: Create a main module to capture user inputs and execute the functions.

# 3. Write a pseudocode
```text
START
    INPUT name
    INPUT coffee_qty
    INPUT tea_qty
    INPUT sandwich_qty
    
    total = (coffee_qty * 8.50) + (tea_qty * 6.00) + (sandwich_qty * 12.00)
    
    PRINT "===== RECEIPT ====="
    PRINT "Customer : ", name
    PRINT "Coffee   : ", coffee_qty
    PRINT "Tea      : ", tea_qty
    PRINT "Sandwich : ", sandwich_qty
    PRINT "-------------------"
    PRINT "Total    : RM ", total
    PRINT "==================="
END