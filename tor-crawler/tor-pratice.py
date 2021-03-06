import requests
from stem import Signal
from stem.control import Controller

# signal TOR for a new connection 
def renew_connection(_password):
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password=_password)
        controller.signal(Signal.NEWNYM)

def get_tor_session():
    '''
    get tor session with request
    '''
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

def main():
    password = "16:872860B76453A77D60CA2BB8C1A7042072093276A3D701AD684053EC4C"
    renew_connection(password)
    session = get_tor_session()
    print(session.get("http://httpbin.org/ip").text)
    print(requests.get("http://httpbin.org/ip").text)
    pass

if __name__ == '__main__':
    main()