from flask import Flask, render_template, request, jsonify
from models import db, Product, Supplier, Category
from flask_migrate import Migrate

# Инициализация приложения и базы данных
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://admin:1111@localhost:5432/testpost'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация SQLAlchemy и Migrate
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)



@app.route('/add_product', methods=['POST'])
def add_product():
    try:
        name = request.form['name']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        category_name = request.form['category']
        supplier_name = request.form['supplier']

        # Найти или создать категорию
        category = Category.query.filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            db.session.add(category)

        # Найти или создать поставщика
        supplier = Supplier.query.filter_by(name=supplier_name).first()
        if not supplier:
            supplier = Supplier(name=supplier_name)
            db.session.add(supplier)

        # Добавить товар
        product = Product(name=name, quantity=quantity, price=price,
                          category=category, supplier=supplier)
        db.session.add(product)
        db.session.commit()

        return jsonify({
            'status': 'success',
            'message': 'Product added successfully',
            'product': {
                'name': product.name,
                'quantity': product.quantity,
                'price': product.price,
                'category': category.name,
                'supplier': supplier.name
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': f'Failed to add product: {str(e)}'
        }), 400


@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({
            'status': 'error',
            'message': f'Product with id {id} not found'
        }), 404

    if request.method == 'GET':
        return jsonify({
            'status': 'success',
            'product': {
                'id': product.id,
                'name': product.name,
                'quantity': product.quantity,
                'price': product.price,
                'category': product.category.name if product.category else None,
                'supplier': product.supplier.name if product.supplier else None
            }
        })

    if request.method == 'POST':
        try:
            product.name = request.form['name']
            product.quantity = int(request.form['quantity'])
            product.price = float(request.form['price'])
            category_name = request.form['category']
            supplier_name = request.form['supplier']

            category = Category.query.filter_by(name=category_name).first()
            if not category:
                category = Category(name=category_name)
                db.session.add(category)

            supplier = Supplier.query.filter_by(name=supplier_name).first()
            if not supplier:
                supplier = Supplier(name=supplier_name)
                db.session.add(supplier)

            product.category = category
            product.supplier = supplier

            db.session.commit()

            return jsonify({
                'status': 'success',
                'message': 'Product updated successfully',
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'quantity': product.quantity,
                    'price': product.price,
                    'category': category.name,
                    'supplier': supplier.name
                }
            }), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({
                'status': 'error',
                'message': f'Failed to update product: {str(e)}'
            }), 400


@app.route('/delete_product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({
        'status': 'success',
        'message': 'Product delete successfully',


    }), 200

@app.route('/get_product_all', methods=['GET'])
def get_product_all():
    products = Product.query.all()

    product_list = []
    for product in products:
        product_list.append({
            'id': product.id,
            'name': product.name,
            'quantity': product.quantity,
            'price': product.price,
            'category': product.category.name if product.category else None,
            'supplier': product.supplier.name if product.supplier else None
        })

    # Возвращаем JSON-ответ
    return jsonify({
        'status': 'success',
        'data': product_list
    }), 200


if __name__ == '__main__':
    app.run(debug=True, port=8000)