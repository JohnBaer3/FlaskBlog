from flask import Flask, escape, request, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'BADskdasdjalkdjlaksdlkask'

posts = [
	{
		'author': 'John Bob',
		'title': 'Blas adventures',
		'content': 'Moby Dick',
		'date_posted': 'Aug 1'
	},
	{
		'author': 'Eric Bob',
		'title': 'Adventures of Bla',
		'content': 'Ricky Bobby',
		'date_posted': 'Dec 31'
	}
]



@app.route('/')

@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)





if __name__ == '__main__':
	app.run(debug=True)