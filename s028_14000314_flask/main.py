from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/index')


@app.route('/index')
def hello_hello():
    return "Hello World"


def pourya():
    return "hello pourya"


@app.route('/pow/<int:a>/', defaults={'b': 3})
@app.route('/pow/<int:a>/<int:b>/')
def pow(a, b):
    return f"{a}**{b}={a ** b}"


# @app.route('/', methods=['POST', 'GET'])
# def index():
#     print("Method", request.method)
#     print("Args", request.args)
#     print("Form", request.form)
#     print("Files", request.files)
#     print("Values", request.values)
#     print("Json", request.json)
#     print("Data", request.data)
#     return {
#         "Args": request.args
#         ,
#         "Form": request.form,
#         "Files": list(request.files.keys())
#         ,
#         "Values": request.values
#         ,
#         "Json": request.json
#         ,
#         "data": request.data
#         ,
#
#     }


app.add_url_rule("/pourya", 'pourya', pourya)
app.run(port=1010)
