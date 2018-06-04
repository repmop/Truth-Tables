import flask
import sys, os
import Truth_table_gen
app = flask.Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def enter(name=None):
    return flask.render_template('index.html', name=name)
@app.route('/handle', methods=['POST', 'GET'])
def handle():
    text = flask.request.form['input']
    return flask.redirect('/entered')

app.run(host= '0.0.0.0', port=5000, debug=True)