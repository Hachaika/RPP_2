import requests
from bs4 import BeautifulSoup
import time

pairs = {
    'fwfwafw@mail.ru': '11111',
    'fwfwa@mail.ru': '22222',
    'fwfw@mail.ru': '33333',
    'fwf@mail.ru': '44444',
    'f@mail.ru': '55555',
    'fwfwaf@mail.ru': '66666',
    'fwfwfw@mail.ru': '77777',
    'fwfwaw@mail.ru': '88888',
    'fwwafw@mail.ru': '99999',
    'fwfwrerfw@mail.ru': '10101',
    'fwffw@mail.ru': '11101',
    'ffw@mail.ru': '12121',
    'fwfweqw2afw@mail.ru': '13131',
    'fwfwgsegafw@mail.ru': '14141',
    'fwfjjwafw@mail.ru': '15151',
    'fwfwrwafw@mail.ru': '16161',
    'fwfwahrhfw@mail.ru': '17171',
    'fwfwhtyhafw@mail.ru': '18181',
    'fwfwew4fafw@mail.ru': '19191',
    'fwfwhttafw@mail.ru': '20202',
    'vip.polyav1911@bk.ru': '12345',
    'fwfwafwfw@mail.ru': '21212',
    'fwfwadfgfw@mail.ru': '22202',
    'fwfwajrtfw@mail.ru': '23232',
    'fwfwnhfafw@mail.ru': '24242',
    'fwfwafeww@mail.ru': '25252'
}

login_url = 'http://127.0.0.1:5000/login'


def get_csrf_token(session, url):
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'}).get('value')
    return csrf_token


def login_request(session, username, password, csrf_token):
    payload = {'email': username, 'password': password, 'csrf_token': csrf_token}
    response = session.post(login_url, data=payload, allow_redirects=False)
    return response


def main():
    with requests.Session() as session:
        csrf_token = get_csrf_token(session, login_url)

        for username, password in pairs.items():
            while True:
                response = login_request(session, username, password, csrf_token)

                if response.status_code == 302:
                    print(f"Successful login - Username: {username}, Password: {password}")
                    return
                elif response.status_code == 429:
                    print("Too Many Requests. Pausing for 1 minute.")
                    time.sleep(60)
                else:
                    break


if __name__ == "__main__":
    main()
