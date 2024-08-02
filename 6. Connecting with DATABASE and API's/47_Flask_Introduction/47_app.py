# Flask is a pythonic library jo aapko APIs banane mein ya fir jo bhi methods hai usko expose krne mein to the outer world taaki hum usko kahi se bhi access kar sake i.e. aap code yha python mein likh rhe hai, aapka function python mein available hai but iss same function ko i want to access not thorough python , maybe through a website , URL ke through , google ke through , ya kisi or tool ke through
# and then comes client server based architecture
from flask import Flask

# variable with dunder
# now app becomes object of class(FLASK) jo flask mein hoga vo ab app mein bhi available ho jayega
app = Flask(__name__)

# decorator
@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

# flask will make the server and using above function client will give outcomes
# 1. cleint pehle pochega server ke paas see in diag. 
# 2. flask will provide route to reach out to a particular function using "@app.route("/")"
# 3. Ab aapko(cleint) koi bhi function access karna hai to iss route ke paas jao "/" or jakar vha access karlo

if __name__=="__main__":
    app.run(host="0.0.0.0")



# Now after running you will see that this program(hello_world()) is running on server and if you want to access this program then
# 1.sabse pehle pochenge hum machine ke paas. Now the url is the rasta to reach server. URL of current website 
# 2. If you copy this url ("https://mango-librarian-euwxh.pwskills.app/") and paste on new tab as : ("https://mango-librarian-euwxh.pwskills.app:5000") it will show hello world
# 3. hellow world is the outcome of the function/program
# 4. and with the help of this url you can access this from any device 

# AND if you remeber this was our objective
# AND we are calling on heterogenous platform i.e. your browser understand : HTML/CSS/JS and your flask is in python. 2 alag alag. we are able to hit with the help of HTTP. which is REST
# Jo jo ab isko access krega aapko terminal mein dikhhta rhega. 200-> successful and 404->page not found
