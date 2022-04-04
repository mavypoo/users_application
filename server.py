from flask import Flask, render_template, request, redirect
# import the class from user.py
from user import User


app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def all_users():
    users = User.get_all()
    # users is the list users =[] in the get_all class method. Friend is the class. get)all is the method name
    print(users)
    return render_template("read.html", all_users=users)

@app.route("/users/new")
def new_users():
    return render_template("create.html")


@app.route('/users/add', methods=['POST'])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email":request.form["email"]
    }
    # We pass the data dictionary into the save method from the User class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')
            
if __name__ == "__main__":
    app.run(debug=True)