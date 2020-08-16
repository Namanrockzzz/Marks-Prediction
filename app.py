
# Importing Required 
from flask import Flask, render_template, redirect, request
import joblib

# __name__ = "__main"
app = Flask(__name__)

# Loading model
model = joblib.load("model.pkl")

# Home route (Get request)
@app.route('/')
def hello():
	# Flask already knows that all the HTML files reside in templates folder
	return render_template("index.html")

# Home route (Post request)
@app.route('/', methods = ['POST'])
def marks():
	if request.method == 'POST':
		# Taking input
		hours = float(request.form['hours'])
		# Predicting marks
		marks = model.predict([[hours]])[0][0]

	return render_template("index.html", your_marks = marks)

if __name__=="__main__":
	# app.debug = True
	app.run(debug = True)