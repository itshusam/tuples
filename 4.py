def print_order_details(orders):
    for i, order in enumerate(orders, start=1):
        customer_name, product, quantity = order
        print(f"Order {i}:")
        print(f"Customer: {customer_name}")
        print(f"Product: {product}")
        print(f"Quantity: {quantity}")
        print()  


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    
]


print_order_details(orders)