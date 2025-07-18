#!/usr/bin/python3
import csv

from flask import Flask, render_template, request
import json
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def abour():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json') as file:
            data = json.load(file)
            itemList = data.get("items", [])

    except Exception as e:
        itemList = []
        print(f"Error: {e}")

    return render_template('items.html', items=itemList)

def read_json(somefile):
    try:
        with open(somefile, 'r') as file:
            return json.load(file)
    except Exception as e:
        return None


def read_csv(somefile):
    try:
        with open(somefile, 'r', newline='') as file:
            reader = csv.DictReader(file)
            products = []
            for row in reader:
                products.append(
                    {
                        "id": int(row["id"]),
                        "name": str(row["name"]),
                        "category": str(row['category']),
                        "price": float(row["price"])
                    }
                )
            return products

    except Exception as e:
        return None


@app.route('/products')
def product_display():
    source = request.args.get('source')
    if source == 'json':
        try:
           products = read_json("products.json")
        except Exception as e:
            return render_template("product_display.html", error="Failed to open JSON")
        return  render_template("product_display.html", products=products)
    elif source == 'csv':
        try:
            products = read_csv("products.csv")
        except Exception as e:
            return render_template("product_display.html", error="Failed to open csv")


        return render_template("product_display.html", products=products)
    else:
        return render_template("product_display.html", error="Failed")


    if product_data is None:
        error_message = f"Could not read data from {source} file."
        return render_template('product_display.html', error=error_message)

    if id_Of_Product:
        try:
            product_id = int(id_param)
            product_data = [p for p in product_data if p["id"] == product_id]
            if not product_data:
                error_message = f"Product with ID {product_id} not found."
        except ValueError:
            error_message = "ID must be an integer."

        return render_template('product_display.html', products=product_data, error=error_message)

if __name__=="__main__":
    app.run(debug=True, port=5000)
