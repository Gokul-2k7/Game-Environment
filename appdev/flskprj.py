import os
from flask import Flask,request,render_template,redirect,url_for
app=Flask(__name__)
login={}
@app.route('/',methods=["GET","POST"])
def home():
    error=None
    if request.method=="POST":
        name=request.form.get("name")
        Password=request.form.get("Pass")
        if name in login and login[name]==Password:
            return f"HI {name}"
        else:
           error="Invalid username or password"        
    return render_template('index.html',error=error)
@app.route('/register',methods=["GET","POST"])
def register():
    Name=None
    if request.method=="POST":
        Name=request.form.get("Name")
        Pass=request.form.get("Pass")
        if Name in login:
            error="Username exists"
            return render_template('register.html',login=login,Name=Name,error=error)
        login[Name]=Pass
        return redirect(url_for('home'))
    return render_template('register.html',login=login,Name=Name)

@app.route('/name=<name>/age=<age>')
def details(name,age):
    return f"{name} age is {age}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
