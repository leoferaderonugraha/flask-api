from flask import request, jsonify
from env import app, db, mm

# Models
from Models.ProductModel import Product, ProductSchema

# Init schema
productSchema = ProductSchema()
manyProductSchema = ProductSchema(many=True)

# Create a product
def addProduct():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    newProduct = Product(name, description, price, qty)

    db.session.add(newProduct)
    db.session.commit()

    return productSchema.jsonify(newProduct)

# Get all products
def getProducts():
    allProducts = Product.query.all()
    result = manyProductSchema.dump(allProducts)

    return jsonify(result)

# Get single product
def getProduct(id):
    product = Product.query.get(id)
    return productSchema.jsonify(product)

# Update a product
def updateProduct(id):
    product = Product.query.get(id)
    
    product.name = request.json['name']
    product.description = request.json['description']
    product.price = request.json['price']
    product.qty = request.json['qty']

    db.session.commit()

    return productSchema.jsonify(product)

# Delete a product
def deleteProduct(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return productSchema.jsonify(product)