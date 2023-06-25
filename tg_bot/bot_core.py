from time import sleep
from datetime import datetime
import db


def main():
    i = 0
    while i < 10:
        i += 1

        current_date = datetime.now().date()
        upcoming_meetups = db.fetch_upcoming_meetups(current_date)

        for row in upcoming_meetups:
            print(row)
        sleep(10)


if __name__ == "__main__":
    main()
