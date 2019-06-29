from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <html>

    <head>
        <title>User Signup</title>

        <style>
            form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 20 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
            	}}
            body{{
                    margin: 150px;
                    background-image: url("https://images.alphacoders.com/261/thumb-1920-261841.jpg");
                    background-repeat: no-repeat;
                    background-size: 100% 150%;
                }}
            h1{{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    border-radius: 20px;
                    text-align: center;
                }}
        </style>
    </head>
    <body>

        <h1>Sign Up</h1>
        <form action ="/" method = "post">
            <label for = "username">
                Username:
            </label>
            <input type = "text" name="username" placeholder = "username" value = {0}>{1}</input>
            <br>
            <label for = "password">
                Password:
            </label>
            <input div = "hi" type = "password" name="password" placeholder = "password" >{2}</input>
            <br>
            <label for = "retype_password">
                Confirm Password:
            </label>
            <input type = "password" name="retype_password" placeholder = "Re-type password">{3}</input>
            <br>
            <label for = "Email">
                Email Address (optional):
            </label>
            <input type = "text" name="email" placeholder = "ex: username@email.com" value ={4}>{5}</input>
            <br>	
            <input type = "submit" value = "Submit">
	</form>
        
    </body>

    </html>
"""

@app.route("/", methods = ['POST'])
def func():
    username1 = True
    email1 = True
    symbol = 0
    symbol2 = 0
    space = 0
    username = request.form.get('username')
    password = request.form.get('password')
    verified_pass =request.form.get('retype_password')
    email = request.form.get('email')
    if not 3 <= len(username) <= 20 or " " in username:
        username1 = False
    if not 3 <= len(password) <= 20 or " " in password:
        password = False
    if password != verified_pass:
        verified_pass = False
    for i in email:
        if i == "@":
            symbol+=1
        if i == ".":
            symbol2+=1
        if i == " ":
            space+=1
    if email != "":
        if symbol == 1 and symbol2 == 1 and space == 0:
            if 3 <= len(email) <= 20:
                email1 = True
        email1 = False
    if username1 == False or password == False or verified_pass == False or email1 == False:
        if username1 == False:
            username1 = " Invalid username"
            username = ""
        else:
            username1 = ""
        if password == False:
            password = " Invalid password"
        else:
            password = ""
        if password != verified_pass:
            verified_pass = " Password does not match."
        else:
            verified_pass = ""
        if email1 == False:
            email1 = " Invalid email"
            email = ""
        else:
            email1 = ""
        return form.format(username,username1,password,verified_pass,email,email1)
    return f"<h1>Welcome, {username}!<h1>"
    
@app.route("/")
def index():
    return form.format("","","","","","")
app.run()
