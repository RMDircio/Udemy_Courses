# Set up your imports and your flask app.
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('07-exam-index.html')


# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements
    ''' 
    1. Username must contain a lowercase letter
    2. Username must contain an uppercase letter
    3. Username must end in a number
    '''
    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # set up the rules - False as default
    lower = False
    upper = False
    end_number = False
    username = request.args.get('username')

    # # Fancy for loops
    # lower = any(c.islower() for c in username)
    # upper = any(c.isupper() for c in username)
    # end_number = username[-1].isdigit()

    # another way - not as fancy
    for letter in username:
        if letter == letter.lower():
            lower = True
        if letter == letter.upper():
            upper = True
        if letter[-1].isdigit():
            end_number = True
    

    # Check if all are True.
    report = lower and upper and end_number 
   
    # Return the information to the report page html.
    return render_template('07-exam-report.html',report=report,
                           lower=lower,upper=upper,
                           num_end=end_number)


if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True)
