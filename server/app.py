#!/usr/bin/env python3

from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the base URL ('/')
@app.route('/')
def index():
    # Render an HTML template with the title
    title = "Python Operations with Flask Routing and Views"
    return f"<h1>{title}</h1>"

# Define a route for the '/print/<string_param>' URL
@app.route('/print/<string_param>')
def print_string(string_param):
    # Print the string to the console and display it in the browser
    print(string_param)
    return string_param

# Define a route for the '/count/<int_param>' URL
@app.route('/count/<int_param>')
def count(int_param):
    # Display numbers in the range of int_param on separate lines
    numbers = "\n".join(map(str, range(1, int_param + 1)))
    return numbers

# Define a route for the '/math/<float:num1>/<operation>/<float:num2>' URL
@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    # Perform mathematical operations based on the operation parameter
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Division by zero is not allowed"
    elif operation == '%':
        result = num1 % num2

    return str(result)

# Run the Flask application on port 5555 with debug mode enabled
if __name__ == '__main__':
    app.run(port=5555, debug=True)
