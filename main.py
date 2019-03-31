#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ii_module
import getpass
import db_module


class User:  # TODO Нужно ли еще доработать?
    userlist = []
    """Класс пользователей и ролей"""
    def __init__(self, name, passwd, role):
        self.name = name
        self.passwd = passwd
        self.role = role
        User.userlist.append(self)

    def is_valid_password(self, passwd):
        return True if passwd == self.passwd else False

    @staticmethod
    def registered_user(login):
        for user in User.userlist:
            if login == user.name:
                return user




def show_empty_manage_form():
    """Отображает форму для заполнения заказа менеджеру"""
    id = input("Номер заказа: ")
    input("Тип детали: [стандарт]: ")
    type = 1

    quantity = int(input("Количество: "))
    priority = int(input("Приоритет (1 - низ/2 - об/3 - выс) [2] ") or 2)
    price = int(input("Сумма: "))
    answer = {
        'id': id,
        'type': type,
        'quantity': quantity,
        'priority': priority,
        'price': price
    }
    #print(a)
    return answer


def manage_form():
    """Отображает форму заполнения заказа менеджеру"""
    while True:
        print("\nВыберите действие:")
        print("1 - Добавить заказ")
        print("2 - Удалить заказ")
        print("3 - Просмотр заказов")
        print("0 - Выход")
        choise = int(input('? : '))

        if choise == 1:
            # Формируем словарь с заказом
            offer_data = show_empty_manage_form()
            # Получаем ответ от ИИ
            ii_answer = ii_module.calculate_deadline(offer_data)
            result = """
            Номер заказа: {}
            Тип детали: стандарт-1
            Количество: {}
            Приоритет: {}
            Сумма: {}
            Срок: {}
            """.format(offer_data['id'],
                       offer_data['type'],
                       offer_data['quantity'],
                       offer_data['priority'],
                       offer_data['price'],
                       ii_answer)
            print(result)


def admin_form():
    db = db_module.DBConnection()
    while True:
        print("\nВыберите действие:")
        print("1 - Добавить пользователя")
        print("2 - Удалить пользователя")
        print("3 - Отобразить список пользователей")
        print("0 - Выход")
        choise = int(input('? : '))
        if choise == 0:
            print("Выход из формы администратора")
            break
        elif choise == 1:
            login = input("Введите имя пользователя (Логин): ")

            # Если такой пользователь уже есть то выкинуть ошибку!
            #if User.registered_user(login):
            if db.user_registered(login):
                print("Такой пользователь уже присутствует в системе!\n")
                continue

            passwd = input("Введите пароль для пользователя: ")
            passwd_2 = input("Повторите пароль: ")
            if passwd != passwd_2:
                print("Введенные пароли не совпадают!\n")
                continue
            role = input("Роль пользователя (admin/manager/engineer): ")
            if role not in ['admin', 'manager', 'engineer']:
                print("Неверная роль!\n")
                continue

            print("Создание ползователя...")
            db.add_user(login, passwd, role)
            print("Пользователь {} создан с превилегиями {}\n".format(login, role))

        elif choise == 2:
            name = input("Введите имя ползователя для удаления: ")
            if not db.user_registered(name):
                print("Данный пользователь не зарегистрирован в системе!")
            choise = input('Вы действительно хотите удалить данного пользователя? (y/n): ')
            if choise.lower() in ['yes', 'y']:
                #User.userlist.remove(user)
                db.user_remove(name)
                print("Пользователь {} был удален!".format(name))
            else:
                print("Отмена.")

        elif choise == 3:
            template = "{0:<20} {1:<7}"
            print(template.format("\nИмя пользователя", "Роль"))
            for user in db.get_all():
                print(template.format(*user))


def db_call_machine_state():
    """Запрос к БД о списке станков"""
    return dict()


def show_engineer_table(filer_by='break_chance'):  # TODO реализовать
    """Отображает сводную таблицу инженера"""
    # получаем ответ от ДБ по списку станков
    machine_data = db_call_machine_state()

    # вычлиняем список айдишников станков
    machines_list = [id for id in machine_data['id']]  # TODO проверить

    # получаем ответ от ии по станкам id_станка:шанс_поломки
    ii_answer = ii_module.calculate_breakout(machines_list)  # TODO реализовать

    # примиксовываем шанс поломки в структуру ответа
    answer = []  # TODO реализовать

    return answer


def show_login_page():
    """Отображает форму авторизации"""
    print("Пожалуйста, авторизуйтесь.")
    login = input('Логин: ')
    password = input('Пароль: ')
    user = User.registered_user(login)
    if not user:
        print("Пользователь {} не зарегистрирован".format(login))
        show_login_page()
    if not user.is_valid_password(password):
        print("Неверный пароль!")
        show_login_page()
    if user.role == "admin":
        admin_form()
    elif user.role == 'manager':
        show_empty_manage_form()


# Инициализируем пользователей
User('admin', 'admin', 'admin')
User('man', 'man', 'manager')
User('en', 'en', 'engineer')

if __name__ == '__main__':
    while True:
        #show_login_page() Failed!
        show_login_page()
        #admin_form() passed!
