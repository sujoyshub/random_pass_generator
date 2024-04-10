from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

password_history = []

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    global password_history
    if request.method == 'POST':
        if request.form['action'] == 'regenerate':
            password = generate_password()
            password_history.append(password)
            if len(password_history) > 10:
                password_history = password_history[-10:]
            return render_template('index.html', password=password, password_history=password_history, warning_message='')
        elif request.form['action'] == 'clear':
            password_history = []
            return render_template('index.html', password='', password_history=password_history, warning_message='')
    else:
        password = generate_password()
        password_history.append(password)
        return render_template('index.html', password=password, password_history=password_history, warning_message='')

@app.route('/download')
def download_password():
    if password_history:
        password_to_download = password_history[-1]
        return f"<a href='data:text/plain;charset=utf-8,{password_to_download}' download='password.txt'>Click here to download the last generated password</a>"
    else:
        return "No password generated yet."

if __name__ == '__main__':
    app.run(debug=True)

