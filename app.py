from env import app

# Controllers
from Controllers.ProductController import addProduct, getProduct, getProducts, updateProduct, deleteProduct

# Routes
app.add_url_rule('/product', view_func=addProduct, methods=['POST'], strict_slashes=False)
app.add_url_rule('/product', view_func=getProducts, methods=['GET'], strict_slashes=False)
app.add_url_rule('/product/<id>', view_func=getProduct, methods=['GET'])
app.add_url_rule('/product/<id>', view_func=updateProduct, methods=['PUT'])
app.add_url_rule('/product/<id>', view_func=deleteProduct, methods=['DELETE'])

# Run server
if __name__ == '__main__':
    app.run(debug=True)