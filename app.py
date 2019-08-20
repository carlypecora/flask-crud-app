import os

from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "appdatabase.db"))

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Book(db.Model):
	title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

	def __repr__(self):
		return "<Title: {}>".format(self.title)

@app.route("/")
def origin():
	return "My flask app"

@app.route("/home", methods=["GET", "POST"])
def home():
	if request.form:
		book = Book(title=request.form.get("title"))
		db.session.add(book)
		db.session.commit()
	return render_template('home.html')

if __name__ == "__main__":
	app.run(debug=True)