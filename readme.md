# Магазин за техника (Tech Store)

Конзолно Python приложение за управление на магазин за техника.

## Какво може приложението
- Добавяне на продукти
- Продажба на продукти
- Зареждане на наличност (restock)
- Премахване на продукт
- Търсене по име
- Сортиране по цена
- Проверка за ниска наличност
- Изчисляване на стойност на наличността и статистика
- Зареждане на примерни данни (`loadexample`)

## Структура
- `models.py` - бизнес логика (`TechStore`)
- `main.py` - CLI команди и интерактивен режим
- `tests/test_models.py` - unit тестове за модела
- `tests/test_cli.py` - тестове за командите (CLI)
- `requirements.txt` - зависимости

## Инсталация
1. (Препоръчително) Създай и активирай виртуална среда.
2. Инсталирай зависимостите:

```bash
python -m pip install -r requirements.txt
```

## Стартиране на приложението
```bash
python main.py
```

## Основни команди в приложението
- `help`
- `loadexample`
- `add product`
- `sell product`
- `restock product`
- `remove product`
- `list`
- `list desc`
- `lowstock` или `lowstock 5`
- `search`
- `calculate`
- `clear`
- `exit`

## Тестове
Проектът използва **pytest**.

### Стартиране на всички тестове
```bash
python -m pytest -v
```

### Стартиране само на модел тестовете
```bash
python -m pytest -v tests/test_models.py
```

### Стартиране само на CLI тестовете
```bash
python -m pytest -v tests/test_cli.py
```

### Какво покриват тестовете
- `tests/test_models.py`
  - добавяне/обновяване на продукт
  - валидации за невалидни данни
  - продажба, зареждане, премахване
  - сортиране, low stock, total value, clear
  - `loadexample` поведение
- `tests/test_cli.py`
  - вход/изход за командите
  - обработка на невалиден вход
  - проверка на изхода от `calculate`, `search`, `lowstock`
  - dispatch логика в `run()`
