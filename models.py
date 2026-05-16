class TechStore:
    """Клас за управление на магазин за техника."""

    def __init__(self, store_name):
        self.store_name = store_name
        self.products = []

    def find_product(self, name):
        """Намира продукт по име (без значение от главни/малки букви)."""
        for product in self.products:
            if product["name"].lower() == name.lower():
                return product
        return None

    def add_product(self, name, category, price, quantity):
        """Добавя продукт в наличността или обновява съществуващ.

        Връща:
        - "created" при нов продукт
        - "updated" при съществуващ продукт
        """
        if not name.strip() or not category.strip():
            raise ValueError("Името и категорията не могат да бъдат празни.")
        if price < 0 or quantity < 0:
            raise ValueError("Цената и количеството трябва да са неотрицателни.")

        existing_product = self.find_product(name)
        if existing_product:
            existing_product["category"] = category
            existing_product["price"] = float(price)
            existing_product["quantity"] += int(quantity)
            return "updated"

        self.products.append(
            {
                "name": name,
                "category": category,
                "price": float(price),
                "quantity": int(quantity),
            }
        )
        return "created"

    def sell_product_status(self, name, quantity):
        """Продава количество от продукт и връща статус на операцията."""
        product = self.find_product(name)
        if not product:
            return "not_found"
        if quantity <= 0:
            return "invalid_quantity"

        if product["quantity"] < quantity:
            return "insufficient_stock"

        product["quantity"] -= quantity
        return "sold"

    def sell_product(self, name, quantity):
        """Продава количество от продукт. Връща True при успех, иначе False."""
        return self.sell_product_status(name, quantity) == "sold"

    def restock_product_status(self, name, quantity):
        """Добавя количество към съществуващ продукт и връща статус."""
        product = self.find_product(name)
        if not product:
            return "not_found"
        if quantity <= 0:
            return "invalid_quantity"

        product["quantity"] += quantity
        return "restocked"

    def restock_product(self, name, quantity):
        """Добавя количество към съществуващ продукт."""
        return self.restock_product_status(name, quantity) == "restocked"

    def remove_product_status(self, name):
        """Премахва продукт по име и връща статус."""
        product = self.find_product(name)
        if not product:
            return "not_found"

        self.products.remove(product)
        return "removed"

    def remove_product(self, name):
        """Премахва продукт по име."""
        return self.remove_product_status(name) == "removed"

    def sort_by_price(self, descending=False):
        """Връща списък с продукти, сортирани по цена."""
        return sorted(self.products, key=lambda product: product["price"], reverse=descending)

    def low_stock_products(self, threshold=3):
        """Връща продуктите, които са под зададения праг на наличност."""
        low_stock = []
        for product in self.products:
            if product["quantity"] < threshold:
                low_stock.append(product)
        return low_stock

    def total_inventory_value(self):
        """Изчислява общата стойност на наличността."""
        total_value = 0
        for product in self.products:
            total_value += product["price"] * product["quantity"]
        return total_value

    def total_units(self):
        """Връща общия брой налични бройки от всички продукти."""
        total = 0
        for product in self.products:
            total += product["quantity"]
        return total

    def clear_products(self):
        """Изчиства всички продукти от магазина."""
        self.products.clear()
