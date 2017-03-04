from flask import Flask, render_template
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)
app.debug=True

@app.route('/user/<name>')
def user(name):
	return render_template('index.html', name=name)


@app.route('/wine')
def wine():
	return render_template('wine.html')
@app.route('/juice')
def juice():
	return render_template('juices.html')

@app.route('/demo')
def demo():
	return render_template('jdemo.html')

if __name__ == '__main__':
	manager.run()
