from tabulate import tabulate

from models import TechStore


DEMO_PRODUCTS = [
    ("Лаптоп Lenovo IdeaPad", "Лаптопи", 1499.00, 5),
    ("Смартфон Samsung Galaxy A55", "Смартфони", 799.00, 8),
    ("Слушалки Sony WH-CH520", "Аудио", 119.00, 12),
    ("Монитор LG 27\"", "Монитори", 429.00, 4),
    ("Клавиатура Redragon", "Периферия", 89.00, 2),
    ("Смарт часовник Huawei Watch Fit", "Носими", 219.00, 3),
]


def print_products(title, products):
    print(f"\n{title}")
    if not products:
        print("Няма продукти за показване.")
        return

    rows = []
    for product in products:
        rows.append(
            [
                product["name"],
                product["category"],
                f"{product['price']:.2f} лв.",
                product["quantity"],
            ]
        )

    print(tabulate(rows, headers=["Име", "Категория", "Цена", "Наличност"], tablefmt="github"))


def print_help():
    rows = [
        ["help", "Показва списък с всички команди"],
        ["loadexample", "Зарежда примерните продукти (изчиства текущите)"],
        ["add product", "Добавя нов продукт или увеличава количество на съществуващ"],
        ["sell product", "Продава количество от продукт"],
        ["restock product", "Добавя количество към съществуващ продукт"],
        ["remove product", "Премахва продукт от списъка"],
        ["list", "Показва продукти, сортирани по цена (възходящо)"],
        ["list desc", "Показва продукти, сортирани по цена (низходящо)"],
        ["lowstock [число]", "Показва продукти с ниска наличност (по подразбиране под 3)"],
        ["search", "Търси продукти по име"],
        ["calculate", "Изчислява обща стойност и статистика за наличността"],
        ["clear", "Изчиства всички продукти"],
        ["exit", "Изход от приложението"],
    ]
    print("\nНалични команди:")
    print(tabulate(rows, headers=["Команда", "Описание"], tablefmt="github"))


def read_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Стойността не може да бъде празна. Опитай отново.")


def read_float(prompt, min_value=0):
    while True:
        raw_value = input(prompt).strip().replace(",", ".")
        try:
            value = float(raw_value)
        except ValueError:
            print("Моля, въведи валидно число.")
            continue

        if value < min_value:
            print(f"Стойността трябва да е >= {min_value}.")
            continue
        return value


def read_int(prompt, min_value=1):
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Моля, въведи валидно цяло число.")
            continue

        if value < min_value:
            print(f"Стойността трябва да е >= {min_value}.")
            continue
        return value


def load_example_data(store):
    store.clear_products()
    for name, category, price, quantity in DEMO_PRODUCTS:
        store.add_product(name, category, price, quantity)
    print(f"Заредени са {len(DEMO_PRODUCTS)} примерни продукта.")


def add_product_command(store):
    name = read_non_empty_text("Име на продукт: ")
    category = read_non_empty_text("Категория: ")
    price = read_float("Цена: ", min_value=0)
    quantity = read_int("Количество: ", min_value=0)

    try:
        result = store.add_product(name, category, price, quantity)
    except ValueError as error:
        print(f"Грешка: {error}")
        return

    if result == "created":
        print("Продуктът е добавен успешно.")
    else:
        print("Продуктът вече съществува. Обновени са цена, категория и количество.")


def sell_product_command(store):
    name = read_non_empty_text("Име на продукт за продажба: ")
    quantity = read_int("Количество за продажба: ", min_value=1)

    result = store.sell_product_status(name, quantity)
    if result == "sold":
        print("Продажбата е успешна.")
        return
    if result == "not_found":
        print(f"Неуспешна продажба: продуктът '{name}' не е намерен.")
        return
    if result == "insufficient_stock":
        available_quantity = store.find_product(name)["quantity"]
        print(
            f"Неуспешна продажба: налични са само {available_quantity} бр. "
            f"от '{name}', а поиска {quantity} бр."
        )
        return
    print("Неуспешна продажба: количеството трябва да е положително число.")


def restock_product_command(store):
    name = read_non_empty_text("Име на продукт за зареждане: ")
    quantity = read_int("Количество за добавяне: ", min_value=1)

    result = store.restock_product_status(name, quantity)
    if result == "restocked":
        print("Наличността е обновена успешно.")
        return
    if result == "not_found":
        print(f"Неуспешно зареждане: продуктът '{name}' не е намерен.")
        return
    print("Неуспешно зареждане: количеството трябва да е положително число.")


def remove_product_command(store):
    name = read_non_empty_text("Име на продукт за премахване: ")
    if store.remove_product_status(name) == "removed":
        print("Продуктът е премахнат успешно.")
        return
    print(f"Неуспешно премахване: продуктът '{name}' не е намерен.")


def list_products_command(store, descending=False):
    title = "Продукти (сортирани по цена, низходящо):" if descending else "Продукти (сортирани по цена, възходящо):"
    print_products(title, store.sort_by_price(descending=descending))


def search_command(store):
    query = read_non_empty_text("Търси по име: ").lower()
    matches = []
    for product in store.products:
        if query in product["name"].lower():
            matches.append(product)
    print_products(f"Резултати за '{query}':", matches)


def low_stock_command(store, command):
    threshold = 3
    parts = command.split()
    if len(parts) > 1:
        try:
            threshold = int(parts[1])
            if threshold <= 0:
                print("Прагът трябва да е положително цяло число.")
                return
        except ValueError:
            print("Невалиден праг. Пример: lowstock 5")
            return

    low_stock = store.low_stock_products(threshold=threshold)
    print_products(f"Продукти с наличност под {threshold} бр.:", low_stock)


def calculate_command(store):
    products_count = len(store.products)
    total_units = store.total_units()
    total_value = store.total_inventory_value()
    average_price = 0
    if products_count > 0:
        total_prices = 0
        for product in store.products:
            total_prices += product["price"]
        average_price = total_prices / products_count

    summary_rows = [
        ["Брой различни продукти", products_count],
        ["Общ брой налични бройки", total_units],
        ["Средна единична цена", f"{average_price:.2f} лв."],
        ["Обща стойност на наличността", f"{total_value:.2f} лв."],
    ]

    print("\nОбобщение:")
    print(tabulate(summary_rows, headers=["Показател", "Стойност"], tablefmt="github"))

    category_stats = {}
    for product in store.products:
        category = product["category"]
        if category not in category_stats:
            category_stats[category] = {"products": 0, "units": 0, "value": 0}

        category_stats[category]["products"] += 1
        category_stats[category]["units"] += product["quantity"]
        category_stats[category]["value"] += product["price"] * product["quantity"]

    if not category_stats:
        print("\nНяма налични категории за анализ.")
        return

    category_rows = []
    for category, stats in category_stats.items():
        category_rows.append(
            [
                category,
                stats["products"],
                stats["units"],
                f"{stats['value']:.2f} лв.",
            ]
        )

    print("\nСтатистика по категории:")
    print(tabulate(category_rows, headers=["Категория", "Брой продукти", "Налични бройки", "Стойност"], tablefmt="github"))


def clear_command(store):
    confirmation = input("Сигурен ли си, че искаш да изчистиш всички продукти? (yes/no): ").strip().lower()
    if confirmation == "yes":
        store.clear_products()
        print("Всички продукти са изчистени.")
        return
    print("Операцията е отказана.")


def run():
    store = TechStore("TechNova")
    print(f"Добре дошли в {store.store_name}!")
    print("Използвай команда `help`, за да видиш всички възможности.")

    try:
        while True:
            raw_command = input("\nВъведи команда: ").strip()
            if not raw_command:
                continue

            command = " ".join(raw_command.lower().split())

            if command in {"exit", "quit"}:
                print("Изход от приложението. До скоро!")
                break
            if command in {"help", "commands"}:
                print_help()
                continue
            if command == "loadexample":
                load_example_data(store)
                continue
            if command in {"add product", "add"}:
                add_product_command(store)
                continue
            if command in {"sell product", "sell"}:
                sell_product_command(store)
                continue
            if command in {"restock product", "restock"}:
                restock_product_command(store)
                continue
            if command in {"remove product", "remove"}:
                remove_product_command(store)
                continue
            if command == "list":
                list_products_command(store, descending=False)
                continue
            if command == "list desc":
                list_products_command(store, descending=True)
                continue
            if command.startswith("lowstock"):
                low_stock_command(store, command)
                continue
            if command == "search":
                search_command(store)
                continue
            if command == "calculate":
                calculate_command(store)
                continue
            if command == "clear":
                clear_command(store)
                continue

            print("Непозната команда. Напиши `help`, за да видиш валидните команди.")
    except KeyboardInterrupt:
        print("\nПриложението беше спряно от потребителя (CTRL+C). До скоро!")
    except EOFError:
        print("\nПолучен е край на входа. До скоро!")


if __name__ == "__main__":
    run()
