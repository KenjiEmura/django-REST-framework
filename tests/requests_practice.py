import requests


def main():
    # response = requests.get('http://www.google.com')
    # print("Status Code: ", response.status_code)
    # print("Content-Type: ", response.headers['Content-Type'])
    # print("Content: ", response.text)

    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get('https://httpbin.org/get', data=payload)
    print(r.url)


if __name__ == "__main__":
    main()
