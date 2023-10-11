#libraries
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import cv2
import csv
import ctypes


tf.config.set_visible_devices([], 'GPU')


# Import c functions
c_file = "./my_functions.so"
rgb = ctypes.CDLL(c_file)


#input classes
loop = True
while loop:    #in case couldnt find excel data
    try:    
        print("")  #new line
        number_of_images = int(input('what number of images of each class do you want to use: '))
        if (number_of_images < 1):  #restart loop with error
            print(0/0)
        print("")
        print("(this will look for a folder with the name of that class and png images with ascending number names)")
        class1 = input('what is the first class of image you want to classify: ')
        class2 = input('what is the second class of image you want to classify: ')

        # Load Excel data for training
        class1_data = [np.loadtxt(f'temp/{class1}{x+1}.csv', delimiter=',') for x in range(number_of_images)]
        class2_data = [np.loadtxt(f'temp/{class2}{x+1}.csv', delimiter=',') for x in range(number_of_images)]
        loop = False
    except:
        print("sorry, something went wrong, please try again")


# Function to load and preprocess image from file using C library
def load_and_preprocess_image(file_path):
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)  # Load as grayscale (black and white)

    image = cv2.resize(image, (100, 100))                #each pixel in the loaded image is a list of 3 values, 
                                                         #in grayscale the are made the same, 
                                                         #this will resize and replace the lists with the single values"""

    image = image / 255.0                                # make each value a decimal between 0 and 1 to make comparing easier
    image = np.expand_dims(image, axis=-1)               # Add a channel dimension
    image = np.expand_dims(image, axis=0)                # Add a batch dimension
    return image


# Load and preprocess the test image using C library
loop = True
while loop:  #in case couldnt find image
    test_image_path = input("\nWhere is the test image: ")
    try:
        test_image = load_and_preprocess_image(test_image_path)
        loop = False
    except:
        print("sorry, couldn't find the image")

# Define the CNN model for grayscale images
model = models.Sequential()

# Convolutional layer 1
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 1)))
model.add(layers.MaxPooling2D((2, 2)))

# Convolutional layer 2
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Convolutional layer 3
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

# Flatten the output
model.add(layers.Flatten())

# Dense layers
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(2, activation='softmax'))  # Two output classes: cat and dog as example

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Convert labels to NumPy array
train_labels = np.array([0] * len(class1_data) + [1] * len(class2_data))  # 0 for cat, 1 for dog as example

# Train the model with your cat and dog data
train_images = np.concatenate([class1_data, class2_data], axis=0)
model.fit(train_images, train_labels, epochs=10)

# Make predictions on the test image
predictions = model.predict(test_image)


# Classify the test image
if predictions[0][0] >= predictions[0][1]:
    print(class1)
if predictions[0][0] <= predictions[0][1]:
    print(class2)
if predictions[0][0] == predictions[0][1]:
    print('Error')
