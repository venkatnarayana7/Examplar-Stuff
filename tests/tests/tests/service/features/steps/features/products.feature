# ====================================================================
# Task 6: features/products.feature (BDD Scenarios)
# ====================================================================
Feature: Product Inventory Management
  The Product service provides a RESTful API to list, retrieve, update, and delete products
  
  Background:
    Given the following products
      | name | category | available | price |
      | T-Shirt | Clothing | True | 19.99 |
      | Laptop | Electronics | True | 899.99 |
      | Book | Books | False | 12.50 |
      | Sweater | Clothing | True | 45.00 |

# Task 6a: BDD Scenario for READING a Product
Scenario: Read a Product
  When I visit the "homepage"
  And I click the "List Products" button
  And I select "Laptop" in the "product_name" dropdown
  And I click the "Retrieve" button
  Then I should see the name "Laptop" in the "product_name" field

# Task 6b: BDD Scenario for UPDATING a Product
Scenario: Update a Product
  When I visit the "homepage"
  And I click the "List Products" button
  And I select "Laptop" in the "product_name" dropdown
  And I click the "Retrieve" button
  Then I should see the name "Laptop" in the "product_name" field
  When I set the "product_price" to "799.99"
  And I click the "Update" button
  Then I should see the message "Product has been updated"
  When I click the "Retrieve" button
  Then I should see "799.99" in the "product_price" field

# Task 6c: BDD Scenario for DELETING a Product
Scenario: Delete a Product
  Given a Product with name "Test_Delete" exists
  When I visit the "homepage"
  And I click the "List Products" button
  And I select "Test_Delete" in the "product_name" dropdown
  And I click the "Retrieve" button
  Then I should see the name "Test_Delete" in the "product_name" field
  When I click the "Delete" button
  Then I should see the message "Product has been deleted"
  When I click the "List Products" button
  Then I should not see "Test_Delete"

# Task 6d: BDD Scenario for LISTING ALL PRODUCTS
Scenario: List All Products
  When I visit the "homepage"
  And I click the "List Products" button
  Then I should see 4 products in the results

# Task 6e: BDD Scenario for Searching a Product based on Category
Scenario: Search Products by Category
  When I visit the "homepage"
  And I set the "Search_Category" to "Clothing"
  And I click the "Search" button
  Then I should see 2 products in the results
  And I should see "T-Shirt"
  And I should see "Sweater"
  And I should not see "Laptop"

# Task 6f: BDD Scenario for Searching a Product based on Availability
Scenario: Search Products by Availability
  When I visit the "homepage"
  And I set the "Search_Available" to "False"
  And I click the "Search" button
  Then I should see 1 product in the results
  And I should see "Book"
  And I should not see "Laptop"

# Task 6g: BDD Scenario for Searching a Product based on Name
Scenario: Search Products by Name
  When I visit the "homepage"
  And I set the "Search_Name" to "T-Shirt"
  And I click the "Search" button
  Then I should see 1 product in the results
  And I should see "T-Shirt"
  And I should not see "Laptop"
