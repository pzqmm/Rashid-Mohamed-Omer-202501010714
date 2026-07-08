def calculate_total(price, quantity):
    # Validate customer input to prevent negative or zero values
    if price <= 0:
        return "invalid price"
    if quantity <= 0:
        return "invalid quantity"
    
    # Calculate the total
    return price * quantity
