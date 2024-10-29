from db.models import CarItem, Order

# Симулированная база данных
cars_items = [
    CarItem(id=1, name="Погрузчик фронтальный SEM636F", description="крутой погрузчик", price=1000.0, available=True),
    CarItem(id=2, name="Smartphone", description="Latest model smartphone", price=800.0, available=True),
    CarItem(id=3, name="Tablet", description="Lightweight tablet", price=400.0, available=False),
]

orders = []