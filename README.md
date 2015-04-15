# Python Telex

This library is a port of [minitel](https://github.com/heroku/minitel) for Python. The `Client` interface is identical:

``` python
from telex.client import Client

client = Client('https://user:pass@telex.heroku.com')

client.notify_app(app_uuid='...', title='Your database is on fire!', body='Sorry.')
client.notify_user(user_uuid='...', title='Here is your invoice', body='You owe us 65k.')
client.add_followup(message_uuid='...', body='here are even more details')
```

# Running Tests

``` bash
cd ./tests
pip install -r requirements.txt
PYTHONPATH=..:$PYTHONPATH ./test_telex.py
```
