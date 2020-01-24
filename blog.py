from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	{
		'author' : 'Lovish',
		'title' : 'Blog post 1',
		'content': 'First Post content',
		'date_posted': 'Jan 24, 2019'
	},
	{
		'author' : 'Komal',
		'title' : 'Blog post 2',
		'content': 'Second Post content',
		'date_posted': 'Jan 23, 2019'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts = posts, title = "home")

@app.route("/about")
def about():
	return render_template('about.html', title = "about")

if __name__=='__main__':
	app.run(debug=True)