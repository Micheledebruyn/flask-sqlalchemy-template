from . import main
from app.models import User
from app.helpers.api_helper import say_hello_again # Example of import from helpers

@main.route('/')
def say_hello():
  return "<h1>Hello there</h1>"
