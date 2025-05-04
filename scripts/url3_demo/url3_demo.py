import urllib3
http = urllib3.PoolManager()

def get(method: str, url: str) -> urllib3.BaseHTTPResponse:
    """ Makes an HTTP rerquest and returns response

    Args:
        method (str): Method, for example "GET"
        url (str): url
    Returns:
        BaseHTTPResponse: Response object
    """
    return http.request(method, url)

def get_status(_resp: urllib3.BaseHTTPResponse) -> int:
    """ Get status code from a response object

    Args:
        _resp (BaseHTTPResponse): Response object

    Returns:
        int: HTTP status code
    """
    return _resp.status

def get_data(_resp:urllib3.BaseHTTPResponse) -> bytes:
    """ Get data part in bytes from a Response object

    Args:
        _resp (BaseHTTPResponse): Response object

    Returns:
        bytes: Data part of the response in bytes
    """
    return _resp.data

resp = get('GET', 'https://httpbin.org/robots.txt')
print (f'Status: {get_status(resp)}')
print (f'Data  : {get_data(resp)}')
