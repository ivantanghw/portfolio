# Debugger on --- $env:FLASK_ENV = "development"
# insert app variable --- $env:FLASK_APP='server.py'
# server on --- flask run
from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(
            f'\nname:{name}, email:{email}, subject:{subject}, message:{message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'Did not save to database!'
    else:
        return 'Something went wrong. Try again!'

# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about-me')
def about_me():
    return render_template('about-me.html')


@app.route('/blogs')
def blog():
    return render_template('blogs.html')
