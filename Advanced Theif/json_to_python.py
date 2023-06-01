import json
from jinja2 import Template

# Read the JSON file
with open('input.json') as file:
    data = json.load(file)

# Process and format the data
# Modify this section based on your specific requirements

# Create a template for the HTML output
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Formatted Output</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <style>
        body {
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Formatted Output</h1>
        <pre id="formatted-data"></pre>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script>
        $(document).ready(function() {
            $.getJSON("input.json", function(data) {
                var formattedData = JSON.stringify(data, null, 4);
                $("#formatted-data").text(formattedData);
            });
        });
    </script>
</body>
</html>

"""

# Render the template with the formatted data
template = Template(html_template)
output = template.render(formatted_data=json.dumps(data, indent=4))

# Save the rendered output as an HTML file
with open('output.html', 'w') as file:
    file.write(output)
