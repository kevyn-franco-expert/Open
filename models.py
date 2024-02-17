class Product:
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.country_prices = {}
        self.country_discounts = {}
        self.quantity_discounts = []  # List of (quantity, discount, is_percentage)

    def __str__(self):
        return f'{self.name}'

    def set_country_price(self, country_code, price):
        try:
            if price < 0:
                raise ValueError("Price must be a non-negative number.")
            self.country_prices[country_code] = price
        except TypeError:
            print("Invalid type for price. It should be a number.")

    def set_country_discount(self, country_code, discount):
        try:
            if not 0 <= discount <= 100:
                raise ValueError("Discount must be between 0 and 100.")
            self.country_discounts[country_code] = discount
        except TypeError:
            print("Invalid type for discount. It should be a number.")

    def set_quantity_discount(self, quantity, discount, is_percentage=False):
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be a positive number.")
            if discount < 0 or (is_percentage and discount > 100):
                raise ValueError("Invalid discount value.")
            self.quantity_discounts.append((quantity, discount, is_percentage))
        except TypeError:
            print("Invalid type for quantity or discount. They should be numbers.")

    def get_price(self, country_code, quantity):
        price = self.country_prices.get(country_code, self.base_price)
        country_discount = self.country_discounts.get(country_code, 0)
        price_after_country_discount = price * (1 - country_discount / 100)

        total_discount = 0
        for qty_threshold, qty_discount, is_percentage in sorted(self.quantity_discounts, reverse=True):
            if quantity >= qty_threshold:
                if is_percentage:
                    price_after_country_discount *= (1 - qty_discount / 100)
                else:
                    total_discount = qty_discount
                break

        discounted_total = (price_after_country_discount * quantity) - total_discount
        return discounted_total / quantity if quantity > 0 else 0


class Cart:
    def __init__(self):
        self.products = []
        self.promo_code = None

    def add_product(self, product, quantity, country_code):
        try:
            if not isinstance(product, Product):
                raise TypeError("Invalid product type.")
            if quantity <= 0:
                raise ValueError("Quantity must be a positive number.")
            self.products.append((product, quantity, country_code))
        except Exception as e:
            print(f"Error adding product to cart: {e}")

    def set_promo_code(self, promo_code):
        self.promo_code = promo_code

    def calculate_total(self):
        try:
            total_before_promo = sum(product.get_price(country_code, quantity) * quantity
                                     for product, quantity, country_code in self.products)

            if self.promo_code and self.promo_code.is_applicable(total_before_promo):
                return max(total_before_promo - self.promo_code.discount, 0)

            return total_before_promo  # Ensure total is not negative
        except Exception as e:
            print(f"Error calculating total: {e}")
            return 0


class PromotionCode:
    def __init__(self, code, discount, minimum_amount):
        self.code = code
        self.discount = discount
        self.minimum_amount = minimum_amount

    def is_applicable(self, total_amount):
        try:
            if total_amount < 0:
                raise ValueError("Total amount must be a non-negative number.")
            return total_amount >= self.minimum_amount
        except TypeError:
            print("Invalid type for total amount. It should be a number.")
