from PIL import Image
import os
import shutil
import random

def crop_images_to_square(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for filename in os.listdir(source_dir):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img_path = os.path.join(source_dir, filename)
            img = Image.open(img_path)

            # Assuming the image is 480x640 (width x height)
            width, height = img.size
            new_height = width  # The target height is equal to the current width for a square

            # Calculate the top and bottom coordinates for cropping
            crop_height = height - new_height
            top = crop_height / 2
            bottom = height - crop_height / 2

            # The left and right coordinates remain the same as we are cropping vertically
            left = 0
            right = width

            img_cropped = img.crop((left, top, right, bottom))
            save_path = os.path.join(target_dir, filename)
            img_cropped.save(save_path)

def resize_images(source_dir, target_dir, size=(256, 256)):
    """Resize images in source_dir and save them to target_dir with the specified size."""
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    for filename in os.listdir(source_dir):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img_path = os.path.join(source_dir, filename)
            img = Image.open(img_path)
            img_resized = img.resize(size, Image.LANCZOS)

            save_path = os.path.join(target_dir, filename)
            img_resized.save(save_path)



def split_data(source_folder, train_folder, eval_folder, eval_ratio):
    """Split data into training and evaluation sets."""
    if not os.path.exists(train_folder):
        os.makedirs(train_folder)
    if not os.path.exists(eval_folder):
        os.makedirs(eval_folder)

    images = [img for img in os.listdir(source_folder) if img.endswith('.png') or img.endswith('.jpg')]
    random.shuffle(images)
    
    eval_size = int(len(images) * eval_ratio)

    for img in images[:eval_size]:
        shutil.move(os.path.join(source_folder, img), os.path.join(eval_folder, img))

    for img in images[eval_size:]:
        shutil.move(os.path.join(source_folder, img), os.path.join(train_folder, img))

# Adjust these paths and values
source_folder = 'FFHQ/Images'  # Path to your dataset
train_folder = 'FFHQ/Train'    # Path to the training set folder
eval_folder = 'FFHQ/Eval'      # Path to the evaluation set folder
eval_ratio = 0.2               # Percentage of data to be used for evaluation




# Replace with the actual paths
crop_images_to_square('Images', 'Crop')
resize_images('Crop', 'FFHQ/Images')

folder_path = 'Crop'  # Path to the folder you want to delete

# Check if the folder exists
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    shutil.rmtree(folder_path)
    print(f"Folder '{folder_path}' has been deleted.")
else:
    print(f"Folder '{folder_path}' does not exist.")

split_data(source_folder, train_folder, eval_folder, eval_ratio)