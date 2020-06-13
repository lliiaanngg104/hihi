from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

from flask import render_template
@app.route('/template')
def show_template():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
