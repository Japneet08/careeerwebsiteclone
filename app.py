from flask import Flask
# give flask app a name
app = Flask(__name__)


# name application
# creating a route
@app.route(
    "/"
)  # telling the flask that when a particular url is selected what should be returned
# route is a part of url after the domain name and everything after that is a path or a route
# @ -> decorator in python
# route is a function
# / is an empty route
# what should be returned when the route is selected
# when url / is accessed then show hello world

# DEFINING A FUNCTION
def hello_world():
  return "Hello World"


if (__name__) == "__main__":
  app.run(host='0.0.0.0', debug=True)
