from flask import Flask, render_template
import json

"""Flask app serving pages and an item list from a JSON file."""

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render items page from items.json."""
    with open('items.json', 'r') as file:
        data = json.load(file)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    """Run the Flask app on port 5000 in debug mode."""
    app.run(debug=True, port=5000)
