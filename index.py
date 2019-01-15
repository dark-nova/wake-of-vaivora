# encoding: utf-8

def main():
    text = []
    text.append('<!DOCTYPE html>')
    text.append('<html>')
    text.append('<title></title>')
    text.append('<head>')
    text.append('<meta charset=UTF-8>')
    text.append('<style>')
    text.append('body {font-family:sans-serif;font-size:15px;color:#222222}')
    text.append('.mono {font-family:monospace}')
    text.append('.caps {font-variant:small-caps}')
    text.append('table {border-collapase:collapse}')
    text.append('</style>')
    text.append('</head>')
    text.append('<body>')

    text.append('</body>')
    text.append('</html>')
    return [line.encode('utf8') for line in text]


def application(environ, start_response):
    status = '200 OK'

    #output = 'Hello world'
    output = main()

    response_headers = [('Content-type', 'text/html; charset=utf-8'),
                        ('Content-Length', str(len('\n'.join(output))))]

    start_response(status, response_headers)

    return output

