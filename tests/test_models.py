import pytest

from main import DEMO_PRODUCTS, load_example_data
from models import TechStore


@pytest.fixture
def store():
    return TechStore("Test Store")


def test_add_product_creates_new_product(store):
    result = store.add_product("Laptop", "Computers", 1200.0, 3)

    assert result == "created"
    assert len(store.products) == 1
    assert store.products[0]["name"] == "Laptop"
    assert store.products[0]["quantity"] == 3


def test_add_product_updates_existing_product(store):
    store.add_product("Laptop", "Computers", 1200.0, 3)

    result = store.add_product("Laptop", "Premium Computers", 1300.0, 2)

    product = store.find_product("laptop")
    assert result == "updated"
    assert product is not None
    assert product["category"] == "Premium Computers"
    assert product["price"] == 1300.0
    assert product["quantity"] == 5


def test_add_product_rejects_invalid_data(store):
    with pytest.raises(ValueError):
        store.add_product("", "Computers", 1000, 1)

    with pytest.raises(ValueError):
        store.add_product("Laptop", "Computers", -1, 1)

    with pytest.raises(ValueError):
        store.add_product("Laptop", "Computers", 1000, -1)


def test_sell_product_success_and_failures(store):
    store.add_product("Phone", "Smartphones", 800, 4)

    assert store.sell_product("phone", 2) is True
    assert store.find_product("Phone")["quantity"] == 2
    assert store.sell_product("Phone", 3) is False
    assert store.sell_product("Missing", 1) is False
    assert store.sell_product("Phone", 0) is False


def test_restock_product(store):
    store.add_product("Mouse", "Peripherals", 30, 1)

    assert store.restock_product("mouse", 4) is True
    assert store.find_product("Mouse")["quantity"] == 5
    assert store.restock_product("Mouse", 0) is False
    assert store.restock_product("Missing", 3) is False


def test_remove_product(store):
    store.add_product("Keyboard", "Peripherals", 100, 2)

    assert store.remove_product("KEYBOARD") is True
    assert store.find_product("Keyboard") is None
    assert store.remove_product("Keyboard") is False


def test_sort_by_price(store):
    store.add_product("A", "Category", 300, 1)
    store.add_product("B", "Category", 100, 1)
    store.add_product("C", "Category", 200, 1)

    asc_names = [product["name"] for product in store.sort_by_price()]
    desc_names = [product["name"] for product in store.sort_by_price(descending=True)]

    assert asc_names == ["B", "C", "A"]
    assert desc_names == ["A", "C", "B"]


def test_low_stock_products(store):
    store.add_product("A", "Category", 10, 1)
    store.add_product("B", "Category", 10, 3)
    store.add_product("C", "Category", 10, 5)

    low_stock_names = [product["name"] for product in store.low_stock_products(threshold=4)]

    assert low_stock_names == ["A", "B"]


def test_totals(store):
    store.add_product("Laptop", "Computers", 1000, 2)
    store.add_product("Mouse", "Peripherals", 50, 4)

    assert store.total_units() == 6
    assert store.total_inventory_value() == 2200


def test_clear_products(store):
    store.add_product("Laptop", "Computers", 1000, 2)
    store.add_product("Mouse", "Peripherals", 50, 4)

    store.clear_products()

    assert store.products == []
    assert store.total_units() == 0
    assert store.total_inventory_value() == 0


def test_load_example_data_replaces_existing_products(store):
    store.add_product("Temporary", "Temp", 1, 1)

    load_example_data(store)

    assert len(store.products) == len(DEMO_PRODUCTS)
    demo_names = [name for name, _, _, _ in DEMO_PRODUCTS]
    loaded_names = [product["name"] for product in store.products]
    assert loaded_names == demo_names
