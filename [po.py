# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect("C:/Users/USER_17/Desktop/db")

# Создание курсора
cur = con.cursor()
print(cur)
# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT * FROM food""").fetchall()

# Вывод результатов на экран
for elem in result:
    print(elem)

con.close()