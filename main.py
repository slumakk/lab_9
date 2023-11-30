import pymongo

# Підключення до сервера MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Створення бази даних
db = client["eshop"]

# Створення колекції (еквівалент таблиці в реляційних базах даних)
customers = db["customers"]
products = db["products"]
orders = db["orders"]

# Додавання документів (еквівалент записів в таблиці)
products_data = {
    "name": "Кросівки для бігу",
    "description": "Легкі та зручні кросівки для активного способу життя.",
    "price": 80,
    "category": "взуття",
    "sizes": { "41": 10, "42": 15, "43": 20 },
    "colors": ["сірий", "зелений", "рожевий"]
  }
customer_data = {
    "name": "Мекола Сидоренко",
    "email": "mekola@example.com",
    "address": "вул. Пса Патрона, 23",
    "phone": "+380955550011"
  }

customer_data_2 = {
    "name": "Васелько Григорович",
    "email": "vaselko@example.com",
    "address": "пр. Центральний, 78",
    "phone": "+380988889988"
  }

# Вставка документів
products.insert_one(products_data)
customers.insert_one(customer_data)
customers.insert_one(customer_data_2)

# Зчитування документів
for document in customers.find():
    print(document)

# Оновлення документа
new_data = {"$set": {"address": "вул. Байденська, 44"}}
customers.update_one(customer_data, new_data)

new_data = {"$set": {"sizes": { "41": 10, "42": 15, "43": 20 }}}
products.update_one(products_data, new_data)

# Видалення документа
customers.delete_one(customer_data_2)

# Зчитування документів після оновлення та видалення
print("Після оновлення та видалення:")
for document in customers.find():
    print(document)

# Закриття підключення
client.close()
