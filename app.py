from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
	return "My flask app"

@app.route("/home", methods=["GET", "POST"])
def form():
	if request.form:
		print(request.form)
	return render_template('home.html')

if __name__ == "__main__":
	app.run(debug=True)