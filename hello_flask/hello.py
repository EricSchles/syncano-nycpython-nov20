from flask import Flask
app = Flask(__name__)
#an example application completely lifted from:
#http://flask.pocoo.org/

@app.route("/")
def hello():
    return "Hello nycpython people!  You are all awesome!"

if __name__=='__main__':
    app.run(debug=True) 
    # debug=true - find errrors + reloads pages when there are changes

