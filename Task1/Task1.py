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

    # Apply app order discount
    if is_app_order:
        total_cost *= 0.75

    return round(total_cost, 2)


def main():
    print("BPP Pizza Price Calculator")
    print("==========================")

    # Get user input with validation
    while True:
        try:
            num_pizzas = int(input("How many pizzas ordered? "))
            if num_pizzas < 0:
                raise ValueError("Please enter a positive integer!")
            break
        except ValueError:
            print("Please enter a number!")

    is_delivery = input("Is delivery required? (y/n) ").lower() == "y"

    is_tuesday = input("Is it Tuesday? (y/n) ").lower() == "y"

    is_app_order = input("Did the customer use the app? (y/n) ").lower() == "y"

    # Calculate and display total price if input is valid
    total_price = calculate_total_price(is_tuesday, num_pizzas, is_delivery, is_app_order)
    if total_price is not None:
        print(f"\nTotal Price: £{total_price}.")


if __name__ == "__main__":
    main()
