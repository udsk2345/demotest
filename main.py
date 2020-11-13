from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QTableView, QApplication
import sys

SERVER_NAME = 'LAPTOP-MVNOOJMC'
DATABASE = 'bauty_saloon_user4'


def create_connection():
    connection_string = f'DRIVER={{SQL Server}};' \
                  f'SERVER={SERVER_NAME};' \
                  f'DATABASE={DATABASE};'

    global db
    db = QSqlDatabase.addDatabase('QODBC')
    db.setDatabaseName(connection_string)

    if db.open():
        print('Successful connection')
        return True
    else:
        print('Connection error')
        return False


def display_data(query):
    print('Запрос обрабатывается...')
    qry = QSqlQuery(db)
    qry.exec(query)

    model = QSqlQueryModel()
    model.setQuery(qry)

    view = QTableView()
    view.setModel(model)
    view.setWindowTitle("Тестовый вывод из бд")
    view.resize(800, 1000)
    return view


if __name__ == "__main__":
    app = QApplication(sys.argv)

    if create_connection():
        SQL_STATEMENT = 'SELECT * FROM Manufacturer'
        dataView = display_data(SQL_STATEMENT)
        dataView.show()

    app.exit()
    sys.exit(app.exec_()) # Запускаем цикл обработки событий