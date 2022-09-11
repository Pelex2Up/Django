import sqlite3

# conn = sqlite3.connect('data.db') # создание бд
# cursor = conn.cursor() # создание объекта для взаимодействия с бд
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT) ''')
# cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES ('hello', 'world')''')
# conn.commit()
# cursor.execute('''SELECT*FROM tab_1''')
# k = cursor.fetchall()
# print(k)

conn = sqlite3.connect('patients.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_of_patients (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, 
last_name TEXT, age INTEGER, city TEXT)''')
first_name = input('Enter patients first name: ')
last_name = input('Enter patients last name: ')
age = int(input('Enter his age: '))
city = input('Enter the city from where he comes: ')
cursor.execute('''INSERT INTO tab_of_patients(first_name, last_name, age, city) VALUES (?, ?, ?, ?)''',
               (first_name, last_name, age, city,))
conn.commit()
cursor.execute('''SELECT * FROM tab_of_patients''')
congr = cursor.fetchall()
for i in congr:
    e = 0
    h = list(i)
    m = ' '.join(str(e) for e in h)
    print(m)