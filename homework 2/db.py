import sqlite3

db = sqlite3.connect("db.db")
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                b BOOLEAN,
                name TEXT,
                price INTEGER)''')
db.commit()


while True:
    print("1)Выйти")
    print("2)Новое заведение")
    print("3)Узнать о заведении")
    print("4)Забронировать")
    n = int(input())
    if n == 1:
        break
    elif n == 2:
        name = input("Что за заведение: ")
        price = int(input("Цена: "))
        cursor.execute("INSERT INTO users (b, name, price) VALUES (?, ?, ?)", (False, name, price))
    elif n == 3:
        name = input("Введите заведение: ")
        cursor.execute("SELECT * FROM users WHERE name = ? AND b = FALSE", (name,))
        l = cursor.fetchall()
        for i in l:
            print(i[2], "стоит -", i[3])
        db.commit()
    elif n == 4:
        name = input("Введите заведение: ")
        cursor.execute("UPDATE users SET b = TRUE WHERE name = ?", (name,))
db.commit()
db.close()
