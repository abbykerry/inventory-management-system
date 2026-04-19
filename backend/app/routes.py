from flask import Blueprint, request, jsonify
from app import db
from app.models import Product, InventoryTransaction

# Blueprint (this groups all product-related routes)
product_bp = Blueprint('products', __name__)


# CREATE PRODUCT
@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.json

    # FIX: prevent KeyError + invalid request
    if not data or 'name' not in data:
        return jsonify({"error": "Product name is required"}), 400

    new_product = Product(
        name=data['name'],
        price=data.get('price', 0),
        stock=0
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify({
        "message": "Product created",
        "product_id": new_product.id
    }), 201


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


# INVENTORY TRANSACTIONS (MAIN TASK)
@product_bp.route('/transactions', methods=['POST'])
def handle_transaction():
    data = request.json

    # FIX: prevent KeyError crashes
    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    if 'product_id' not in data or 'quantity' not in data or 'transaction_type' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    product = Product.query.get(data['product_id'])

    if not product:
        return jsonify({"error": "Product not found"}), 404

    quantity = data['quantity']
    transaction_type = data['transaction_type']

    # validate quantity
    if quantity <= 0:
        return jsonify({"error": "Quantity must be greater than 0"}), 400

    # ADD STOCK
    if transaction_type == "in":
        product.stock += quantity

    # REMOVE STOCK
    elif transaction_type == "out":
        if product.stock < quantity:
            return jsonify({"error": "Not enough stock"}), 400
        product.stock -= quantity

    else:
        return jsonify({"error": "Invalid transaction type"}), 400

    # Save transaction record (ledger system)
    transaction = InventoryTransaction(
        product_id=product.id,
        quantity=quantity,
        transaction_type=transaction_type
    )

    db.session.add(transaction)
    db.session.commit()

    return jsonify({
        "message": "Transaction successful",
        "current_stock": product.stock
    }), 201