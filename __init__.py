import flask
import sys, os
#sys.stderr.write("PATH PATH PATH: ")
#for s in sys.path:
#    sys.stderr.write(s)
#sys.path.append("/var/www/faithinnothing.me/truthtables/truthtables")
from truthtables import  tt


app = flask.Flask(__name__)
path = '/var/www/html/faithinnothing.me/truthtables/truthtables/'
@app.route('/', methods=['POST', 'GET'])
def enter(name=None):
    indexpath = path + 'templates/index.html'
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
if __name__=='__main__':
    app.run(host= "127.0.1.1", port=5003, debug=True)
