from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/',methods=['get', 'post'])
@app.route('/home',methods=['get', 'post'])
def index():
	return render_template('main.html')


@app.route('/love',methods=['get', 'post'])
def love():
	return render_template('page-11.html')


@app.route('/needs',methods=['get', 'post'])
def needs():
	return render_template('page2.html')

if __name__ == "__main__":
    app.run(debug = True)