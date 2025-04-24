# All SQL related functions
from PyQt6.QtSql import QSqlDatabase, QSqlQuery

def init_db(db_name):
    database = QSqlDatabase.addDatabase("QSQLITE")
    database.setDatabaseName(db_name)
    if not database.open():
        print("Unable to open the database.")
        return False
    
    query = QSqlQuery()
    query.exec("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    """)

    return True


def get_expenses():
    query = QSqlQuery("SELECT * FROM expenses ORDER BY date DESC")
    
    expenses = []
    while query.next():
        expenses.append([query.value(i)] for i in range(query.record().count()))
    
    return expenses


def add_expense(date, category, amount, description):
    query = QSqlQuery()
    query.prepare("""
        INSERT INTO expenses (date, category, amount, description)
        VALUES (:date, :category, :amount, :description)
    """)
    query.bindValue(":date", date)
    query.bindValue(":category", category)
    query.bindValue(":amount", amount)
    query.bindValue(":description", description)

    result = query.exec()
    # Check if the query executed successfully
    if not query.exec():
        print("Failed to add expense:", query.lastError().text())
    else:
        return result


def delete_expense(expense_id):
    query = QSqlQuery()
    query.prepare("DELETE FROM expenses WHERE id = :id")
    query.bindValue(":id", expense_id)

    result = query.exec()
    # Check if the query executed successfully
    if not query.exec():
        print("Failed to delete expense:", query.lastError().text())
    else:
        return result
