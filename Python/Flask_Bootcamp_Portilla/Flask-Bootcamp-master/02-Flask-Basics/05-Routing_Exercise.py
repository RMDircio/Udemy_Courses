# Set up your imports here!
from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/') # Fill this in!
def index():
    # Create a generic welcome page.
    return '<h1>Hello Puppers!</h1>'
    

@app.route('/latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    
    # if the name does end with 'y'
    if name[-1] == 'y':
        # remove the 'y' + add 'iful' to the name
        changed_name = name[:-1] + 'iful'
        return 'Your new name is {}'.format(changed_name)
        
    
    # if the name does not end with 'y'
    else:
        # add an 'y' to the end of the name
        changed_name = name + 'y'
        return 'Your new name is {}'.format(changed_name)


if __name__ == '__main__':
    app.run(debug=True)
