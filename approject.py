from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from database import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


@app.route('/way_to_love')
def home():
	return render_template("way_to_love.html")

@app.route('/about_us')
def about():
	return render_template("about_us.html")

@app.route('/my_story', methods=['GET', 'POST'])
def story():
	if request.method == 'GET':
		return render_template('my_story.html')
	else:
		name = request.form['name']
		time = request.form['time']
		title = request.form['title']
		story = request.form['story']


		add_story(name, time, title, story)      
		return redirect('access_stories')

@app.route('/delete_stories')
def delete():
	delete_all()
	return render_template("stories.html")

@app.route('/access_stories')
def access():
	if request.method == 'POST':
		comments = request.form['comments']
		name = request.form['name']

		add_comment(name, comments)   
		return render_template("stories.html", stories=query_all())
	else:
		return render_template("stories.html", stories=query_all())
		

@app.route('/researches')
def researches():
	return render_template("researches.html")

# @app.route('/home')
# def home():
# 	return render_template("home.html")

if __name__ == '__main__':
	app.run(debug=True, threaded=True)