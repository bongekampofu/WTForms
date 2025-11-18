from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key_here"


class Register(FlaskForm):
    email_address = EmailField("Email Address:",
                               validators=[InputRequired(), Length(min=4)])

    first_name = StringField("First Name:",
                             validators=[InputRequired(), Length(max=25)])

    last_name = StringField("Last Name:",
                            validators=[InputRequired(), Length(max=25)])

    password = PasswordField("Password:",
                             validators=[InputRequired(), Length(min=8, max=25)])

    house_number = StringField("House Number:",
                               validators=[InputRequired(), Length(max=25)])

    street_name = StringField("Street Name:",
                              validators=[InputRequired(), Length(max=35)])

    country = StringField("Country:",
                          validators=[InputRequired(), Length(max=35)])

    post_code = StringField("Post Code:",
                            validators=[InputRequired(), Length(max=7)])


@app.route("/register", methods=["GET", "POST"])
def register():
    form = Register()

    if form.validate_on_submit():
        # When form passes all validation
        return render_template("success.html",
                               first_name=form.first_name.data,
                               last_name=form.last_name.data)

    # If GET or validation fails
    return render_template("register.html", form=form)


@app.route("/")
def home():
    return redirect(url_for("register"))


# Run the App
if __name__ == "__main__":
    app.run(debug=True)
