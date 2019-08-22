import subprocess

import yaml
from flask import Flask, request


app = Flask(__name__)

with open('config.yaml', 'r') as f:
    conf = yaml.load(f, Loader=yaml.Loader)

try:
    with open('images.yaml', 'r') as f:
        images = yaml.load(f, Loader=yaml.Loader)
except FileNotFoundError:
    # Fallback on default
    with open('images.yaml.example', 'r') as f:
        images = yaml.load(f, Loader=yaml.Loader)

# with hints from https://scotch.io/bar-talk/processing-incoming-request-data-in-flask
@app.route(conf['uri'], methods=['GET', 'POST'])
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
    img = images['success']

    try:
        ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
        piped = subprocess.Popen(
            ['grep', '{}.*python'.format(conf['directory'])],
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
        img = images['failure_already_running']
    else:
        # be sure your user has sudo password-less permissions,
        # preferably via sudoers
        result = subprocess.run(
            ['sudo', 'systemctl', 'restart', conf['service']]
            )
        if result.returncode != 0:
            img = images['failure_could_not_restart']
    return """
        <img src="{}" style="max-width:100%; height:auto; width:auto\9; /* ie8 */" />
        """.format(img)
