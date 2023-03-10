import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching: {response.status_code}), check the API and try again!")
    return response


def read_res(response):
    print(response.text)


def check_pwned_api(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_chars, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_chars)
    print(first5_chars, tail)
    print(response)
    return read_res(response)


check_pwned_api('123')
