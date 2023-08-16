from flask import Flask, render_template

app = Flask(__name__)

products_data = {
    'Cloth': [
        {'name': 'Shirt', 'price': 1000},
        {'name': 'Jeans', 'price': 2000},
        # Add more products...
    ],
    'Shoes': [
        {'name': 'Sneakers', 'price': 2500},
        {'name': 'Boots', 'price': 3000},
        # Add more products...
    ],
    'Jacket': [
        {'name': 'Windcheater', 'price': 3500},
        {'name': 'Down jacket', 'price': 5000},
        # Add more products...
    ]
}


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/category/<category_name>')
def category(category_name):
    if category_name in products_data:
        products = products_data[category_name]
        return render_template('category.html', category_name=category_name, products=products)
    else:
        return "Category not found"


@app.route('/product/<product_name>')
def product(product_name):
    for cat, products in products_data.items():
        for prod in products:
            if product_name == prod['name']:
                price = prod['price']
                return render_template('product.html', product_name=product_name, price=price)
    return "Product not found"


if __name__ == '__main__':
    app.run(debug=True)
