import flask
from flask import Flask
app = Flask(__name__)

### Routing Example
@app.route('/') # decorator so output would be rendered on http://127.0.0.1:5000/; bind function to URL
                # without decorator: app.add_url_rule(‘/’, ‘hello’, hello_world)
def hello_world():
    return 'Hello World'

@app.route('/python/') # trailing '/' indicates a canonical URL; without trailing '/', then /python would result in 404 Not Found page
def hello_python():
   return 'Hello Python'

### Variable Rules
@app.route('/hello/<name>') # if http://127.0.0.1:5000/hello/TutorialsPoint is entered, then 'TutorialsPoint' will be provided as argument for function
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/blog/<int:postID>') # example using int variable
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>') # example using float variable
def revision(revNo):
   return 'Revision Number %f' % revNo

### URL Building
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return flask.redirect(flask.url_for('hello_admin'))
   else:
      return flask.redirect(flask.url_for('hello_guest', guest = name))

if __name__ == '__main__':
    app.debug = True # could do a single line: app.run(debug = True)
    app.run()
