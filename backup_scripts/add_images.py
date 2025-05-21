import os
import django
import glob
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'farm_fresh_india.settings')
django.setup()

from products.models import Product

def add_images_to_products():
    """
    This script allows you to add images to products by following a naming convention.
    
    Instructions:
    1. Create a folder named 'product_images' in your project root
    2. Add images with filenames that match the product name, e.g:
       - 'Potato (Aloo).jpg' for the product "Potato (Aloo)"
       - 'Organic Apple (Seb).png' for the product "Organic Apple (Seb)"
    3. Run this script
    
    The script will search for matching images and add them to the products.
    """
    print("Starting to add images to products...")
    
    # Directory containing product images
    image_dir = 'product_images'
    
    # Create directory if it doesn't exist
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)
        print(f"Created '{image_dir}' directory. Please add your product images to this folder.")
        print("Image filenames should match product names, e.g., 'Potato (Aloo).jpg'")
        return
    
    # Get all products
    products = Product.objects.all()
    print(f"Found {products.count()} products in the database")
    
    # Get all image files in the image directory
    image_files = []
    for ext in ['jpg', 'jpeg', 'png', 'gif', 'webp']:
        image_files.extend(glob.glob(f"{image_dir}/*.{ext}"))
    
    print(f"Found {len(image_files)} images in the {image_dir} directory")
    
    # Counter for tracking successful image assignments
    assigned_count = 0
    
    # For each product, try to find a matching image
    for product in products:
        # Clean the product name for filename matching
        product_name = product.name
        
        # Try to find a matching image
        for image_path in image_files:
            image_filename = os.path.basename(image_path)
            image_name = os.path.splitext(image_filename)[0]
            
            # If the image name matches the product name
            if image_name.lower() == product_name.lower():
                print(f"Found matching image for '{product_name}'")
                
                # Open the image file
                with open(image_path, 'rb') as img_file:
                    # Save the image to the product
                    product.image.save(
                        image_filename,
                        File(img_file),
                        save=True
                    )
                    assigned_count += 1
                    print(f"Added image to '{product_name}'")
                    break
    
    print(f"Completed! Added images to {assigned_count} products.")
    print(f"Products still missing images: {products.count() - assigned_count}")

if __name__ == '__main__':
    add_images_to_products() 