# ====================================================================
# Task 1: tests/factories.py (Code for ProductFactory)
# ====================================================================
import factory
from service.models import Product  # Assumes your Product model is here

class ProductFactory(factory.Factory):
    """Factory for creating fake Products"""
    class Meta:
        model = Product
        # Prevent factory_boy from trying to create an object when generating data
        # Adjust based on your model's implementation
        
    id = factory.Sequence(lambda n: n)
    name = factory.Faker("word")
    category = factory.Faker("random_element", elements=["Electronics", "Clothing", "Books", "Home Goods"])
    available = factory.Faker("boolean")
    price = factory.Faker("pydecimal", left_digits=2, right_digits=2, positive=True)
    
# Example use: product = ProductFactory()
