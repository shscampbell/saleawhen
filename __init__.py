from flask import Flask

# instantiate an application of the Flask class.
app = Flask(__name__)

from saleawhen import views
