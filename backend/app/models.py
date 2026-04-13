from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Category Model

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # relationship
    products = db.relationship('Product', backref='category')



# Supplier Model

class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    products = db.relationship('Product', backref='supplier')



# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)
    stock = db.Column(db.Integer, default=0)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))



# Inventory Transaction Model

class InventoryTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)

    # "in" for adding stock, "out" for removing stock
    transaction_type = db.Column(db.String(10))

    created_at = db.Column(db.DateTime, server_default=db.func.now())