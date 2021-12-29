from flask import Flask
app = Flask(__name__)

print(__name__)

def make_bold(function):
    def wrapped():
        result = f'<b>{function()}</b>'
        return result
    return wrapped

def make_emphasis(function):
    def wrapped():
        result = f'<em>{function()}</em>'
        return result
    return wrapped

def make_underlined(function):
    def wrapped():
        result = f'<u>{function()}</u>'
        return result
    return wrapped


# When user navigates to home page:
# Python decorator. Provides additional functionality to existing function.
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" width=500px>'

# Provide different routes using the #app.route decorator
@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    Text = "Bye"
    return Text

# Creating variable paths and converting the path to a specified data type
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, you are {number} years old!"

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload and access debug console from within browser.
    app.run(debug=True)