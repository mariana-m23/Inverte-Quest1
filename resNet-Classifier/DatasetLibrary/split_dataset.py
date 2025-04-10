import os
import shutil
import random

# Set paths
source_dir = 'all_invertebrates'     # Folder with all your images organized by class
output_dir = '.'               # Current directory
train_ratio = 0.8              # 80% training, 20% validation

# Create train/ and val/ folders
for split in ['train', 'val']:
    split_path = os.path.join(output_dir, split)
    os.makedirs(split_path, exist_ok=True)

    # Create class subfolders
    for class_name in os.listdir(source_dir):
        class_path = os.path.join(split_path, class_name)
        os.makedirs(class_path, exist_ok=True)

# Loop through each class
for class_name in os.listdir(source_dir):
    class_folder = os.path.join(source_dir, class_name)
    images = os.listdir(class_folder)
    random.shuffle(images)

    # Calculate split
    train_size = int(len(images) * train_ratio)
    train_images = images[:train_size]
    val_images = images[train_size:]

    # Move files to train/
    for img in train_images:
        src = os.path.join(class_folder, img)
        dst = os.path.join(output_dir, 'train', class_name, img)
        shutil.copy2(src, dst)

    # Move files to val/
    for img in val_images:
        src = os.path.join(class_folder, img)
        dst = os.path.join(output_dir, 'val', class_name, img)
        shutil.copy2(src, dst)

print("✅ Dataset successfully split into train/ and val/ folders.")
