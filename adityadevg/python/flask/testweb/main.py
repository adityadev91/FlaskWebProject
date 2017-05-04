# Created using PyCharm - an excellent Python IDE from JetBrains

from flask import Flask, request

app = Flask(__name__)




# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route('/')
def index():
    return 'This is the homepage'




# The parameter defines the url of the result returned by the function below
@app.route('/about')
def about():
    return '<h4>Software Engineer</h4>'



# The function can also take a String parameter in the following fashion
@app.route('/profile/<username>')
def profile(username):
    return '<h4>Hi %s</h4>' % username



# The function can also take an Integer parameter in the following fashion
@app.route('/post/<int:post_id>')
def post(post_id):
    return '<h4>Display Post with Id: %s</h4>' % post_id




# How to find out which HTTP request type - GET or POST
@app.route('/requestType')
def requestType():
    return '<h4>HTTP Request Type: %s</h4>' % request.method




# Handle multiple request types, here - GET or POST
# To check out the POST request type, try using the PostMaster app from the Google Chrome Store
@app.route('/bothRequests', methods=['GET','POST'])
def bothRequests():
    if request.method == 'POST':
        return '<h4>You are using %s</h4>' % request.method
    else:
        return '<h4>You are using %s</h4>' % request.method





# This ensures that the main is the main project file
# Setting Debug True gets us all the log statements
if __name__ == "__main__":
    app.run(debug=True)





# Each function name must be different because they refer to a different end point
