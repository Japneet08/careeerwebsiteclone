from flask import Flask, render_template
# give flask app a name
app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi, India',
    # 'salary':'Rs. 15,00,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':'Rs. 12,00,000'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'San Francisco, USA',
    'salary':'$120,000'  
  }
]

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
  return render_template("home.html", jobs=JOBS)
# templates are used to decide what is displayed on webpage 

if (__name__) == "__main__":
  app.run(host='0.0.0.0', debug=True)
