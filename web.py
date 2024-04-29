from flask import Flask, render_template_string, request
from data.data import create_table, insert_data, check_existing_data
from unicode.cnv import is_nepali
import engine.engine as engi

# Your Flask application code remains the same
app = Flask(__name__)


# HTML template remains the same as well
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
        <label for="name">Enter data in Nepali:</label>
        <input type="text" id="name" name="name">
        <input type="submit" value="Submit">
    </form>
   <div class="highlight">
    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
   </div>
</body>
</html>
"""

# Route to handle both GET and POST requests remains the same


@app.route('/', methods=['GET', 'POST'])
def index():
    # Create the table if not exists
    create_table()

    if request.method == 'POST':
        user_data = request.form['name']
        if len(user_data) != 0:
            if not is_nepali(user_data):
                message = "Please enter data in Nepali!"
            else:
                # Convert Nepali data to Unicode
                unicode_data = engi.split_convert_to_unicode(user_data)
                if unicode_data is None:
                    message = "Could not convert data to Unicode!"
                else:
                    # Check if the data already exists in the database
                    if check_existing_data(unicode_data):
                        message = "Data already exists!"
                    else:
                        # Insert the data into the database
                        insert_data(unicode_data)
                        message = "Data added successfully!"
        else:
            message = "Field is empty"
        return render_template_string(html_content, message=message)
    return render_template_string(html_content, message='')


# Main entry point remains the same
if __name__ == '__main__':
    app.run(debug=True)
