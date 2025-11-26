# ====================================================================
# Task 2: tests/test_models.py (Code Snippets for Model Tests)
# Note: Assume necessary imports (unittest, Product, ProductFactory, db) are present
# ====================================================================

# Task 2a: READ test case
def test_read_a_product(self):
    """It should Read a Product"""
    product = ProductFactory()
    product.create()
    found_product = Product.find(product.id)
    self.assertEqual(found_product.id, product.id)
    self.assertEqual(found_product.name, product.name)

# Task 2b: UPDATE test case
def test_update_a_product(self):
    """It should Update a Product's name and save it"""
    product = ProductFactory(name="Old Name")
    product.create()
    
    # Update the name
    product.name = "New Name"
    product.update()
    self.assertEqual(product.name, "New Name")
    
    # Verify the update persisted
    found_product = Product.find(product.id)
    self.assertEqual(found_product.name, "New Name")

# Task 2c: DELETE test case
def test_delete_a_product(self):
    """It should Delete a Product"""
    product = ProductFactory()
    product.create()
    self.assertEqual(len(Product.all()), 1)
    
    product.delete()
    self.assertEqual(len(Product.all()), 0)
    self.assertIsNone(Product.find(product.id))

# Task 2d: LIST ALL test case
def test_list_all_products(self):
    """It should List all Products in the database"""
    ProductFactory.create_batch(5)
    self.assertEqual(len(Product.all()), 5)

# Task 2e: FIND BY NAME test case
def test_find_by_name(self):
    """It should Find Products by Name"""
    ProductFactory(name="Widget").create()
    ProductFactory(name="Gizmo").create()
    ProductFactory(name="Widget").create()
    
    products = Product.find_by_name("Widget")
    self.assertEqual(len(products), 2)
    for product in products:
        self.assertEqual(product.name, "Widget")

# Task 2f: FIND BY CATEGORY test case
def test_find_by_category(self):
    """It should Find Products by Category"""
    ProductFactory(category="Electronics").create()
    ProductFactory(category="Books").create()
    ProductFactory(category="Electronics").create()
    
    products = Product.find_by_category("Electronics")
    self.assertEqual(len(products), 2)
    for product in products:
        self.assertEqual(product.category, "Electronics")

# Task 2g: FIND BY AVAILABILITY test case
def test_find_by_availability(self):
    """It should Find Products by Availability"""
    ProductFactory(available=True).create()
    ProductFactory(available=False).create()
    ProductFactory(available=True).create()
    
    products = Product.find_by_availability(True)
    self.assertEqual(len(products), 2)
    for product in products:
        self.assertEqual(product.available, True)
