from flask import Flask, render_template_string

app = Flask(__name__)

# Sample data for the table
data = [
    ('D8:94:03:FA:37:D5', 'Hewlett Packard Enterprise – WW Corporate Headquarters'),
    ('F0:B4:D2:AB:0B:0A', 'D-Link International'),
    ('C8:8A:9A:16:E3:A1', 'Intel Corporate')
]

# HTML template to render the table
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MAC Address Table</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f4f4f9;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 8px;
            text-align: left;
            border: 1px solid #ddd;
        }
        th {
            background-color: #f2f2f2;
        }
        h1 {
            text-align: center;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>MAC Address Table</h1>
    <table>
        <thead>
            <tr>
                <th>MAC Address</th>
                <th>Corporation</th>
            </tr>
        </thead>
        <tbody>
            {% for mac, corp in data %}
            <tr>
                <td>{{ mac }}</td>
                <td>{{ corp }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>
"""



# Route to render the table
@app.route('/')
def home():
    return render_template_string(html_template, data=data)

if __name__ == '__main__':
    app.run(debug=True)
