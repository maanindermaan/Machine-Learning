# Flask is a pythonic library jo aapko APIs banane mein ya fir jo bhi methods hai usko expose krne mein to the outer world taaki hum usko kahi se bhi access kar sake i.e. aap code yha python mein likh rhe hai, aapka function python mein available hai but iss same function ko i want to access not thorough python , maybe through a website , URL ke through , google ke through , ya kisi or tool ke through
# and then comes client server based architecture
from flask import Flask

app = Flask(__name__)

# now "/" is home route and i want to access hellow world 1 and 2 as well becuase ek route mein hum ek hi function dalenge

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

# to overcome that we write anything beside "/"
# we are just route bidning. pehle system tak pocho or fir / karke hello_world1 daldo 
@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello, World!1</h1>"

@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello, World!2</h1>"



# 1. Now to access same you've to just do minor changes
# 2. copy the url and make changes till "https://mango-librarian-euwxh.pwskills.app:5000/" and now to access specific functions you can just
# 3. https://mango-librarian-euwxh.pwskills.app:5000/hello_world1


# Making your function to execute 
@app.route("/test")
def test():
    return "this is my function to run app"
# https://mango-librarian-euwxh.pwskills.app:5000/test


# Method to return 2 statements
@app.route("/test2")
def test2():
    a = 5+5
    return "this is my function to run app {}".format(a)



if __name__=="__main__":
    app.run(host="0.0.0.0")



# THis is known as app routing 





