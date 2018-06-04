import flask
import sys, os
import Truth_table_gen as fl
app = flask.Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def enter(name=None):
    return flask.render_template('index.html', name=name)
@app.route('/handle/<string:exp>', methods=['GET'])
def handle(exp):
    try:
        out = fl.tabToStr(fl.primToTab(exp[1:]))
    except Exception as e:
        out = str(e)
    return out

app.run(host= "localhost", port=5000, debug=True)