from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')

@app.route('/home')
def home():
    name = request.args.get("name", "World")
    return render_template


@app.route('/about')
def about():
    name = request.args.get("name", "World")
    return f'<h1>About, {escape(name)}!</h1>'





if __name__ == '__main__':
	app.run(debug=True)