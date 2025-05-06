import urllib3
from url3demo import get, get_status, get_data

def test_get_status():
    resp = get('GET', 'https://httpbin.org/robots.txt')
    status = get_status(resp)
    assert status == 200

def test_get_data():
    resp = get('GET', 'https://httpbin.org/robots.txt')
    expected = b'User-agent: *\nDisallow: /deny\n'
    actual = get_data(resp)
    assert actual == expected

