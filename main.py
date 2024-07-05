from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from info import text_data

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', text_data=text_data)

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html', text_data=text_data)


@app.route('/conocimientos')
def conocimientos():
    return render_template('conocimientos.html', text_data=text_data)

@app.route('/contactame')
def contactame():
    return render_template('contactame.html', text_data=text_data)

if __name__ == "__main__": app.run()
