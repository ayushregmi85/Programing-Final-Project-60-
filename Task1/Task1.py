def calculate_total_price(is_tuesday, num_pizzas, is_delivery, is_app_order):
    pizza_price = 12
    delivery_cost = 2.5

    # Apply Tuesday discount
    if is_tuesday:
        pizza_price *= 0.5

    # Validate number of pizzas
    if num_pizzas < 0:
        print("Please enter a positive integer!")
        return None

    # Check if delivery is free (5 or more pizzas)
    if num_pizzas >= 5 and is_delivery:
        delivery_cost = 0

        # Calculate total pizza price
    total_pizza_price = pizza_price * num_pizzas

    # Calculate total cost with delivery
    total_cost = total_pizza_price + delivery_cost