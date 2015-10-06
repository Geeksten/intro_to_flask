from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "<a href = '/hello'> Hi! This is the home page.</a>"

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet">
                <label>What's your name? <input type="text" name="person"></label>
                <input type="submit">
                <br>
                <label>Compliment
                <input type="radio" approve="yesno" value="yes">Yes
                <input type="radio" approve="yesno" value="no">No
                </label>
                <br>
                <label>Qualities
                <select>
                <option value="awesome">awesome</option>
                <option value="wonderful">wonderful</option>
                <option value="tenacious">tenacious</option>
                </select>
                </label>
            </form>
        </body>
    </html>

    """

@app.route('/greet')
def greet_person():
    player = request.args.get("person")
    nice_thing = choice(AWESOMENESS)
    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s!
        </body>
    </html>""" % (player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
