from application import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')
@app.route('/achievements')
def ach():
    return render_template('ach.html')
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run()