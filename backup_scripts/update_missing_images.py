import os
import django
import shutil
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_fresh_india.settings')
django.setup()

from products.models import Product

def update_missing_images():
    print("Updating missing product images...")
    
    # Dictionary of products and their image paths (will be placed in product_images folder)
    products_to_update = {
        # Normal products
        'Pigeon Pea (Arhar / Toor Dal)': 'product_images/pigeon_pea.jpg',
        'Wheat (Gehu)': 'product_images/wheat.jpg',
        'Custard Apple (Sharifa / Sitaphal)': 'product_images/custard_apple.jpg',
        
        # Organic products
        'Organic Barley (Jau)': 'product_images/organic_barley.jpg',
        'Organic Corn (Makka)': 'product_images/organic_corn.jpg',
        'Organic Pigeon Pea (Arhar / Toor Dal)': 'product_images/organic_pigeon_pea.jpg',
        'Organic Custard Apple (Sharifa / Sitaphal)': 'product_images/organic_custard_apple.jpg',
    }
    
    # Create product_images directory if it doesn't exist
    if not os.path.exists('product_images'):
        os.makedirs('product_images')
    
    # Create placeholder images
    for product_name, image_path in products_to_update.items():
        # Check if the product exists
        try:
            product = Product.objects.get(name=product_name)
            
            # Create a basic placeholder image if it doesn't exist
            if not os.path.exists(image_path):
                print(f"Creating placeholder image for {product_name}...")
                
                # Just create a copy of an existing image for now (can be replaced later)
                sample_images = ['product_images/Apple (Seb).jpg', 'product_images/Carrot (Gajar).jpg']
                
                for sample in sample_images:
                    if os.path.exists(sample):
                        shutil.copy(sample, image_path)
                        print(f"Created placeholder image at {image_path}")
                        break
            
            # Set the image for the product
            if os.path.exists(image_path):
                with open(image_path, 'rb') as img_file:
                    # Get the filename from the path
                    filename = os.path.basename(image_path)
                    
                    # Save the image to the product
                    product.image.save(
                        filename,
                        File(img_file),
                        save=True
                    )
                    print(f"Added image to '{product_name}'")
            else:
                print(f"Warning: Image file not found for {product_name}")
                
        except Product.DoesNotExist:
            print(f"Product not found: {product_name}")
    
    # Set the specific image for Organic Banana (Kela)
    try:
        banana_product = Product.objects.get(name='Organic Banana (Kela)')
        banana_image = '/Users/krishna/Desktop/ppp/media/products/banana2.jpg'
        
        if os.path.exists(banana_image):
            with open(banana_image, 'rb') as img_file:
                filename = os.path.basename(banana_image)
                banana_product.image.save(
                    filename,
                    File(img_file),
                    save=True
                )
                print(f"Added image to 'Organic Banana (Kela)' from {banana_image}")
        else:
            print(f"Warning: Image file not found at {banana_image}")
            
    except Product.DoesNotExist:
        print("Product not found: Organic Banana (Kela)")
    
    print("Image update completed!")

if __name__ == '__main__':
    update_missing_images() 