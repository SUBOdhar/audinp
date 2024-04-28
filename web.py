from flask import Flask, render_template_string, request

# Create a Flask application instance
app = Flask(__name__)

# Define the HTML content with the input box
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App with Input Box</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>Welcome to Audinp</h1>
    <form method="POST" autocomplete="off">
        <label for="name">Enter  data in neplai:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    </form>
   <div class="highlight">
    {% if name %}
        <p>Hello, {{ name }}!</p>
    {% endif %}
   </div>
</body>
</html>
"""

# Define a route to render the HTML page with an input box


@app.route('/', methods=['GET', 'POST'])
def index():
    # Check if a POST request with form data is received
    if request.method == 'POST':
        # Get the value entered in the input box named 'name'
        user_name = request.form['name']
        # Render the HTML template with the personalized greeting message
        return render_template_string(html_content, name="Data added successfully")
    # Render the HTML template with an empty input box
    return render_template_string(html_content, name='')


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
