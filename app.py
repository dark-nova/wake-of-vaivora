import subprocess
from flask import Flask, request

import secrets


app = Flask(__name__)

# with hints from https://scotch.io/bar-talk/processing-incoming-request-data-in-flask
@app.route(secrets.URL, methods=['GET', 'POST'])
def page():
    if request.method == 'GET':
        return """
            <form method="POST">
                <button>Wake Wings of Vaivora</button>
            </form>
            """
    else:
        return wake()


def wake():
    img = 'OK.png'

    try:
        ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
        piped = subprocess.Popen(
            ['grep', '{}.*python'.format(secrets.VAIVORA_DIR)],
            stdin=ps.stdout,
            stdout=subprocess.PIPE
            )
        process = subprocess.check_output(
            ['grep', '-v', 'grep'],
            stdin=piped.stdout
            )
        ps.wait()
    except:
        process = None

    if process:
        img = 'tired.png'
    else:
        # be sure your user has sudo password-less permissions,
        # preferably via sudoers
        result = subprocess.run(
            ['sudo', 'systemctl', 'restart', secrets.VAIVORA_SERVICE]
            )
        if result.returncode != 0:
            img = 'angery.png'
    return """
        <img src="{}" style="max-width:100%; height:auto; width:auto\9; /* ie8 */" />
        """.format(img)
