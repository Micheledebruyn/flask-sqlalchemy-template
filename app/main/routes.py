from app.models import User
from . import main


@main.route('/')
def say_hello():
  return "<h1>Hello there</h1>"
