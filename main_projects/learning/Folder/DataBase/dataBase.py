################
#      КАК РАБОТАЕТ ДБ
#################
##################################################
"""
1) Создание курсора, благодаря которому мы сможем создавать запросы и т.д.
2) Создаем запрос на создание таблицы
3) Создаем запрос на создание стобцов
4) Создаем запрос на заполнение таблицы
5) Создаем запрос на закрытие таблицы
"""
#############
# Безопасные метод заполнения дб - это: query = """INSERT INTO твоя_таблицы (имя_стоблца, имя_столбцы)
#		VALUES (?, ?)""" - количество столбцов
#		cursor.execute(query, первая_переменная, вторая_переменная)
#
#############
############# Пример:
#
#query = """INSERT INTO users (login, password)
#		VALUES (?, ?)"""
#		cursor.execute(query, (self.log.text(), self.password.text()))
#
import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE Try')
# def DataBase(login, password, money):
cursor.execute("""CREATE TABLE IF NOT EXISTS Try
	(	
		login VARCHAR(30),
		password VARCHAR(30)
	)
	""")
# login = input("enter a login: ")
# password = input("enter a password: ")
data_list = [("omar090910", "omar090920")]
cursor.executemany('''INSERT INTO Try VALUES(?,?)''', data_list)
#cursor.execute('''INSERT INTO Try VALUES(
#	"omar090910",
#	"omar090920"
#	)''')
cursor.execute('SELECT * FROM Try')
print(cursor.fetchall())

# DataBase(input("Enter a login: "), input("Enter a password: ", "How much do you have money: ")
