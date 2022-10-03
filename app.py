from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods = ["POST"])
def test():
    name  = request.form["name"]
    age = request.form["age"]
    email = request.form["email"]
    phone_number = request.form["phone_number"]
    symptoms = request.form["symptoms"]  
    print(name, age, email, phone_number, symptoms)
    return render_template("results.html")

if(__name__ == "__main__"):
    app.run(debug=True)