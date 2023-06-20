from time import sleep
from datetime import datetime


def main():
    while True:
        current_time = datetime.now()
        print(current_time)
        sleep(300)


if __name__ == "__main__":
    main()
