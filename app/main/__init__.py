from flask import Blueprint

main = Blueprint('main', __name__)
# the bp name and the module or package
# print(__name__) #app.main
from . import views, errors
