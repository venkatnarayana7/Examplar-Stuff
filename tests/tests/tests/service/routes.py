# ====================================================================
# Task 4: service/routes.py (Code Snippets for Route Functions)
# Note: Assume imports (app, Product, STATUS_CODES) and route decorators are present
# ====================================================================

# Task 4a: READ function (GET /products/{id})
@app.route("/products/<int:product_id>", methods=["GET"])
def get_products(product_id):
    """
    Retrieve a single Product
    This endpoint returns a Product based on its id
    """
    app.logger.info(f"Request to retrieve product with id: {product_id}")
    product = Product.find(product_id)
    if not product:
        return {"message": f"Product with id '{product_id}' was not found."}, STATUS_CODES["NOT_FOUND"]
    return product.serialize(), STATUS_CODES["OK"]

# Task 4b: UPDATE function (PUT /products/{id})
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_products(product_id):
    """
    Update a Product
    This endpoint will update a Product based on the body that is posted
    """
    app.logger.info(f"Request to update product with id: {product_id}")
    product = Product.find(product_id)
    if not product:
        return {"message": f"Product with id '{product_id}' was not found."}, STATUS_CODES["NOT_FOUND"]

    # This assumes the Product.deserialize method handles updating attributes
    product.deserialize(app.current_request.get_json())
    product.update()
    return product.serialize(), STATUS_CODES["OK"]

# Task 4c: DELETE function (DELETE /products/{id})
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_products(product_id):
    """
    Delete a Product
    This endpoint will delete a Product based on the id specified in the path
    """
    app.logger.info(f"Request to delete product with id: {product_id}")
    product = Product.find(product_id)
    if product:
        product.delete()
    # 204 is the recommended status code for a successful delete
    return "", STATUS_CODES["NO_CONTENT"]

# Task 4d: LIST ALL / LIST BY NAME / LIST BY CATEGORY and LIST BY AVAILABILITY function (GET /products)
@app.route("/products", methods=["GET"])
def list_products():
    """Returns a list of Products"""
    app.logger.info("Request to list Products...")
    
    # Check for query parameters for searching
    name = app.current_request.args.get("name")
    category = app.current_request.args.get("category")
    available = app.current_request.args.get("available")

    if name:
        products = Product.find_by_name(name)
    elif category:
        products = Product.find_by_category(category)
    elif available:
        # Convert string 'True'/'False' to boolean
        is_available = available.lower() in ["true", "t", "1"]
        products = Product.find_by_availability(is_available)
    else:
        # If no query params, list all
        products = Product.all()

    results = [product.serialize() for product in products]
    return results, STATUS_CODES["OK"]
