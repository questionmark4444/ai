import csv
import ctypes
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import time

# Function to load and preprocess image from file using C library
def load_and_preprocess_image(file_path):
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (100, 100))
    image = image / 255.0
    image = np.expand_dims(image, axis=-1)
    image = np.expand_dims(image, axis=0)
    return image

def load_images_in_batches(image_folder, Class, batch_size):
  """Loads the images in a batch from the specified folder.

  Args:
    image_folder: The path to the folder containing the images.
    batch_size: The number of images to load in each batch.

  Returns:
    A NumPy array containing the images in the batch.
  """

  image_paths = os.listdir(image_folder)
  image_paths.sort()

  for i in range(batch_size):
    image_path = os.path.join(image_folder, image_paths[i])
    processed_image = load_and_preprocess_image(image_path)
    write_processed_data_to_disk(processed_image, f"temp/{Class}{i + 1}.csv")

def write_processed_data_to_disk(processed_data, output_file):
  """Writes the processed data to a CSV file.

  Args:
    processed_data: A NumPy array containing the processed data.
    output_file: The path to the CSV file to write the processed data to.
  """

  with open(output_file, "w") as f:
    writer = csv.writer(f)
    for row in processed_data:
      writer.writerow(row)

# Variable to record how long this will take to load C functions
RecordStart1 = time.time()

# Import C functions
c_file = "./my_functions.so"
rgb = ctypes.CDLL(c_file)

# Other variable to record how long this will take to load C functions
Recordend1 = time.time() - RecordStart1

# Input classes and number of images from the user
loop = True
while loop:
  #try:
    # Get the class folder names
    class1 = input("Enter the name of the first class folder: ")
    class2 = input("Enter the name of the second class folder: ")

    # Get the number of images in each class folder (smaller number)
    number_images = min(len(os.listdir("training_set/" + class1)), len(os.listdir("training_set/" + class2)))

    if number_images < 1:
      print(0/0)

    # Variable to record how long this will take to load and process images
    RecordStart2 = time.time()

    # process and save images from the class folders
    load_images_in_batches("training_set/" + class1, class1, number_images)
    load_images_in_batches("training_set/" + class2, class2, number_images)

    # Other variable to record how long this will take to load and process images
    Recordend2 = time.time() - RecordStart2
    minutes = int((Recordend1 + Recordend2) / 60 * 100) / 100
    print(f"the smaller number of images one folder is {number_images}")
    print(f"This took {minutes} minutes")  # Print the amount of minutes it took with 2 decimal places
    loop = False
  #except:
  #  print("Sorry, something went wrong.")
  #  print("Please make sure you provide valid folder names and that images are named correctly.\n")
