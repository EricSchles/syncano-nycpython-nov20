from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/<name>")
@app.route("/<name>/<friend>")
@app.route("/index/<name>")
@app.route("/index/<name>/<friend>")
def hello(name=None,friend=None):
    if name != None and friend!=None:
        string= "Hello there %s, how are you? I heard you are friends with %s, is that true?" % (name,friend)
    elif name !=None:
        string= "Hello there %s, how are you?" % name
    else:
        string = "Hello there, who are you again?"
    return string

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000
    )
