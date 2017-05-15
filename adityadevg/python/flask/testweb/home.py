from flask import Flask, render_template
app = Flask(__name__)

#The names of the directory must be static and templates as per naming convention
@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)



if __name__ == "__main__":
    app.run(debug=True)
