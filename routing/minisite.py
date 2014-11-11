from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "This is the index page - I'm sorry it's not very interesting"

@app.route("/hello")
def hello():
    return "Hello nycpython!"

"""
To add variable parts to a URL you can mark these special sections as <variable_name>.
Such a part is then passed as a keyword argument to your function.  Optionally a converter can be used
by specifying a rule with <converter:variable_name>.  Here are some examples:"""

@app.route("/user/<username>")
def show_user_profile(username):
    #show the user profile for that user
    return 'User %s' % username

@app.route("/post/<int:post_id>")
def show_post(post_id):
    #show the post with the given id, the id is an integer
    return "Post %d" % post_id


@app.route('/testing',defaults={'path':''})
@app.route("/testing/<path:path>")
def testing(path):
    base_url = url_for('show_post',_external=True).split('/show_post')[0]
    r = requests.get(base_url+path)
    return r.ok


"""
Flask's URL rules are based on Werkzeug's routing module.  The idea behind that module is to ensure beautiful and unique URLs
based on precedents laid down by Apache and earlier HTTP servers."""

#Example:

@app.route("/projects")
def projects():
    return "this is my project page"

@app.route("/about")
def about():
    return "The about page"

"""Though they look similar, they differ in their use of the trailing slash in the URL definition.
In the first case, the canonical URL for the projects endpoint has a trailing slash.  In that sense,
it is similar to a folder on a file system.  Accessing it without a trailing slash will cause Flask to
redirect to the canonical URL with the trailing slash.

In the secone case, however, the URL is defined without a trailing slash, rather like the pathname of a file.
Accessing the URL with the trailing slash will produce a 404 NOT FOUND error.

This behavior allows relative URLs to continue working even if the trailing slash is ommited, consistent with how
Apache and other servers work.  Also, the URLs will stay unique, which helps search engines avoid indexing the same
page twice."""

if __name__ == '__main__':
    app.run(debug=True) #remember to turn this off in production

#the following converters exist: int, float, path
