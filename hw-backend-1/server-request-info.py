import json

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'application/json')]
    start_response(status, headers)
    
    method = environ.get('REQUEST_METHOD', '')
    url = environ.get('PATH_INFO', '')
    protocol = environ.get('SERVER_PROTOCOL', '')
    
    response = {
        "method": method,
        "url": url,
        "protocol": protocol
    }
    
    return [json.dumps(response).encode()]
