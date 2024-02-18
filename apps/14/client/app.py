from time import sleep

from requests import post


def incremented(number: int) -> int: 
    response = post("http://localhost:8080", json=dict(number=number))

    if response.status_code != 200:
        return number
    
    return response.json()["result"]


def main() -> None:
    number = 0

    while True:
        print(number)
        number = incremented(number)

        sleep(2)


if __name__ == "__main__":
    main()

