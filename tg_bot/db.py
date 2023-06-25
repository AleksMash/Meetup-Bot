"""
Работа с БД

Содержит функции для работы с БД.

Версия: 1.0
"""


import os
import psycopg2
from datetime import date


def get_connection():
    """
    Установление соединения с базой данных

    Параметры:
    Отсутствуют

    Возвращаемое значение:
    Объект соединения с базой данных
    """
    connection = psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )
    return connection


def fetch_upcoming_meetups(start_date: date):
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
        cursor = connection.cursor()
        cursor.execute(query, (start_date,))
        data = cursor.fetchall()
        print("data: ", data)
        return data
    finally:
        connection.close()
