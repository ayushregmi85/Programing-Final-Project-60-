def calculate_total_price(is_tuesday, num_pizzas, is_delivery, is_app_order):
    pizza_price = 12
    delivery_cost = 2.5

    # Apply Tuesday discount
    if is_tuesday:
        pizza_price *= 0.5