import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_fresh_india.settings')
django.setup()

from products.models import Category, Product, Farmer
from django.contrib.auth.models import User

# Create Categories
def create_categories():
    # Normal Categories
    categories = [
        {
            'name': 'Normal Anaj',
            'category_type': 'normal',
            'sub_category': 'anaj',
            'description': 'Traditional grains grown using conventional farming methods.'
        },
        {
            'name': 'Normal Fruits',
            'category_type': 'normal',
            'sub_category': 'fruits',
            'description': 'Fresh fruits grown using conventional farming methods.'
        },
        {
            'name': 'Normal Vegetables',
            'category_type': 'normal',
            'sub_category': 'vegetables',
            'description': 'Fresh vegetables grown using conventional farming methods.'
        },
        # Organic Categories
        {
            'name': 'Organic Anaj',
            'category_type': 'organic',
            'sub_category': 'anaj',
            'description': 'Organic grains grown without synthetic pesticides or fertilizers.'
        },
        {
            'name': 'Organic Fruits',
            'category_type': 'organic',
            'sub_category': 'fruits',
            'description': 'Organic fruits grown without synthetic pesticides or fertilizers.'
        },
        {
            'name': 'Organic Vegetables',
            'category_type': 'organic',
            'sub_category': 'vegetables',
            'description': 'Organic vegetables grown without synthetic pesticides or fertilizers.'
        }
    ]
    
    created_categories = []
    for category_data in categories:
        category, created = Category.objects.get_or_create(
            name=category_data['name'],
            defaults={
                'category_type': category_data['category_type'],
                'sub_category': category_data['sub_category'],
                'description': category_data['description']
            }
        )
        created_categories.append(category)
        print(f"Category {'created' if created else 'already exists'}: {category.name}")
    
    return created_categories

# Create Products
def create_products(categories):
    products_data = [
        # Normal Anaj Products
        {
            'category': 'Normal Anaj',
            'name': 'Wheat (Gehu)',
            'description': 'Fresh wheat grains perfect for making rotis and chapatis.',
            'price': 40.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': True
        },
        {
            'category': 'Normal Anaj',
            'name': 'Rice (Chawal)',
            'description': 'Premium quality rice, perfect for daily meals.',
            'price': 60.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'category': 'Normal Anaj',
            'name': 'Bajra',
            'description': 'Nutritious bajra for making healthy rotis.',
            'price': 45.00,
            'stock': 80,
            'unit': 'kg',
            'is_featured': False
        },
        
        # Normal Fruits Products
        {
            'category': 'Normal Fruits',
            'name': 'Mango (Aam)',
            'description': 'Sweet and juicy mangoes from the farms of Maharashtra.',
            'price': 120.00,
            'stock': 50,
            'unit': 'kg',
            'is_featured': True
        },
        {
            'category': 'Normal Fruits',
            'name': 'Banana (Kela)',
            'description': 'Fresh and ripe bananas.',
            'price': 60.00,
            'stock': 100,
            'unit': 'dozen',
            'is_featured': False
        },
        
        # Normal Vegetables Products
        {
            'category': 'Normal Vegetables',
            'name': 'Potato (Aloo)',
            'description': 'Fresh potatoes from the farms of Punjab.',
            'price': 30.00,
            'stock': 150,
            'unit': 'kg',
            'is_featured': True
        },
        {
            'category': 'Normal Vegetables',
            'name': 'Tomato (Tamatar)',
            'description': 'Fresh and ripe tomatoes.',
            'price': 40.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': False
        },
        
        # Organic Anaj Products
        {
            'category': 'Organic Anaj',
            'name': 'Organic Wheat (Gehu)',
            'description': 'Organically grown wheat free from pesticides and chemicals.',
            'price': 80.00,
            'stock': 50,
            'unit': 'kg',
            'is_featured': True
        },
        {
            'category': 'Organic Anaj',
            'name': 'Organic Rice (Chawal)',
            'description': 'Organically grown rice, perfect for health-conscious consumers.',
            'price': 120.00,
            'stock': 50,
            'unit': 'kg',
            'is_featured': False
        },
        
        # Organic Fruits Products
        {
            'category': 'Organic Fruits',
            'name': 'Organic Mango (Aam)',
            'description': 'Organically grown sweet mangoes without any chemicals.',
            'price': 200.00,
            'stock': 30,
            'unit': 'kg',
            'is_featured': True
        },
        {
            'category': 'Organic Fruits',
            'name': 'Organic Banana (Kela)',
            'description': 'Organically grown bananas without any chemicals.',
            'price': 100.00,
            'stock': 50,
            'unit': 'dozen',
            'is_featured': False
        },
        
        # Organic Vegetables Products
        {
            'category': 'Organic Vegetables',
            'name': 'Organic Potato (Aloo)',
            'description': 'Organically grown potatoes without any chemicals.',
            'price': 60.00,
            'stock': 80,
            'unit': 'kg',
            'is_featured': True
        },
        {
            'category': 'Organic Vegetables',
            'name': 'Organic Tomato (Tamatar)',
            'description': 'Organically grown tomatoes without any chemicals.',
            'price': 80.00,
            'stock': 60,
            'unit': 'kg',
            'is_featured': False
        },
    ]
    
    created_products = []
    for product_data in products_data:
        category_name = product_data.pop('category')
        category = next((c for c in categories if c.name == category_name), None)
        
        if category:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'category': category,
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'stock': product_data['stock'],
                    'unit': product_data['unit'],
                    'is_featured': product_data['is_featured']
                }
            )
            created_products.append(product)
            print(f"Product {'created' if created else 'already exists'}: {product.name}")
    
    return created_products

# Create Farmers
def create_farmers(products):
    farmers_data = [
        {
            'name': 'Rajesh Kumar',
            'location': 'Punjab',
            'description': 'I have been farming for over 20 years, specializing in wheat and rice cultivation using traditional methods passed down through generations.',
            'products': ['Wheat (Gehu)', 'Rice (Chawal)']
        },
        {
            'name': 'Meena Devi',
            'location': 'Maharashtra',
            'description': 'I grow a variety of fruits in my family-owned orchard, focusing on sustainable farming practices.',
            'products': ['Mango (Aam)', 'Banana (Kela)']
        },
        {
            'name': 'Suresh Patel',
            'location': 'Gujarat',
            'description': 'I am a third-generation farmer specializing in organic farming. I believe in growing food that is good for people and the planet.',
            'products': ['Organic Wheat (Gehu)', 'Organic Rice (Chawal)']
        },
        {
            'name': 'Anita Singh',
            'location': 'Himachal Pradesh',
            'description': 'I grow vegetables in the hills of Himachal, where the climate offers perfect conditions for healthy, flavorful produce.',
            'products': ['Potato (Aloo)', 'Tomato (Tamatar)', 'Organic Potato (Aloo)', 'Organic Tomato (Tamatar)']
        }
    ]
    
    created_farmers = []
    for farmer_data in farmers_data:
        product_names = farmer_data.pop('products')
        farmer, created = Farmer.objects.get_or_create(
            name=farmer_data['name'],
            defaults={
                'location': farmer_data['location'],
                'description': farmer_data['description']
            }
        )
        
        # Add products to farmer
        for product_name in product_names:
            product = next((p for p in products if p.name == product_name), None)
            if product:
                farmer.products.add(product)
        
        created_farmers.append(farmer)
        print(f"Farmer {'created' if created else 'already exists'}: {farmer.name}")
    
    return created_farmers

if __name__ == '__main__':
    print("Creating sample data...")
    categories = create_categories()
    products = create_products(categories)
    farmers = create_farmers(products)
    print("Sample data creation completed!") 