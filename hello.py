from flask import Flask, render_template, redirect,request
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', today = date.today(), user_name = 'aditya')

@app.route('/<page_name>')
def about(page_name):
    print(page_name)
    return render_template(f'{page_name}')

@app.route('/you/<string:user_name>')
def youtube(user_name):
    return redirect(f'https://www.youtube.com/c/{user_name}')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    data = request.form.to_dict()
    print(data)
    with open('database.txt','a') as file:
        name=data["name"]
        email=data["email"]
        message=data["message"]
        file.write(f"\n{name},{email},{message}")
    return render_template('thankyou.html', name = name)
    