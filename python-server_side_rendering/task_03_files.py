from flask import Flask, render_template, request
import json
import csv

"""Flask app to display products from JSON or CSV files."""


app = Flask(__name__)


def read_json(file_path):
    """Read and return data from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)


def read_csv(file_path):
    """Read and return data from a CSV file with id and price parsed."""
    products = []
    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products


@app.route("/products")
def products():
    """Render products page filtered by source and optional id."""
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)
    error = None
    products_list = []

    if source == "json":
        try:
            products_list = read_json("products.json")
        except Exception as e:
            error = f"Error reading JSON: {e}"
    elif source == "csv":
        try:
            products_list = read_csv("products.csv")
        except Exception as e:
            error = f"Error reading CSV: {e}"
    else:
        error = "Wrong source"

    if not error and product_id is not None:
        filtered = [
            product
            for product in products_list
            if product["id"] == product_id
        ]
        if filtered:
            products_list = filtered
        else:
            error = "Product not found"
            products_list = []

    return render_template(
        "product_display.html", products=products_list, error=error
    )


if __name__ == "__main__":
    """Run the Flask app on port 5000 in debug mode."""
    app.run(debug=True, port=5000)
