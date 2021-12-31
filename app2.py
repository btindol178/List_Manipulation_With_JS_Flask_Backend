import json
from flask import Flask, render_template
#https://stackoverflow.com/questions/15321431/how-to-pass-a-list-from-python-by-jinja2-to-javascript?fbclid=IwAR31QE1dkRJl9vT8MeKyB0pIJ0cNbPxuWo8J5Gw7GfVPNVeZzSfZlgG3wZU
#https://stackoverflow.com/questions/46141450/create-li-from-loop-through-array-and-display-to-html-as-a-list
app = Flask(__name__)

@app.route('/')
def chart_sandbox():

    list1 = ['what','is','this','all','about','can','i','make','a','million','dollars']

    return render_template("index2.html", list1=json.dumps(list1))

if __name__ == "__main__":
    app.run(debug=True)