from flask import Flask , render_template , request , jsonify

app = Flask(__name__)

@app.route('/' , methods = ['GET' , 'POST'])
# this will render the html index page
def home_page():
    return render_template('index.html')

# 1. ye data extract krega https://lemon-analyst-husmt.pwskills.app:5000/ yha se or jo operation hoga usko perform krega lets say we input 1 and 2 and add
# 2. so now server will do the calculations and then it will send the result to display there on url 
# 3. uper wale code se hum render karwapayenge but data dalne ka code nahi likha hai vo abhi likhenge


# becuase humne yehi route define kiya tha jab html banaya tha
@app.route('/math' , methods = ['POST'])
# Now making method to do calculations
def math_ops():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtraction of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiplication of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The division of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
            
        return render_template('results.html' , result = result)


# isme hum form se data utha rhe hai because class == 'form ' kal hum url se data utha rhe the
# 1. form se hume uthana hai ki operation ka type kya hai addn , subtr , .. 
# 2. num1 -> number 1 input
# 3. num2 -> number 2 input
# 4. ab jo bhi cleint input dalega vo in varibales ops , num1 , num2 mein store ho jayega
# 5. WHILE RUNNING WE CAN ALSO USE MONGODB TO STORE THE RESULT INTO DB



# Now lets say you want to pass data with some other tool (WITHOUT FORMS) by using a post method
# we are using the tool postman
# change form with json


@app.route('/postman_data' , methods = ['POST'])
def math_ops1():
    if(request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if ops == 'add':
            r = num1+num2
            result = "The sum of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1-num2
            result = "The subtraction of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1*num2
            result = "The multiplication of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1/num2
            result = "The division of " + str(num1) + ' and ' + str(num2) + " is " + str(r)
            
        return jsonify(result)
        # jo bhi result yha par aarha hai usko as a json object hum return karwaden and that is why we will pass the data in json format
        # you have to download this tool postman as well 






if __name__=="__main__":
    app.run(host="0.0.0.0" , port = 5001)




# NOW TALKING ABOUT GET AND POST
# 1. we have seen that while writing something on google it passes the query in URL(accessible to all), we have deployed it as well.
# 2. but in case of gmail when you write password and mail id, it doesnot appear in the URL. It is passed data as a BODY. Ye as a BODY bhejta hai system aapke server ke paas
# 3. When you passes data through URL it is called GET(through URL).(sending a data)
# 4. When you passes data through BODY it is called POST(through BODY).(sending a data)
# 5. both means sending a data in different types (url and body)
# 6. Dono jagah hum data hi behjte hai
