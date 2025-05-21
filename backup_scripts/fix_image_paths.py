import os
import django
import glob
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_fresh_india.settings')
django.setup()

from products.models import Product

def fix_product_images():
    print("Fixing product images with correct file paths...")
    
    # Products that need fixing
    products_to_fix = [
        'Organic Barley (Jau)',
        'Organic Corn (Makka)',
        'Organic Pigeon Pea (Arhar / Toor Dal)',
        'Organic Custard Apple (Sharifa / Sitaphal)',
        'Mustard Seeds (Sarson)',
        'Pigeon Pea (Arhar / Toor Dal)',
        'Wheat (Gehu)',
        'Custard Apple (Sharifa / Sitaphal)',
    ]
    
    # Get all image files in the product_images directory
    image_files = []
    for ext in ['jpg', 'jpeg', 'png', 'gif']:
        image_files.extend(glob.glob(f"product_images/*.{ext}"))
    
    print(f"Found {len(image_files)} image files in product_images directory")
    
    # For each product that needs fixing
    for product_name in products_to_fix:
        try:
            # Get the product
            product = Product.objects.get(name=product_name)
            
            # Normalize the product name for comparison
            # For "Pigeon Pea (Arhar / Toor Dal)" we want to find "Pigeon Pea (Arhar : Toor Dal)"
            normalized_name = product_name.replace('/', ':').replace('  ', ' ')
            
            # Find matching image
            found_image = None
            for image_path in image_files:
                # Extract just the filename without extension
                image_filename = os.path.basename(image_path)
                name_part = os.path.splitext(image_filename)[0]
                
                # Handle the special case of ".jpg .jpeg" in filename
                if ".jpg .jpeg" in image_filename:
                    name_part = image_filename.split(".jpg")[0]
                
                # If the normalized name matches the file name
                if normalized_name.lower() == name_part.lower():
                    found_image = image_path
                    break
            
            # If we found an image
            if found_image:
                print(f"Found matching image for '{product_name}': {found_image}")
                
                # Open and set the image
                with open(found_image, 'rb') as img_file:
                    # Get clean filename
                    clean_filename = os.path.basename(found_image).split(".jpg")[0] + ".jpg"
                    
                    # Save the image to the product
                    product.image.save(
                        clean_filename,
                        File(img_file),
                        save=True
                    )
                    print(f"Fixed image for '{product_name}'")
            else:
                print(f"Error: No matching image found for '{product_name}'")
                
        except Product.DoesNotExist:
            print(f"Error: Product not found: {product_name}")
    
    print("Image path correction completed!")

if __name__ == '__main__':
    fix_product_images() 