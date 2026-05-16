import main
from models import TechStore


def set_inputs(monkeypatch, responses):
    iterator = iter(responses)

    def fake_input(_prompt=""):
        try:
            return next(iterator)
        except StopIteration as exc:
            raise AssertionError("Not enough test inputs provided.") from exc

    monkeypatch.setattr("builtins.input", fake_input)


def test_add_product_command_adds_new_product(monkeypatch):
    store = TechStore("CLI Store")
    set_inputs(monkeypatch, ["Mouse", "Peripherals", "25.50", "3"])

    main.add_product_command(store)

    product = store.find_product("Mouse")
    assert product is not None
    assert product["category"] == "Peripherals"
    assert product["price"] == 25.5
    assert product["quantity"] == 3


def test_add_product_command_retries_after_invalid_numeric_input(monkeypatch):
    store = TechStore("CLI Store")
    set_inputs(monkeypatch, ["Mouse", "Peripherals", "invalid", "25", "-2", "4"])

    main.add_product_command(store)

    product = store.find_product("Mouse")
    assert product is not None
    assert product["price"] == 25.0
    assert product["quantity"] == 4


def test_sell_product_command_reduces_quantity(monkeypatch):
    store = TechStore("CLI Store")
    store.add_product("Mouse", "Peripherals", 30, 5)
    set_inputs(monkeypatch, ["Mouse", "2"])

    main.sell_product_command(store)

    assert store.find_product("Mouse")["quantity"] == 3


def test_sell_product_command_shows_error_when_product_is_missing(monkeypatch, capsys):
    store = TechStore("CLI Store")
    set_inputs(monkeypatch, ["Mouse", "2"])

    main.sell_product_command(store)
    output = capsys.readouterr().out

    assert "продуктът 'Mouse' не е намерен" in output


def test_sell_product_command_shows_error_when_quantity_exceeds_stock(monkeypatch, capsys):
    store = TechStore("CLI Store")
    store.add_product("Mouse", "Peripherals", 30, 2)
    set_inputs(monkeypatch, ["Mouse", "5"])

    main.sell_product_command(store)
    output = capsys.readouterr().out

    assert "налични са само 2 бр." in output
    assert "поиска 5 бр." in output
    assert store.find_product("Mouse")["quantity"] == 2


def test_restock_product_command_increases_quantity(monkeypatch):
    store = TechStore("CLI Store")
    store.add_product("Mouse", "Peripherals", 30, 2)
    set_inputs(monkeypatch, ["Mouse", "5"])

    main.restock_product_command(store)

    assert store.find_product("Mouse")["quantity"] == 7


def test_restock_product_command_shows_error_when_product_is_missing(monkeypatch, capsys):
    store = TechStore("CLI Store")
    set_inputs(monkeypatch, ["Mouse", "5"])

    main.restock_product_command(store)
    output = capsys.readouterr().out

    assert "Неуспешно зареждане" in output
    assert "продуктът 'Mouse' не е намерен" in output


def test_remove_product_command_deletes_product(monkeypatch):
    store = TechStore("CLI Store")
    store.add_product("Mouse", "Peripherals", 30, 2)
    set_inputs(monkeypatch, ["Mouse"])

    main.remove_product_command(store)

    assert store.find_product("Mouse") is None


def test_remove_product_command_shows_error_when_product_is_missing(monkeypatch, capsys):
    store = TechStore("CLI Store")
    set_inputs(monkeypatch, ["Mouse"])

    main.remove_product_command(store)
    output = capsys.readouterr().out

    assert "Неуспешно премахване" in output
    assert "продуктът 'Mouse' не е намерен" in output


def test_search_command_shows_only_matching_products(monkeypatch, capsys):
    store = TechStore("CLI Store")
    store.add_product("Mouse", "Peripherals", 30, 2)
    store.add_product("Keyboard", "Peripherals", 80, 1)
    set_inputs(monkeypatch, ["mou"])

    main.search_command(store)
    output = capsys.readouterr().out

    assert "Mouse" in output
    assert "Keyboard" not in output


def test_low_stock_command_filters_products(capsys):
    store = TechStore("CLI Store")
    store.add_product("Mouse", "Peripherals", 30, 2)
    store.add_product("Keyboard", "Peripherals", 80, 10)

    main.low_stock_command(store, "lowstock 5")
    output = capsys.readouterr().out

    assert "Mouse" in output
    assert "Keyboard" not in output


def test_calculate_command_prints_total_value(capsys):
    store = TechStore("CLI Store")
    store.add_product("Laptop", "Computers", 1000, 2)
    store.add_product("Mouse", "Peripherals", 50, 4)

    main.calculate_command(store)
    output = capsys.readouterr().out

    assert "2200.00" in output


def test_clear_command_no_keeps_products(monkeypatch):
    store = TechStore("CLI Store")
    store.add_product("Laptop", "Computers", 1000, 1)
    set_inputs(monkeypatch, ["no"])

    main.clear_command(store)

    assert len(store.products) == 1


def test_clear_command_yes_clears_products(monkeypatch):
    store = TechStore("CLI Store")
    store.add_product("Laptop", "Computers", 1000, 1)
    set_inputs(monkeypatch, ["yes"])

    main.clear_command(store)

    assert store.products == []


def test_run_dispatches_loadexample(monkeypatch):
    called = {"count": 0}

    def fake_load_example_data(_store):
        called["count"] += 1

    monkeypatch.setattr(main, "load_example_data", fake_load_example_data)
    set_inputs(monkeypatch, ["loadexample", "exit"])

    main.run()

    assert called["count"] == 1


def test_run_handles_keyboard_interrupt_gracefully(monkeypatch, capsys):
    def raise_interrupt(_prompt=""):
        raise KeyboardInterrupt

    monkeypatch.setattr("builtins.input", raise_interrupt)

    main.run()
    output = capsys.readouterr().out

    assert "CTRL+C" in output
