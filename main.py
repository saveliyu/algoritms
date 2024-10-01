import sqlite3

con = sqlite3.connect('pisun.db')
cur = con.cursor()


go = True
print('Здравствуйте, это программа для записи данных в таблицу\nесли вы хотите выйти из нее введите в консоль "0"')
print('вводите данные в формате [имя, пол(0 - если женский, 1 - если мужской), возраст]')
while go:
    text = input()
    if text == "0":
        go = False
        break
    name, sex, old = text.split()
    cur.execute("""INSERT INTO users (name, sex, old, score) 
    VALUES (?, ?, ?, 0)""", (name, int(sex), int(old)))
    con.commit()
con.close()