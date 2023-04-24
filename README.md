# Install

## Install pipenv

If you're using Debian Buster+:

sudo apt install pipenv

Or, if you're using Fedora:

sudo dnf install pipenv

Or, if you're using FreeBSD:

pkg install py39-pipenv

Or, if you're using Gentoo:

sudo emerge pipenv

Or, if you're using Void Linux:

sudo xbps-install -S python3-pipenv

Or, if you're using Windows:

pip install --user pipenv

When none of the above is an option, it is recommended to use Pipx:

pipx install pipenv

## Install deps

`pipenv install`

# Running in dev mode

`pipenv run dev`

# Running in prod mode

`pipenv run prod`