from flask import Blueprint, request, jsonify
from app.models import db, Product

product_bp = Blueprint('products', __name__)

# CREATE PRODUCT

@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.json

    new_product = Product(
        name=data['name'],
        price=data.get('price', 0),
        stock=0
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product created"}), 201



# GET ALL PRODUCTS
@product_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()

    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "stock": p.stock
        })

    return jsonify(result), 200



# UPDATE PRODUCT

@product_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.json

    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)

    db.session.commit()

    return jsonify({"message": "Product updated"}), 200



# DELETE PRODUCT

@product_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted"}), 200