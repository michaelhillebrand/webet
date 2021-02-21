# webet

API for betting/voting on various events

## Getting Started

1. `python -m venv venv`
2. `./venv/bin/activate`
3. `pip install -r webet/requirements.txt`
4. `python webet/manage.py migrate`
5. `python webet/manage.py createsuperuser`
6. `python webet/manage.py runserver`

## Updating

1. Pull latest code from master branch
2. `python webet/manage.py migrate` to check for any DB updates
