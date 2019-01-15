# encoding: utf-8
import secrets
import subprocess

def main():
    text = ["Command received"]
    subprocess.run('whoami')
    return text

def application(environ, start_response):
    status = '200 OK'

    #output = 'Hello world'
    output = main()

    response_headers = [('Content-type', 'text/html; charset=utf-8'),
                        ('Content-Length', str(len('\n'.join(output))))]

    start_response(status, response_headers)

    return output

