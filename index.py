# encoding: utf-8
from secrets import secret as secret

def main():
    text = ["Command received"]
    return text

def application(environ, start_response):
    status = '200 OK'

    #output = 'Hello world'
    output = main()

    response_headers = [('Content-type', 'text/html; charset=utf-8'),
                        ('Content-Length', str(len('\n'.join(output))))]

    start_response(status, response_headers)

    return output

