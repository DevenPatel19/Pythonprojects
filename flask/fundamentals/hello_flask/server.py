from flask import Flask, render_template  # Import Flask to allow us to create our app 
app = Flask(__name__)    # Create a new instance of the Flask class called "app"




@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    """This is the root route."""
    
    name = "Deven"
                           #template variable = value
    return render_template("index.html", name = name)



@app.route("/<person>")
def greet_person(person):
    """
    This is a dynamic route that displays the name 
    passed into the URL
    """

    return render_template("index.html", banana=person)



@app.route("/<time_of_day>/<person>")
def greet_person_with_time(time_of_day, person):
    """Greet a person with the time aof day"""


# when using many many variables, use a dictionary and use the dynamic variable way( "**" prior to variable)
    context = {"time_of_day": time_of_day, "person": person}

    print(context)
  

    return render_template("greet_time.html", **context)


@app.route('/Success')
def success():
    return 'Success'


# Here the second parameter is cast into an integer before being passed to the function
@app.route('/hello/<name>/<int:num>') 
def hello(name, num):
    return f"Hello, {name * num}"



@app.route("/muppets")
def list_muppets():
    """This displays a template that lists some Muppets."""

    muppets = [
        {"name" : "Kermit the Frog", "location":"The swamp. I'm a frog."},
        {"name" : "Miss Piggy", "location":"The green room. Where's my champagne?"},
        {"name" : "Fozzy Bear", "location":"The Comedy Store - tonight at 8!"},
        {"name" : "Gonzo the Great", "location":"Waiting to be shot out of a cannon."},
    ]

    return render_template("muppets.html", muppets = muppets)



@app.route("/age-checker/<int:age>")
def age_checker(age):
    """Display a template that checks if the user is over 21"""

    return render_template("age-checker.html", age=age)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

