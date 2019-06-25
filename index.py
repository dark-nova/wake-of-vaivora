# encoding: utf-8
import secrets
import subprocess

def main():
    html[-3] = html[-3].format('OK.png')
    try:
        ps = subprocess.Popen(secrets.check1, stdout=subprocess.PIPE)
        piped = pipes(secrets.prelim_checks, ps)
        vgrep = subprocess.check_output(secrets.check3, stdin=piped.stdout)
        ps.wait()
    except:
        vgrep = False

    if vgrep:
        html[-3] = html[-3].format('tired.png')
    else: # script is probably not running
        result = subprocess.run(secrets.secret)
        if result.returncode != 0:
            html[-3] = html[-3].format('angery.png')
    return html

def pipes(checks, out):
    for check in checks: # `checks` should be [1:-1] of the original checks
        out = subprocess.Popen(check, stdin=out.stdout, stdout=subprocess.PIPE)
    return out

def application(environ, start_response):
    status = '200 OK'

    #output = 'Hello world'
    output = main()

    response_headers = [('Content-type', 'text/html; charset=utf-8'),
                        ('Content-Length', str(len('\n'.join(output))))]

    start_response(status, response_headers)

    return '\n'.join(output)

html = []
html.append('<!DOCTYPE HTML>')
html.append('<html>')
html.append('<head>')
html.append('<style>')
html.append('img { max-width:100%; height:auto; width:auto\9; /* ie8 */ }')
html.append('</style>')
html.append('</head>')
html.append('<body>')
html.append('<img src="{}" />')
html.append('</body>')
html.append('</html>')

print('\n'.join(main()))