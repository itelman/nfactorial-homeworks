def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    
    path = environ.get('PATH_INFO', '')
    
    if path == '/ping':
        return [b'pong']
    else:
        status = '404 Not Found'
        return [b'Not Found']
