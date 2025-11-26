# ====================================================================
# Task 5a: features/steps/load_steps.py (Code Snippet for loading data)
# Note: This is typically inside a @given decorator function
# ====================================================================
@given('the following products')
def step_impl(context):
    """Loads a table of products into the database"""
    for row in context.table:
        product = Product(
            name=row['name'],
            category=row['category'],
            available=row['available'].lower() == 'true',
            price=float(row['price'].replace('$', '').strip())
        )
        product.create()
