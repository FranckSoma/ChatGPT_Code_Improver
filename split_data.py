import random
import os
import shutil

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


split_data(source_folder, train_folder, eval_folder, eval_ratio)
