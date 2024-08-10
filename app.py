from flask import Flask, render_template 
app = Flask(__name__)

Data = [
    {
        "I", "G", "S"
    }
]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/blog')
def blog():
    day = ["I,", "G", "S"]


    return render_template("blog.html", data = data , DataI = DataI)

if __name__ == "__main__":
    app.run(debug=True)