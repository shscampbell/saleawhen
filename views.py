from flask import render_template, request
from saleawhen import app
from saleawhen import sale_model

# The Flask class has a method called route that takes a string (representing a
# path) and returns a decorator that defines a routine (called serve) that
# causes my function askawhen_index() to be called when serve("/") is called.
# i.e., it registers my "view function" with the route "/" so that whenever
# there is a request to the "/" route, this view function will be invoked and
# its result will be sent back to the client.


@app.route("/")
@app.route("/index")
def askawhen_index():
    return render_template("form/form.html")


@app.route("/results")
def askawhen_result():
    quantile = request.args.get('element_7')
    sale = sale_model.saletimeCalgary(quantile)
    return render_template("form/form2.html", quantile=quantile, saletime=sale)
