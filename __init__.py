import flask
import sys, os
import Truth_table_gen as tt
app = flask.Flask(__name__)
path = 'G:\\Scripts\\Truth-Tables\\'
@app.route('/', methods=['POST', 'GET'])
def enter(name=None):
    indexpath = path + 'templates\index.html'
    with open (path + 'temp.html', "r") as myfile:
        data=myfile.read()
    data = data.replace("OR",tt.orOps())
    data = data.replace("AND",tt.andOps())
    data = data.replace("NOT",tt.negOps())
    data = data.replace("CHARS",tt.allowedChars)
    print(data)
    myfile.close()
    with open(indexpath,'w') as myfile:
        myfile.write(data)
    myfile.close()
    return flask.render_template('index.html', name=name)
@app.route('/handle/<string:exp>', methods=['GET'])
def handle(exp):
    try:
        out = tt.tabToStr(tt.primToTab(exp[1:]))
    except Exception as e:
        out = str(e)
    return out

app.run(host= "localhost", port=5000, debug=True)