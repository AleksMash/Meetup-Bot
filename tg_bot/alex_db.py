"""
Работа с БД

Содержит функции для работы с БД.

Версия: 1.0
"""


import os
import psycopg2
from psycopg2.extras import DictCursor
from datetime import date

connection: object = None

def get_connection():
    """
    Установление соединения с базой данных

    Параметры:
    Отсутствуют

    Возвращаемое значение:
    Объект соединения с базой данных
    """
    connection = psycopg2.connect(
        host='127.0.0.1',
        port=5433,
        database='postgres',
        user='postgres',
        password='admin',
    )
    return connection


def get_upcoming_events():
    """
    Получение перечня предстоящих мероприятий

    Параметры:
    дата начала
    """
    query = """
        SELECT  
            id, title, organizer, start_date, end_date
        FROM  meetup
        WHERE start_date >= %s
        ORDER BY start_date ASC
    """
    connection = get_connection()
    try:
        cursor = connection.cursor(cursor_factory=DictCursor)
        cursor.execute(query, (date.today(),))
        data = cursor.fetchall()
        return data
    finally:
        connection.close()

def get_current_events():
    """
    возвращает текущие событие (которые активны в данный момент)
    """
    pass


def get_user_info(tg_user_id):
    """
        Получение полной информации о пользователе
    Параметры:
        tg_user_id
    Возвращает:
        все поля из таблиц person, profile
    """
    # todo:
    #  добавить поле is_organizer - чтобы понимать может ли пользователь организовывать митапы
    #  написать тело функции
    return {'is_organizer': True}


def user_is_organizer(tg_user_id):
    """
       Возвращает True если пользователь - организатор, иначе - False
    Параметры:
        tg_user_id
    """
    return True
