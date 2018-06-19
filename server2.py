from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

# @app.route('/users', methods=['POST'])
# def create_user():
#    print "Got Post Info"
#    name = request.form['name']
#    email = request.form['email']
#    return redirect('/')

@app.route('/show')
def show_user():
	return reder_tempate('user.html', name='Jay', email='aberth79@gmail.com')
app.run(debug=True) 