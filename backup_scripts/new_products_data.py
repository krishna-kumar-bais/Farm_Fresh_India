import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_fresh_india.settings')
django.setup()

from products.models import Category, Product, Farmer

def add_new_products():
    # Get the categories
    normal_vegetables = Category.objects.get(name='Normal Vegetables')
    organic_vegetables = Category.objects.get(name='Organic Vegetables')
    normal_fruits = Category.objects.get(name='Normal Fruits')
    organic_fruits = Category.objects.get(name='Organic Fruits')
    normal_anaj = Category.objects.get(name='Normal Anaj')
    organic_anaj = Category.objects.get(name='Organic Anaj')
    
    # Define new vegetables
    vegetables_data = [
        {
            'name': 'Bottle gourd (Lauki)',
            'description': 'Fresh bottle gourd perfect for curries and stir-fries.',
            'price': 35.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Cucumber (Kakadi)',
            'description': 'Crisp and juicy cucumbers, perfect for salads.',
            'price': 40.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Carrot (Gajar)',
            'description': 'Fresh and crunchy carrots rich in vitamin A.',
            'price': 50.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Onion (Pyaaz)',
            'description': 'Fresh onions, a staple for Indian cooking.',
            'price': 30.00,
            'stock': 150,
            'unit': 'kg',
            'is_featured': True
        },
        {
            'name': 'Fenugreek (Methi)',
            'description': 'Fresh fenugreek leaves for making delicious curries and parathas.',
            'price': 25.00,
            'stock': 50,
            'unit': 'bundle',
            'is_featured': False
        },
        {
            'name': 'Beetroot (Chukander)',
            'description': 'Nutritious beetroots rich in iron and antioxidants.',
            'price': 45.00,
            'stock': 80,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Bitter gourd (Karela)',
            'description': 'Fresh bitter gourds known for their health benefits.',
            'price': 60.00,
            'stock': 70,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Pumpkin (Kaddu)',
            'description': 'Fresh pumpkin perfect for soups and curries.',
            'price': 30.00,
            'stock': 90,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Brinjal (Baingan)',
            'description': 'Fresh brinjal perfect for making bharta and curries.',
            'price': 40.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Ladies Fingers (Bhindi)',
            'description': 'Fresh okra perfect for making bhindi masala.',
            'price': 50.00,
            'stock': 80,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Cauliflower (Phool Gobi)',
            'description': 'Fresh cauliflower for making gobi dishes.',
            'price': 40.00,
            'stock': 90,
            'unit': 'piece',
            'is_featured': False
        },
        {
            'name': 'Cabbage (Patta Gobi)',
            'description': 'Fresh and crisp cabbage for salads and sabzis.',
            'price': 35.00,
            'stock': 90,
            'unit': 'piece',
            'is_featured': False
        },
        {
            'name': 'Capsicum (Shimla Mirch)',
            'description': 'Fresh bell peppers for adding color and flavor to dishes.',
            'price': 60.00,
            'stock': 80,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Peas (Mutter)',
            'description': 'Fresh green peas for curries and pulao.',
            'price': 70.00,
            'stock': 70,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Taro Root (Arbi)',
            'description': 'Fresh taro roots for making delicious side dishes.',
            'price': 50.00,
            'stock': 60,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Raw Bananas (Kachhe Kele)',
            'description': 'Fresh raw bananas for making curries and sabzis.',
            'price': 40.00,
            'stock': 70,
            'unit': 'kg',
            'is_featured': False
        },
    ]
    
    # Define new fruits
    fruits_data = [
        {
            'name': 'Apple (Seb)',
            'description': 'Fresh and juicy apples rich in fiber and vitamins.',
            'price': 120.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': True
        },
        {
            'name': 'Guava (Amrood)',
            'description': 'Fresh guavas rich in vitamin C and fiber.',
            'price': 80.00,
            'stock': 80,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Papaya (Papita)',
            'description': 'Fresh papayas good for digestion and skin health.',
            'price': 60.00,
            'stock': 70,
            'unit': 'piece',
            'is_featured': False
        },
        {
            'name': 'Pomegranate (Anar)',
            'description': 'Fresh pomegranates rich in antioxidants.',
            'price': 150.00,
            'stock': 60,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Watermelon (Tarbooz)',
            'description': 'Sweet and juicy watermelons, perfect for summer.',
            'price': 40.00,
            'stock': 50,
            'unit': 'piece',
            'is_featured': False
        },
        {
            'name': 'Muskmelon (Kharbooja)',
            'description': 'Sweet and aromatic muskmelons rich in vitamins.',
            'price': 60.00,
            'stock': 50,
            'unit': 'piece',
            'is_featured': False
        },
        {
            'name': 'Pineapple (Ananas)',
            'description': 'Sweet and tangy pineapples rich in vitamin C.',
            'price': 80.00,
            'stock': 40,
            'unit': 'piece',
            'is_featured': False
        },
        {
            'name': 'Orange (Santra)',
            'description': 'Juicy oranges packed with vitamin C.',
            'price': 100.00,
            'stock': 80,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Grapes (Angoor)',
            'description': 'Sweet and juicy grapes, perfect for snacking.',
            'price': 120.00,
            'stock': 70,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Custard Apple (Sharifa / Sitaphal)',
            'description': 'Sweet and creamy custard apples rich in nutrients.',
            'price': 160.00,
            'stock': 50,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Jamun (Jamun)',
            'description': 'Fresh jamun known for its antidiabetic properties.',
            'price': 140.00,
            'stock': 40,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Ber (Indian Jujube)',
            'description': 'Sweet and tangy ber rich in vitamin C.',
            'price': 100.00,
            'stock': 60,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Sapodilla (Chikoo)',
            'description': 'Sweet and malty sapodillas rich in fiber.',
            'price': 120.00,
            'stock': 60,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Tamarind (Imli)',
            'description': 'Tangy tamarind used in various Indian dishes.',
            'price': 80.00,
            'stock': 50,
            'unit': 'kg',
            'is_featured': False
        },
    ]
    
    # Define new grains
    grains_data = [
        {
            'name': 'Barley (Jau)',
            'description': 'Nutritious barley grains rich in fiber.',
            'price': 60.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Corn (Makka)',
            'description': 'Fresh corn kernels for making various dishes.',
            'price': 50.00,
            'stock': 90,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Pigeon Pea (Arhar / Toor Dal)',
            'description': 'High-quality pigeon peas for making dal.',
            'price': 120.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Red Lentil (Masoor Dal)',
            'description': 'Nutritious red lentils for making soups and dal.',
            'price': 110.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Green Gram (Moong Dal)',
            'description': 'Protein-rich green gram for making dal and sprouts.',
            'price': 130.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Black Gram (Urad Dal)',
            'description': 'Nutritious black gram for making dal and dosa batter.',
            'price': 140.00,
            'stock': 90,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Chickpeas (Chana)',
            'description': 'Protein-rich chickpeas for various dishes.',
            'price': 100.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Kidney Beans (Rajma)',
            'description': 'Nutritious kidney beans for making rajma curry.',
            'price': 120.00,
            'stock': 100,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Mustard Seeds (Sarson)',
            'description': 'Aromatic mustard seeds for tempering.',
            'price': 80.00,
            'stock': 70,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Sesame Seeds (Til)',
            'description': 'Nutritious sesame seeds rich in calcium.',
            'price': 130.00,
            'stock': 60,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Flax Seeds (Alsi)',
            'description': 'Omega-3 rich flax seeds for health benefits.',
            'price': 150.00,
            'stock': 60,
            'unit': 'kg',
            'is_featured': False
        },
        {
            'name': 'Soya Bean (Soyabean)',
            'description': 'Protein-rich soya beans for various dishes.',
            'price': 90.00,
            'stock': 80,
            'unit': 'kg',
            'is_featured': False
        },
    ]
    
    # Add normal vegetables
    for veg in vegetables_data:
        # Normal version
        Product.objects.get_or_create(
            name=veg['name'],
            category=normal_vegetables,
            defaults={
                'description': veg['description'],
                'price': veg['price'],
                'stock': veg['stock'],
                'unit': veg['unit'],
                'is_featured': veg['is_featured'],
            }
        )
        
        # Organic version (20% price increase)
        Product.objects.get_or_create(
            name=f"Organic {veg['name']}",
            category=organic_vegetables,
            defaults={
                'description': f"Organically grown {veg['name'].lower()} without any chemicals.",
                'price': veg['price'] * 1.8,  # Organic products are typically more expensive
                'stock': int(veg['stock'] * 0.6),  # Less stock for organic products
                'unit': veg['unit'],
                'is_featured': False,
            }
        )
    
    # Add normal fruits
    for fruit in fruits_data:
        # Normal version
        Product.objects.get_or_create(
            name=fruit['name'],
            category=normal_fruits,
            defaults={
                'description': fruit['description'],
                'price': fruit['price'],
                'stock': fruit['stock'],
                'unit': fruit['unit'],
                'is_featured': fruit['is_featured'],
            }
        )
        
        # Organic version (80% price increase)
        Product.objects.get_or_create(
            name=f"Organic {fruit['name']}",
            category=organic_fruits,
            defaults={
                'description': f"Organically grown {fruit['name'].lower()} without any chemicals.",
                'price': fruit['price'] * 1.8,  # Organic products are typically more expensive
                'stock': int(fruit['stock'] * 0.6),  # Less stock for organic products
                'unit': fruit['unit'],
                'is_featured': False,
            }
        )
    
    # Add normal grains
    for grain in grains_data:
        # Normal version
        Product.objects.get_or_create(
            name=grain['name'],
            category=normal_anaj,
            defaults={
                'description': grain['description'],
                'price': grain['price'],
                'stock': grain['stock'],
                'unit': grain['unit'],
                'is_featured': grain['is_featured'],
            }
        )
        
        # Organic version (80% price increase)
        Product.objects.get_or_create(
            name=f"Organic {grain['name']}",
            category=organic_anaj,
            defaults={
                'description': f"Organically grown {grain['name'].lower()} without any chemicals.",
                'price': grain['price'] * 1.8,  # Organic products are typically more expensive
                'stock': int(grain['stock'] * 0.6),  # Less stock for organic products
                'unit': grain['unit'],
                'is_featured': False,
            }
        )

if __name__ == '__main__':
    print("Adding new products...")
    add_new_products()
    print("Products added successfully!") 