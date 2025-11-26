# ====================================================================
# Task 3: tests/test_routes.py (Code Snippets for Route Tests)
# Note: Assume necessary imports (unittest, app, Product, ProductFactory) are present
# ====================================================================

# Task 3a: READ test case (GET /products/{id})
def test_get_a_product(self):
    """It should Get a single Product"""
    product = ProductFactory()
    product.create()
    resp = self.client.get(f"/products/{product.id}")
    self.assertEqual(resp.status_code, 200)
    data = resp.get_json()
    self.assertEqual(data["name"], product.name)

# Task 3b: UPDATE test case (PUT /products/{id})
def test_update_product(self):
    """It should Update an existing Product"""
    product = ProductFactory(name="Old Name", price=10.00)
    product.create()
    
    new_data = product.serialize()
    new_data["name"] = "New Name"
    new_data["price"] = 25.00

    resp = self.client.put(f"/products/{product.id}", json=new_data)
    self.assertEqual(resp.status_code, 200)
    
    # Check if the product was actually updated in the DB
    updated_product = Product.find(product.id)
    self.assertEqual(updated_product.name, "New Name")

# Task 3c: DELETE test case (DELETE /products/{id})
def test_delete_product(self):
    """It should Delete a Product"""
    product = ProductFactory()
    product.create()
    self.assertEqual(len(Product.all()), 1)
    
    resp = self.client.delete(f"/products/{product.id}")
    self.assertEqual(resp.status_code, 204) # No Content
    self.assertEqual(len(Product.all()), 0)

# Task 3d: LIST ALL test case (GET /products)
def test_get_product_list(self):
    """It should Get a list of Products"""
    ProductFactory.create_batch(5)
    resp = self.client.get("/products")
    self.assertEqual(resp.status_code, 200)
    data = resp.get_json()
    self.assertEqual(len(data), 5)

# Task 3e: LIST BY NAME test case (GET /products?name={name})
def test_query_product_list_by_name(self):
    """It should Find Products by Name"""
    ProductFactory(name="Widget").create()
    ProductFactory(name="Gizmo").create()
    ProductFactory(name="Widget").create()
    
    resp = self.client.get("/products", query_string="name=Widget")
    self.assertEqual(resp.status_code, 200)
    data = resp.get_json()
    self.assertEqual(len(data), 2)
    self.assertEqual(data[0]["name"], "Widget")

# Task 3f: LIST BY CATEGORY test case (GET /products?category={category})
def test_query_product_list_by_category(self):
    """It should Find Products by Category"""
    ProductFactory(category="Electronics").create()
    ProductFactory(category="Books").create()
    ProductFactory(category="Electronics").create()
    
    resp = self.client.get("/products", query_string="category=Electronics")
    self.assertEqual(resp.status_code, 200)
    data = resp.get_json()
    self.assertEqual(len(data), 2)
    self.assertEqual(data[0]["category"], "Electronics")

# Task 3g: LIST BY AVAILABILITY test case (GET /products?available={boolean})
def test_query_product_list_by_availability(self):
    """It should Find Products by Availability"""
    ProductFactory(available=True).create()
    ProductFactory(available=False).create()
    ProductFactory(available=True).create()
    
    resp = self.client.get("/products", query_string="available=True")
    self.assertEqual(resp.status_code, 200)
    data = resp.get_json()
    self.assertEqual(len(data), 2)
    self.assertTrue(data[0]["available"])
