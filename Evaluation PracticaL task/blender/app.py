from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    pyramid_height = 2.5
    return render_template('index.html', pyramid_height=pyramid_height)

if __name__ == '__main__':
    app.run(debug=True)
