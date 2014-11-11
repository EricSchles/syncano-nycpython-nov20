from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello nycpython people!  You are all awesome!"

if __name__=='__main__':
    app.run(debug=True) #find errrors + reloads pages when there are changes

