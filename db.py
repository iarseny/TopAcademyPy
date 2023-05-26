import sqlite3

db = sqlite3.connect("shop.db")
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,
            text TEXT,
            k INTEGER,
            price INTEGER)''')
db.commit()


while True:
    print("1)Добавить продукт")
    print("2)Убрать товар")
    print("3)Стоимость и колличество")
    print("4)Выйти")

    n = int(input())
    if n == 4:
        break
    elif n == 1:
        a = input("Товар: ")
        b = int(input("Колличество: "))
        d = int(input("Цена: "))
        cursor.execute("INSERT INTO users (text, k, price) VALUES (?, ?, ?)", (a, b, d))
        db.commit()
    elif n == 2:
        a = input("Какой товар: ")
        cursor.execute("DELETE FROM users WHERE text = ?", (a,))
        db.commit()
    elif n == 3:
        a = input("Какой товар: ")
        cursor.execute("SELECT * FROM users WHERE text = ?", (a,))
        last = cursor.fetchall()
        if len(last) != 0:
            print(last)
        else:
            print("Товара нет!")
        db.commit()




db.commit()
db.close()