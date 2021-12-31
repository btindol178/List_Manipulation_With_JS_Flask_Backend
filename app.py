import json
from flask import Flask, render_template
#https://stackoverflow.com/questions/15321431/how-to-pass-a-list-from-python-by-jinja2-to-javascript?fbclid=IwAR31QE1dkRJl9vT8MeKyB0pIJ0cNbPxuWo8J5Gw7GfVPNVeZzSfZlgG3wZU

app = Flask(__name__)

@app.route('/')
def my_view():
    data = [1, 'foo']
    return render_template('index.html', data=json.dumps(data))

if __name__ == "__main__":
    app.run(debug=True)