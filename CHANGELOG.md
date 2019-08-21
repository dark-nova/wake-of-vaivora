# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.2.1] - 2019-08-21
### Changed
- Use generic images instead of copyright-able images

## [1.2] - 2019-08-12
### Changed
- Migrate from `secrets.py` to [`config.yaml`](config.yaml.example) for better settings management; include PyYAML for this
- Updated [`README.md`](README.md)

## [1.1] - 2019-07-05
### Added
- Retroactively add a changelog
- Integrated `index.py` into [`app.py`](app.py)
- Actual [`requirements.txt`](requirements.txt)

### Changed
- Use Flask instead of bare uWSGI

### Removed
- Removed old `index.py` 

## [1.0.1] - 2019-06-24
### Changed
- Fleshed out index page

### Removed
- Removed buggy [`requirements.txt`](requirements.txt)

## [1.0] - 2019-01-14
### Added
- Initial version
