from fastai.vision import *
from io import BytesIO
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/classify')
def query_example():
    learn = load_learner('.')
    url = request.args.get('url') #if key doesn't exist, returns None
    response = requests.get(url)
    img = open_image(BytesIO(response.content))
    _, _, losses = learn.predict(img)
    result = sorted(zip(learn.data.classes, map(float, losses)),key=lambda p: p[1],reverse=True)
    return str(result)


@app.route('/')
def my_form():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    learn = load_learner('.')
    url = request.form['text']
    response = requests.get(url)
    img = open_image(BytesIO(response.content))
    _, _, losses = learn.predict(img)
    result = sorted(zip(learn.data.classes, map(float, losses)), key=lambda p: p[1], reverse=True)
    return str(result)

if __name__ == '__main__':
    app.run() #rundebug mode on port 5000
