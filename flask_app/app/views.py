from app import app
from flask import render_template,redirect, request, flash,g,session,url_for
import models

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET","POST"])
def signup():
    return render_template("signup.html")

@app.route("/signedup", methods=["GET","POST"])
def signedup():

    if request.form.get('email') == None:
        flash("Please provide an email")
    else:
        email = request.form['email']
    
    if request.form.get('username') == None:
        flash("Please think of a username")
    else:
        username = request.form['username']
    
    if request.form.get('password') == None:
        flash("Please come up with a password")
    else:
        password = request.form['password']
    
    phone = request.form.get('phone')
    
    picture = request.form.get('picture')

    if not session.get("logged_in"):
        models.db.create_all()
        new_user = models.AccountHolder(username,password,email,phone)
            
        models.db.session.add(new_user)
        models.db.session.commit()
    
    return render_template("homepage.html",username=username) 

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/directory/<username>")
def directory(username):
    contacts = models.Contact.query.all()
    return render_template("directory.html",username=username,contacts=contacts)

@app.route("/info/<username>/<person>")
def info(username,person):
    return render_template("info.html",username=username,person=person)

@app.route("/home/<username>")
def homepage(username):
    return render_template("homepage.html",username=username)

@app.route("/add_contact/<username>")
def add_contact(username):    
    return render_template("add_contact.html",username=username)

@app.route("/adding/<username>", methods=["GET","POST"])
def adding(username):
        
    if request.form.get('name') == None:
        flash("Please give us a name, at least")
    else:
        name = request.form['name']
        
    phone = request.form.get('phone')
    email = request.form.get('email')
    picture = request.form.get('picture')
    return redirect("/home",username=username) # add a route to the signed in homepage
