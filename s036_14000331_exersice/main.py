import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


def index_view_get():
    result = requests.get('http://ma-web.ir/maktab52/users.json')
    users = result.json()
    content = {
        'users': users,
        'user': None
    }
    res = render_template('index.html', content=content)
    return res


def index_view_post(user_id):
    result = requests.get('http://ma-web.ir/maktab52/users.json')
    users = result.json()
    user = list((u for u in users if u['id'] == user_id))[0]
    content = {
        'users': users,
        'user': user
    }
    res = render_template('index.html', content=content)
    return res


app.add_url_rule('/users/', 'index', index_view_get, methods=['GET'])
app.add_url_rule('/users/<user_id>/', 'info', index_view_post, methods=['GET', 'POST'])
app.run()
