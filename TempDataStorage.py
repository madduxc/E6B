# Author:           Charles D. Maddux
# Date Created:     11 February 2024
# Description:      Temporary service to store E6B data locally while microservice is in development

import time, json


def main():
    while True:
        print("In development - geese")
        time.sleep(5)


if __name__ == "__main__":
    main()
