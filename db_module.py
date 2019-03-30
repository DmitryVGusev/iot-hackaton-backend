#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3


class DBConnection:
    DB_FILE = 'hack.sqlite'

    def __init__(self):
        self.connection = sqlite3.connect(DBConnection.DB_FILE)
        self.cursor = self.connection.cursor()

    def add_user(self, login, password, role):
        query = ['INSERT INTO User (Name, Password, Role) VALUES (?, ?, ?);', (login, password, role)]
        self.cursor.execute(*query)
        self.connection.commit()

    def db_drop(self):  # TODO реализовать
        """Дропает базу и создает таблицу с пользователями"""
        # Зануляем файл БД
        open(DBConnection.DB_FILE, 'w').close()
        # Создаем таблицу с ползователями
        self.cursor.execute("CREATE TABLE User("
                            "id INTEGER PRIMARY KEY ASC, "
                            "Name TEXT, "
                            "Password TEXT,"
                            "Role TEXT);")

        # Добавляем записи в таблицу с пользователями
        self.add_user('admin', 'admin', 'admin')
        self.add_user('man', 'man', 'manager')
        self.add_user('eng', 'eng', 'engineer')

    def user_registered(self, username):
        """Возвращает id пользователя (Если такой есть)"""
        ans = self.cursor.execute("SELECT id FROM User WHERE Name =?", (username,)).fetchone()
        if ans:
            return ans[0]

    def get_all(self):
        return self.cursor.execute("SELECT * FROM User").fetchall()

    def db_check_user_passwd(self, username, password):
        """Проверяет пароль пользователя"""
        query = ["SELECT id FROM User WHERE Name =? AND Password =?", (username, password)]
        ans = self.cursor.execute(*query).fetchone()
        return True if ans else False


    def db_close(self):
        self.cursor.close()


if __name__ == '__main__':
    conn = DBConnection()
    conn.db_drop()
    print(conn.db_check_user_passwd('admin', 'admin'))
    print(conn.db_check_user_passwd('man', 'mana'))

    conn.db_close()
