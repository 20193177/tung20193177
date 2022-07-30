import sqlite3
import datetime
now = datetime.datetime.utcnow()

CREATE_INCOMES = "CREATE TABLE IF NOT EXISTS incomes (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"
CREATE_EXPENSES = "CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"
CREATE_LOAN = "CREATE TABLE IF NOT EXISTS loan (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"
CREATE_OTHER = "CREATE TABLE IF NOT EXISTS other (id INTEGER PRIMARY KEY,good TEXT, price INTEGER, date DATE);"



INSERT_INCOMES = "INSERT INTO incomes (good, price, date) VALUES(?,?,?);"
INSERT_EXPENSES = "INSERT INTO expenses (good, price, date) VALUES(?,?,?);"
INSERT_LOAN = "INSERT INTO loan (good, price, date) VALUES(?,?,?);"
INSERT_OTHER = "INSERT INTO other (good, price, date) VALUES(?,?,?);"


SELECT_ALL1 = "SELECT * FROM incomes;"
SELECT_ALL2 = "SELECT * FROM expenses;"
SELECT_ALL3 = "SELECT * FROM loan;"
SELECT_ALL4 = "SELECT * FROM other;"

SELECT_INCOMES = "SELECT * FROM incomes WHERE good = ? OR price = ? OR date = ?;"
SELECT_EXPENSES = "SELECT * FROM expenses WHERE good = ? OR price = ? OR date = ?;"
SELECT_LOAN = "SELECT * FROM loan WHERE good = ? OR price = ? OR date = ?;"
SELECT_OTHER = "SELECT * FROM other WHERE good = ? OR price = ? OR date = ?;"

DELETE_INCOMES = "DELETE FROM incomes WHERE good = ? AND price = ?;"
DELETE_EXPENSES = "DELETE FROM expenses WHERE good = ? AND price = ?;"
DELETE_LOAN = "DELETE FROM loan WHERE good = ? AND price = ?;"
DELETE_OTHER = "DELETE FROM other WHERE good = ? AND price = ?;"





###tạo bảng###
def create_tables():
    conn = sqlite3.connect('data.db')
    with conn:
        return conn.execute(CREATE_OTHER)

###Thêm value###

def insert_incomes(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_INCOMES, (good, price, date))
        conn.commit()
        c.close()


def insert_expenses(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_EXPENSES , (good, price, date))
        conn.commit()
        c.close()

def insert_loan(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_LOAN, (good, price, date))
        conn.commit()
        c.close()

def insert_other(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_OTHER, (good, price, date))
        conn.commit()
        c.close()

###SELECT_ALL###



def select_all_incomes():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL1)
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output





def select_all_expenses():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL2)
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_all_loan():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL3)
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_all_other():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL4)
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

###SELECT SPECIFIC###

def select_incomes(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_INCOMES, (good, price, date))
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_expenses(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_EXPENSES, (good, price, date))
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_loan(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_LOAN, (good, price, date))
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output

def select_other(good, price, date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_OTHER, (good, price, date))
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + ' ' + str(x[3]) + '\n'
        return output


###DELETE VALUE###
def delete_incomes(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_INCOMES, (good, price))
        conn.commit()
        c.close()

def delete_expenses(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_EXPENSES, (good, price))
        conn.commit()
        c.close()

def delete_loan(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_LOAN, (good, price))
        conn.commit()
        c.close()

def delete_other(good, price):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_OTHER, (good, price))
        conn.commit()
        c.close()
