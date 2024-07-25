from flask import Flask, render_template, request, url_for
app = Flask(__name__)

# A dictionary of UserProfiles
# key: username
# value: a UserProfile
user_dictionary = {}

# TODO: Fix age
#TODO: Add lname to the UserProfile class. Include it in the constructor!
class UserProfile:
    def __init__(self, fname, email, phone):
        self.fname = fname
        self.email = email
        self.phone = phone

    def __str__(self):
        return "I am " + self.fname
    

@app.route("/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        #etc.
         
        # TODO: Create a UserProfile for the user
        # and store them in the user_dictionary
        # be sure to use the username as the key
        # and the UserProfile as the value

    return render_template("create_profile.html", 
                           users = user_dictionary,
                           url=url_for("signup"))


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)