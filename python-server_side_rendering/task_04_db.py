from flask import Flask, render_template, request
import json
import csv
import sqlite3

"""Flask app to display products from JSON, CSV, or SQLite database."""

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


def read_sql(db_path="products.db"):
    """Read and return products from a SQLite database."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        return products
    except sqlite3.Error as e:
        raise Exception(f"Database error: {e}")


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
    elif source == "sql":
        try:
            products_list = read_sql("products.db")
        except Exception as e:
            error = f"Error reading database: {e}"
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
