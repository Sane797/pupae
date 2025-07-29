from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Store or process the data
    print(f"New message from {name} ({email}): {message}")

    return "Message received! Thank you."

if __name__ == '__main__':
    app.run(debug=True)
