from models import Product, Cart, PromotionCode

if __name__ == "__main__":

    print('#' * 100, '1. Primera Parte, Case 1')
    # Creation of Product A with different prices and discounts
    product_a = Product("Producto A", 50)  # Default price
    product_a.set_country_price("ES", 50)  # Spain
    product_a.set_country_price("GB", 55)  # United Kingdom
    product_a.set_country_price("IT", 55)  # Italy

    product_a.set_country_discount("GB", 10)  # 10% off GB
    product_a.set_country_discount("IT", 25)  # 25% discount on IT

    # Create carts for ES, GB and IT
    cart_es = Cart()
    cart_gb = Cart()
    cart_it = Cart()

    # Add 2 units of Product A to each cart
    cart_es.add_product(product_a, 2, "ES")
    cart_gb.add_product(product_a, 2, "GB")
    cart_it.add_product(product_a, 2, "IT")

    # Calculate and display totals for each cart
    try:
        total_es = cart_es.calculate_total()
        total_gb = cart_gb.calculate_total()
        total_it = cart_it.calculate_total()

        print(f"Total a pagar en ES: {total_es}€")  # Expected: €100
        print(f"Total a pagar en GB: {total_gb}€")  # Expected: €99
        print(f"Total a pagar en IT: {total_it}€")  # Expected: €82.5

    except Exception as e:
        print(f"Ocurrió un error: {e}")

    print('#' * 100, '1. Primera Parte, Case 2')
    # Create Product A and B with prices and discounts in Spain
    product_a = Product("Producto A", 50)
    product_a.set_country_price("ES", 50)  # Spain
    product_a.set_country_discount("ES", 10)  # 10% discount on ES

    product_b = Product("Producto B", 20)
    product_b.set_country_price("ES", 20)  # Spain

    # Create a promotional code
    code_prom_5 = PromotionCode("promo5", 5, 90)

    # Create carts for different scenarios
    cart_1 = Cart()
    cart_2 = Cart()

    # Add products to carts
    # Scenario 1: 1 unit of Product A and 1 unit of Product B
    cart_1.add_product(product_a, 1, "ES")
    cart_1.add_product(product_b, 1, "ES")

    # Scenario 2: 2 units of Product A and 1 unit of Product B
    cart_2.add_product(product_a, 2, "ES")
    cart_2.add_product(product_b, 1, "ES")

    # Apply the promotional code to both carts
    cart_1.set_promo_code(code_prom_5)
    cart_2.set_promo_code(code_prom_5)

    # Calculate and display totals for each scenario
    try:
        total_1 = cart_1.calculate_total()
        total_2 = cart_2.calculate_total()

        print(f"Total a pagar para el Escenario 1: {total_1}€")  # Expected: €65
        print(f"Total a pagar para el Escenario 2: {total_2}€")  # Calculate and view

    except Exception as e:
        print(f"Ocurrió un error: {e}")

    print('#' * 100, '2. Segunda Parte Parte')

    # Create Product A with quantity discount
    product_a = Product("Product A", 50)
    product_a.set_country_price("ES", 50)  # Spain
    product_a.set_country_discount("ES", 10)  # 10% discount on ES
    product_a.set_quantity_discount(3, 45, is_percentage=False)  # Fixed discount of €45 for 3 or more units

    # Create Product B with quantity discounts in sections
    product_b = Product("Product B", 1.5)
    product_b.set_country_price("ES", 1.5)  # Spain
    product_b.set_quantity_discount(10, 5, is_percentage=False)  # Fixed discount of €5 for 10 or more units
    product_b.set_quantity_discount(50, 10, is_percentage=True)  # 10% discount for 50 or more units
    product_b.set_quantity_discount(200, 20, is_percentage=True)  # 20% discount for 200 or more units

    # Create a promotional code
    promo_code_100 = PromotionCode("promo100", 100, 200)

    # Examples of carts with different combinations of products and quantities
    cart_combinations = [
        (1, 1),  # 1 unidad de A y 1 de B
        (3, 9),  # 3 unidades de A y 9 de B
        (3, 10),  # 3 unidades de A y 10 de B
        (3, 60),  # 3 unidades de A y 60 de B
        (4, 110),  # 4 unidades de A y 110 de B
        (6, 200)  # 6 unidades de A y 200 de B
    ]

    for qty_a, qty_b in cart_combinations:
        cart = Cart()
        cart.add_product(product_a, qty_a, "ES")
        cart.add_product(product_b, qty_b, "ES")
        cart.set_promo_code(promo_code_100)
        total = cart.calculate_total()
        print(f"Total a pagar para {qty_a} unidad(es) de A y {qty_b} unidad(es) de B: {total}€")
