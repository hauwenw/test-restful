### Instructions

setup virtualenv and install requirements

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

run server
```
cd udn_nba
./manage.py migrate
./manage.py runscript web_crawler
./manage.py runserver
```