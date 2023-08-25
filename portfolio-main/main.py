from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)

@app.route('/submit', methods=['POST'])
def feedback_form():
    text = request.form['text']
    email = request.form['email']

    with open('feedback.txt', 'a') as f:
        f.write(email + " " + text + "\n")

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)