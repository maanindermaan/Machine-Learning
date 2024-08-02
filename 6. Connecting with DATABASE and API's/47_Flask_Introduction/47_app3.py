# In this we are making function that will take input at the time when you hit url. It will take input as a query parameter
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World!1</h1>"

@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World!2</h1>"

@app.route("/test")
def test():
    return "this is my function to run app"

@app.route("/test2")
def test2():

    a = 5+5
    return "this is my function to run app {}".format(a)

# can take any heirarchy
@app.route("/test3/test3")
def test3():
    data = request.args.get('x')
    return "this is a data input from my url {}".format(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)


# https://mango-librarian-euwxh.pwskills.app:5001/test3/test3?x=maninder -> we have to write ?x="whateveryouwant", we take x because in data request we have passed 'x'







