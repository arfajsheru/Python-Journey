# Restaurant Menu
menu = {
    "Pizza": 200,
    "Pasta": 150,
    "Salad": 120,
    "Burger": 180,
    "Coffee": 100
}

# Discount threshold and percentage
DISCOUNT_THRESHOLD = 500
DISCOUNT_PERCENTAGE = 10

# Greet the Customer
def greet_customer():
    print("\nWelcome to Python Restaurant!")
    print("Here's our menu:\n")
    for item, price in menu.items():
        print(f"{item}: Rs {price}")

# Take Order
def take_order():
    order_total = 0
    order_list = []
    while True:
        print("\nWhat would you like to order? (Enter 'done' to finish)")
        order_item = input("Item Name: ").capitalize()
        if order_item == 'Done':
            break
        elif order_item in menu:
            quantity = int(input(f"How many {order_item}s would you like? "))
            cost = menu[order_item] * quantity
            order_total += cost
            order_list.append((order_item, quantity, cost))
            print(f"Added {quantity} {order_item}(s) to your order. Subtotal: Rs {order_total}")
        else:
            print("Sorry, we don't have that item on the menu.")
    
    return order_list, order_total

# Apply Discount
def apply_discount(order_total):
    if order_total >= DISCOUNT_THRESHOLD:
        discount = (DISCOUNT_PERCENTAGE / 100) * order_total
        print(f"\nCongratulations! You've received a {DISCOUNT_PERCENTAGE}% discount of Rs {discount:.2f}.")
        order_total -= discount
    return order_total

# Generate Bill
def generate_bill(order_list, order_total):
    print("\n----- Final Bill -----")
    print("{:<10} {:<10} {:<10}".format("Item", "Quantity", "Cost"))
    for item, quantity, cost in order_list:
        print(f"{item:<10} {quantity:<10} Rs{cost}")
    
    # Apply discount before final total
    order_total = apply_discount(order_total)
    print("\nTotal Amount after Discount: Rs", round(order_total, 2))
    print("Thank you for dining with us! Please visit again.")

# Main Function
def main():
    greet_customer()
    order_list, order_total = take_order()
    if order_total > 0:
        generate_bill(order_list, order_total)
    else:
        print("No items ordered. Thank you for visiting!")

# Run the Program
if __name__ == "__main__":
    main()
