from tabulate import tabulate

from models import TechStore


DEMO_PRODUCTS = [
    ("Р›Р°РїС‚РѕРї Lenovo IdeaPad", "Р›Р°РїС‚РѕРїРё", 1499.00, 5),
    ("РЎРјР°СЂС‚С„РѕРЅ Samsung Galaxy A55", "РЎРјР°СЂС‚С„РѕРЅРё", 799.00, 8),
    ("РЎР»СѓС€Р°Р»РєРё Sony WH-CH520", "РђСѓРґРёРѕ", 119.00, 12),
    ("РњРѕРЅРёС‚РѕСЂ LG 27\"", "РњРѕРЅРёС‚РѕСЂРё", 429.00, 4),
    ("РљР»Р°РІРёР°С‚СѓСЂР° Redragon", "РџРµСЂРёС„РµСЂРёСЏ", 89.00, 2),
    ("РЎРјР°СЂС‚ С‡Р°СЃРѕРІРЅРёРє Huawei Watch Fit", "РќРѕСЃРёРјРё", 219.00, 3),
]


def print_products(title, products):
    print(f"\n{title}")
    if not products:
        print("РќСЏРјР° РїСЂРѕРґСѓРєС‚Рё Р·Р° РїРѕРєР°Р·РІР°РЅРµ.")
        return

    rows = []
    for product in products:
        rows.append(
            [
                product["name"],
                product["category"],
                f"{product['price']:.2f} Р»РІ.",
                product["quantity"],
            ]
        )

    print(tabulate(rows, headers=["РРјРµ", "РљР°С‚РµРіРѕСЂРёСЏ", "Р¦РµРЅР°", "РќР°Р»РёС‡РЅРѕСЃС‚"], tablefmt="github"))


def print_help():
    rows = [
        ["help", "РџРѕРєР°Р·РІР° СЃРїРёСЃСЉРє СЃ РІСЃРёС‡РєРё РєРѕРјР°РЅРґРё"],
        ["loadexample", "Р—Р°СЂРµР¶РґР° РїСЂРёРјРµСЂРЅРёС‚Рµ РїСЂРѕРґСѓРєС‚Рё (РёР·С‡РёСЃС‚РІР° С‚РµРєСѓС‰РёС‚Рµ)"],
        ["add product", "Р”РѕР±Р°РІСЏ РЅРѕРІ РїСЂРѕРґСѓРєС‚ РёР»Рё СѓРІРµР»РёС‡Р°РІР° РєРѕР»РёС‡РµСЃС‚РІРѕ РЅР° СЃСЉС‰РµСЃС‚РІСѓРІР°С‰"],
        ["sell product", "РџСЂРѕРґР°РІР° РєРѕР»РёС‡РµСЃС‚РІРѕ РѕС‚ РїСЂРѕРґСѓРєС‚"],
        ["restock product", "Р”РѕР±Р°РІСЏ РєРѕР»РёС‡РµСЃС‚РІРѕ РєСЉРј СЃСЉС‰РµСЃС‚РІСѓРІР°С‰ РїСЂРѕРґСѓРєС‚"],
        ["remove product", "РџСЂРµРјР°С…РІР° РїСЂРѕРґСѓРєС‚ РѕС‚ СЃРїРёСЃСЉРєР°"],
        ["list", "РџРѕРєР°Р·РІР° РїСЂРѕРґСѓРєС‚Рё, СЃРѕСЂС‚РёСЂР°РЅРё РїРѕ С†РµРЅР° (РІСЉР·С…РѕРґСЏС‰Рѕ)"],
        ["list desc", "РџРѕРєР°Р·РІР° РїСЂРѕРґСѓРєС‚Рё, СЃРѕСЂС‚РёСЂР°РЅРё РїРѕ С†РµРЅР° (РЅРёР·С…РѕРґСЏС‰Рѕ)"],
        ["lowstock [С‡РёСЃР»Рѕ]", "РџРѕРєР°Р·РІР° РїСЂРѕРґСѓРєС‚Рё СЃ РЅРёСЃРєР° РЅР°Р»РёС‡РЅРѕСЃС‚ (РїРѕ РїРѕРґСЂР°Р·Р±РёСЂР°РЅРµ РїРѕРґ 3)"],
        ["search", "РўСЉСЂСЃРё РїСЂРѕРґСѓРєС‚Рё РїРѕ РёРјРµ"],
        ["calculate", "РР·С‡РёСЃР»СЏРІР° РѕР±С‰Р° СЃС‚РѕР№РЅРѕСЃС‚ Рё СЃС‚Р°С‚РёСЃС‚РёРєР° Р·Р° РЅР°Р»РёС‡РЅРѕСЃС‚С‚Р°"],
        ["clear", "РР·С‡РёСЃС‚РІР° РІСЃРёС‡РєРё РїСЂРѕРґСѓРєС‚Рё"],
        ["exit", "РР·С…РѕРґ РѕС‚ РїСЂРёР»РѕР¶РµРЅРёРµС‚Рѕ"],
    ]
    print("\nРќР°Р»РёС‡РЅРё РєРѕРјР°РЅРґРё:")
    print(tabulate(rows, headers=["РљРѕРјР°РЅРґР°", "РћРїРёСЃР°РЅРёРµ"], tablefmt="github"))


def read_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("РЎС‚РѕР№РЅРѕСЃС‚С‚Р° РЅРµ РјРѕР¶Рµ РґР° Р±СЉРґРµ РїСЂР°Р·РЅР°. РћРїРёС‚Р°Р№ РѕС‚РЅРѕРІРѕ.")


def read_float(prompt, min_value=0):
    while True:
        raw_value = input(prompt).strip().replace(",", ".")
        try:
            value = float(raw_value)
        except ValueError:
            print("РњРѕР»СЏ, РІСЉРІРµРґРё РІР°Р»РёРґРЅРѕ С‡РёСЃР»Рѕ.")
            continue

        if value < min_value:
            print(f"РЎС‚РѕР№РЅРѕСЃС‚С‚Р° С‚СЂСЏР±РІР° РґР° Рµ >= {min_value}.")
            continue
        return value


def read_int(prompt, min_value=1):
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("РњРѕР»СЏ, РІСЉРІРµРґРё РІР°Р»РёРґРЅРѕ С†СЏР»Рѕ С‡РёСЃР»Рѕ.")
            continue

        if value < min_value:
            print(f"РЎС‚РѕР№РЅРѕСЃС‚С‚Р° С‚СЂСЏР±РІР° РґР° Рµ >= {min_value}.")
            continue
        return value


def load_example_data(store):
    store.clear_products()
    for name, category, price, quantity in DEMO_PRODUCTS:
        store.add_product(name, category, price, quantity)
    print(f"Р—Р°СЂРµРґРµРЅРё СЃР° {len(DEMO_PRODUCTS)} РїСЂРёРјРµСЂРЅРё РїСЂРѕРґСѓРєС‚Р°.")


def add_product_command(store):
    name = read_non_empty_text("РРјРµ РЅР° РїСЂРѕРґСѓРєС‚: ")
    category = read_non_empty_text("РљР°С‚РµРіРѕСЂРёСЏ: ")
    price = read_float("Р¦РµРЅР°: ", min_value=0)
    quantity = read_int("РљРѕР»РёС‡РµСЃС‚РІРѕ: ", min_value=0)

    try:
        result = store.add_product(name, category, price, quantity)
    except ValueError as error:
        print(f"Р“СЂРµС€РєР°: {error}")
        return

    if result == "created":
        print("РџСЂРѕРґСѓРєС‚СЉС‚ Рµ РґРѕР±Р°РІРµРЅ СѓСЃРїРµС€РЅРѕ.")
    else:
        print("РџСЂРѕРґСѓРєС‚СЉС‚ РІРµС‡Рµ СЃСЉС‰РµСЃС‚РІСѓРІР°. РћР±РЅРѕРІРµРЅРё СЃР° С†РµРЅР°, РєР°С‚РµРіРѕСЂРёСЏ Рё РєРѕР»РёС‡РµСЃС‚РІРѕ.")


def sell_product_command(store):
    name = read_non_empty_text("РРјРµ РЅР° РїСЂРѕРґСѓРєС‚ Р·Р° РїСЂРѕРґР°Р¶Р±Р°: ")
    quantity = read_int("РљРѕР»РёС‡РµСЃС‚РІРѕ Р·Р° РїСЂРѕРґР°Р¶Р±Р°: ", min_value=1)

    if store.sell_product(name, quantity):
        print("РџСЂРѕРґР°Р¶Р±Р°С‚Р° Рµ СѓСЃРїРµС€РЅР°.")
        return
    print("РџСЂРѕРґР°Р¶Р±Р°С‚Р° Рµ РЅРµСѓСЃРїРµС€РЅР° (Р»РёРїСЃРІР°С‰ РїСЂРѕРґСѓРєС‚ РёР»Рё РЅРµРґРѕСЃС‚Р°С‚СЉС‡РЅР° РЅР°Р»РёС‡РЅРѕСЃС‚).")


def restock_product_command(store):
    name = read_non_empty_text("РРјРµ РЅР° РїСЂРѕРґСѓРєС‚ Р·Р° Р·Р°СЂРµР¶РґР°РЅРµ: ")
    quantity = read_int("РљРѕР»РёС‡РµСЃС‚РІРѕ Р·Р° РґРѕР±Р°РІСЏРЅРµ: ", min_value=1)

    if store.restock_product(name, quantity):
        print("РќР°Р»РёС‡РЅРѕСЃС‚С‚Р° Рµ РѕР±РЅРѕРІРµРЅР° СѓСЃРїРµС€РЅРѕ.")
        return
    print("РќРµСѓСЃРїРµС€РЅРѕ Р·Р°СЂРµР¶РґР°РЅРµ (РїСЂРѕРґСѓРєС‚СЉС‚ РЅРµ Рµ РЅР°РјРµСЂРµРЅ).")


def remove_product_command(store):
    name = read_non_empty_text("РРјРµ РЅР° РїСЂРѕРґСѓРєС‚ Р·Р° РїСЂРµРјР°С…РІР°РЅРµ: ")
    if store.remove_product(name):
        print("РџСЂРѕРґСѓРєС‚СЉС‚ Рµ РїСЂРµРјР°С…РЅР°С‚ СѓСЃРїРµС€РЅРѕ.")
        return
    print("РџСЂРѕРґСѓРєС‚СЉС‚ РЅРµ Рµ РЅР°РјРµСЂРµРЅ.")


def list_products_command(store, descending=False):
    title = "РџСЂРѕРґСѓРєС‚Рё (СЃРѕСЂС‚РёСЂР°РЅРё РїРѕ С†РµРЅР°, РЅРёР·С…РѕРґСЏС‰Рѕ):" if descending else "РџСЂРѕРґСѓРєС‚Рё (СЃРѕСЂС‚РёСЂР°РЅРё РїРѕ С†РµРЅР°, РІСЉР·С…РѕРґСЏС‰Рѕ):"
    print_products(title, store.sort_by_price(descending=descending))


def search_command(store):
    query = read_non_empty_text("РўСЉСЂСЃРё РїРѕ РёРјРµ: ").lower()
    matches = []
    for product in store.products:
        if query in product["name"].lower():
            matches.append(product)
    print_products(f"Р РµР·СѓР»С‚Р°С‚Рё Р·Р° '{query}':", matches)


def low_stock_command(store, command):
    threshold = 3
    parts = command.split()
    if len(parts) > 1:
        try:
            threshold = int(parts[1])
            if threshold <= 0:
                print("РџСЂР°РіСЉС‚ С‚СЂСЏР±РІР° РґР° Рµ РїРѕР»РѕР¶РёС‚РµР»РЅРѕ С†СЏР»Рѕ С‡РёСЃР»Рѕ.")
                return
        except ValueError:
            print("РќРµРІР°Р»РёРґРµРЅ РїСЂР°Рі. РџСЂРёРјРµСЂ: lowstock 5")
            return

    low_stock = store.low_stock_products(threshold=threshold)
    print_products(f"РџСЂРѕРґСѓРєС‚Рё СЃ РЅР°Р»РёС‡РЅРѕСЃС‚ РїРѕРґ {threshold} Р±СЂ.:", low_stock)


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
        ["Р‘СЂРѕР№ СЂР°Р·Р»РёС‡РЅРё РїСЂРѕРґСѓРєС‚Рё", products_count],
        ["РћР±С‰ Р±СЂРѕР№ РЅР°Р»РёС‡РЅРё Р±СЂРѕР№РєРё", total_units],
        ["РЎСЂРµРґРЅР° РµРґРёРЅРёС‡РЅР° С†РµРЅР°", f"{average_price:.2f} Р»РІ."],
        ["РћР±С‰Р° СЃС‚РѕР№РЅРѕСЃС‚ РЅР° РЅР°Р»РёС‡РЅРѕСЃС‚С‚Р°", f"{total_value:.2f} Р»РІ."],
    ]

    print("\nРћР±РѕР±С‰РµРЅРёРµ:")
    print(tabulate(summary_rows, headers=["РџРѕРєР°Р·Р°С‚РµР»", "РЎС‚РѕР№РЅРѕСЃС‚"], tablefmt="github"))

    category_stats = {}
    for product in store.products:
        category = product["category"]
        if category not in category_stats:
            category_stats[category] = {"products": 0, "units": 0, "value": 0}

        category_stats[category]["products"] += 1
        category_stats[category]["units"] += product["quantity"]
        category_stats[category]["value"] += product["price"] * product["quantity"]

    if not category_stats:
        print("\nРќСЏРјР° РЅР°Р»РёС‡РЅРё РєР°С‚РµРіРѕСЂРёРё Р·Р° Р°РЅР°Р»РёР·.")
        return

    category_rows = []
    for category, stats in category_stats.items():
        category_rows.append(
            [
                category,
                stats["products"],
                stats["units"],
                f"{stats['value']:.2f} Р»РІ.",
            ]
        )

    print("\nРЎС‚Р°С‚РёСЃС‚РёРєР° РїРѕ РєР°С‚РµРіРѕСЂРёРё:")
    print(tabulate(category_rows, headers=["РљР°С‚РµРіРѕСЂРёСЏ", "Р‘СЂРѕР№ РїСЂРѕРґСѓРєС‚Рё", "РќР°Р»РёС‡РЅРё Р±СЂРѕР№РєРё", "РЎС‚РѕР№РЅРѕСЃС‚"], tablefmt="github"))


def clear_command(store):
    confirmation = input("РЎРёРіСѓСЂРµРЅ Р»Рё СЃРё, С‡Рµ РёСЃРєР°С€ РґР° РёР·С‡РёСЃС‚РёС€ РІСЃРёС‡РєРё РїСЂРѕРґСѓРєС‚Рё? (yes/no): ").strip().lower()
    if confirmation == "yes":
        store.clear_products()
        print("Р’СЃРёС‡РєРё РїСЂРѕРґСѓРєС‚Рё СЃР° РёР·С‡РёСЃС‚РµРЅРё.")
        return
    print("РћРїРµСЂР°С†РёСЏС‚Р° Рµ РѕС‚РєР°Р·Р°РЅР°.")


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
