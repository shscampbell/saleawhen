from flask import Flask

# instantiate an application of the Flask class.
app = Flask(__name__)

# The Flask class has a method called route that takes a string (representing a path) and returns a decorator that defines a routine (called serve) that causes my function askawhen_index() to be called when serve("/") is called.
@app.route("/")
def askawhen_index():
    return "Sale A-When?"


# run "python server.py" and point the browser to "http://localhost:8080".
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
