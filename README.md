# webet

API for betting/voting on various events

## Getting Started

1. Create a pythong virtual environment: `python -m venv venv`
2. Source the virtual env:
  a. bash/zsh based shells: `source ./venv/bin/activate`
  b. cmd: `.\vemv\Scripts\activate.bat`
  c. PowerShell: `.\vemv\Scripts\Activate.ps1`
3. Install dependencies: `pip install -r webet/requirements.txt`
4. Install SQL Lite database schemas: `python webet/manage.py migrate`
5. Create a local super user: `python webet/manage.py createsuperuser`
6. Start the server`python webet/manage.py runserver`

## Updating

1. Pull latest code from master branch
2. `python webet/manage.py migrate` to check for any DB updates
