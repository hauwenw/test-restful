### Instructions

setup virtualenv and install requirements

demo site: http://ec2-52-193-143-218.ap-northeast-1.compute.amazonaws.com/

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

migrate db
```
cd udn_nba
./manage.py migrate
```

create initial data
```
./manage.py runscript web_crawler
```

add jobs to crontab
```
./manage.py crontab add
```

start server
```
./manage.py runserver
```