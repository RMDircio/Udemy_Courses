from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey' # this is a dictonary configuration

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html

class InfoForm(FlaskForm): # can choose any name for Class - must inherit from FlaskForm
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''

    # these are the Class attributes
    breed = StringField('What breed are you?') # StringField sets the type of label 
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST']) # method helps get/post info to/from forms
def index():
    # Set the breed to a boolean False.
    # So we can use it in an if statement in the html.
    breed = False

    # Create instance of the form.
    form = InfoForm()

    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit(): # if it is True
        # Grab the data from the breed on the form.
        breed = form.breed.data # form.attribute.data = get the value submited from the form
        # Reset the form's breed data to be False/Empty
        form.breed.data = ''

    return render_template('00-home.html', form=form, breed=breed)


if __name__ == '__main__':
    app.run(debug=True)
