import requests


def main():
    make_post()


def make_post():
    data = {
        'username': "geo",
        'data': "nothing important",
        'number': 50,
    }

    ans = requests.post(url="http://localhost:5000/add", data=data)
    print(ans)


if __name__ == "__main__":
    main()
