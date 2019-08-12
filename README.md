# Wake of Vaivora

## Overview

**Wake of Vaivora** is a supplementary app to use with [**Wings of Vaivora**](https://github.com/dark-nova/wings-of-vaivora). It does **not** do anything on its own or when Wings of Vaivora runs on a separate system (without tweaks). This app can be thought as a low-tech frontend for managing uptime on Wings of Vaivora.

## Usage

Copy [`secrets.py.example`](secrets.py.example) into `secrets.py` and change all the fields according to your build. I have left some defaults that may be preferred.

If everything is set up correctly, navigate to your page defined by `secrets.py` (`URL`) and click the button. Results below:

- ![OK](OK.png): **success**; Wings of Vaivora should have restarted
- ![Fail 1](tired.png): **fail**; Wings of Vaivora is already running
- ![Fail 2](angery.png): **fail**; Wings of Vaivora was not running but could not restart

Ideally, you should also have sudo password-less permissions, preferably via sudoers and the specific command(s).

## Requirements

This code is designed around the following:

- Python 3.6+
- Linux
- `sudo`
- `systemd` unit files for both **Wake** and **Wings of Vaivora** and `systemctl` (`*`)
- `flask`
- `uWSGI`
- other [requirements](requirements.txt)
- (preferable) `nginx` to ultimately serve the page

`*` - I realize that `systemd` can be controversial so should the need arise, I will look into compatibility with `rc.d` and other init-like management tools.

## Disclaimer

This project is not affiliated or endorsed by Tree of Savior or Discord. See [`LICENSE`](LICENSE) for more detail.
