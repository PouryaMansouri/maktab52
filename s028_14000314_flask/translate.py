import translators
from flask import Flask,request
import requests
app = Flask(__name__)

# @app.route()
@app.route('/<to_lang>/<fr_lang>/')
def translator_view(to_lang, fr_lang):
    text = request.args['text']
    res = translators.google(text, from_language=fr_lang, to_language=to_lang)
    # res = translators.google(text,'en','fa')
    return f"{res}"


app.run()
