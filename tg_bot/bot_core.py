from time import sleep
import os
import psycopg2


def main():
    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )

    cursor = conn.cursor()

    query = "SELECT * FROM person"

    i = 0
    while i < 10:
        i += 1
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
        sleep(10)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
