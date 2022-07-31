# -*- coding: utf-8 -*-
"""Nexus_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vBSgPJ9J6W1SYC7__ikQbYXRj0wigjaw
"""

from google.colab import drive
drive.mount('/content/drive')

import matplotlib.pyplot as plt
import numpy as np
import os
import pathlib
import PIL # Pillow untuk pemrosesan gambar

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from PIL import Image, ImageDraw
from IPython.display import display
from google.colab.patches import cv2_imshow
import cv2
from datetime import datetime

"""# Data Exploration"""

dataset_path ="/content/drive/MyDrive/NexusProject/dataset"
data = {"Afifah","Agnes","Arridha","Arya","Azizah","Dwi","Dymend","Erel","Mr Nawawi","Pak Iyan","Pak John","Pak Nugraha","Pak Sopiyan",}

train_Afifah_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Train/Afifah')
train_Agnes_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Train/Agnes')
train_Arridha_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Train/Arridha')
train_Arya_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Train/Arya')
train_Azizah_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Train/Azizah')
train_Dwi_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Train/Dwi')
train_Dymend_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Train/Dymend')
train_Erel_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Train/Erel')
train_Nawawi_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Train/Pak Nawawi')
train_John_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Train/Pak John')
train_Nugraha_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Train/Pak Nugrah')
train_Sopiyan_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Train/Pak Sopiyan')
train_Iyan_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Train/Pak Iyan')

test_Afifah_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Test/Afifah')
test_Agnes_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Test/Agnes')
test_Arridha_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Test/Arridha')
test_Arya_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Test/Arya')
test_Azizah_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Test/Azizah')
test_Dwi_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Test/Dwi')
test_Dymend_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Test/Dymend')
test_Erel_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Test/Erel')
test_Nawawi_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Test/Pak Nawawi')
test_John_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Test/Pak John')
test_Nugraha_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Test/Pak Nugrah')
test_Sopiyan_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Test/Pak Sopiyan')
test_Iyan_dir = os.path.join('/content/drive/MyDrive/NexusProject/dataset/Test/Pak Iyan')

train_Afifah_names = os.listdir(train_Afifah_dir)
train_Agnes_names = os.listdir(train_Agnes_dir)
train_Arridha_names = os.listdir(train_Arridha_dir)
train_Arya_names = os.listdir(train_Arya_dir)
train_Azizah_names = os.listdir(train_Azizah_dir)
train_Dwi_names = os.listdir(train_Dwi_dir)
train_Dymend_names = os.listdir(train_Dymend_dir)
train_Erel_names = os.listdir(train_Erel_dir)
train_Nawawi_names = os.listdir(train_Nawawi_dir)
train_Iyan_names = os.listdir(train_Iyan_dir)
train_John_names = os.listdir(train_John_dir)
train_Nugraha_names = os.listdir(train_Nugraha_dir)
train_Sopiyan_names = os.listdir(train_Sopiyan_dir)
print(train_Afifah_names[:10])
print(train_Agnes_names[:10])
print(train_Arridha_names[:10])
print(train_Arya_names[:10])
print(train_Azizah_names[:10])
print(train_Dwi_names[:10])
print(train_Dymend_names[:10])
print(train_Erel_names[:10])
print(train_Nawawi_names[:10])
print(train_Iyan_names[:10])
print(train_John_names[:10])
print(train_Nugraha_names[:10])
print(train_Sopiyan_names[:10])

test_Afifah_names = os.listdir(test_Afifah_dir)
test_Agnes_names = os.listdir(test_Agnes_dir)
test_Arridha_names = os.listdir(test_Arridha_dir)
test_Arya_names = os.listdir(test_Arya_dir)
test_Azizah_names = os.listdir(test_Azizah_dir)
test_Dwi_names = os.listdir(test_Dwi_dir)
test_Dymend_names = os.listdir(test_Dymend_dir)
test_Erel_names = os.listdir(test_Erel_dir)
test_Nawawi_names = os.listdir(test_Nawawi_dir)
test_Iyan_names = os.listdir(test_Iyan_dir)
test_John_names = os.listdir(test_John_dir)
test_Nugraha_names = os.listdir(test_Nugraha_dir)
test_Sopiyan_names = os.listdir(test_Sopiyan_dir)
print(test_Afifah_names[:10])
print(test_Agnes_names[:10])
print(test_Arridha_names[:10])
print(test_Arya_names[:10])
print(test_Azizah_names[:10])
print(test_Dwi_names[:10])
print(test_Dymend_names[:10])
print(test_Erel_names[:10])
print(test_Nawawi_names[:10])
print(test_Iyan_names[:10])
print(test_John_names[:10])
print(test_Nugraha_names[:10])
print(test_Sopiyan_names[:10])

print('total training Afifah images:', len(os.listdir(train_Afifah_dir)))
print('total training Agnes images:', len(os.listdir(train_Agnes_dir)))
print('total training Arridha images:', len(os.listdir(train_Arridha_dir)))
print('total training Arya images:', len(os.listdir(train_Arya_dir)))
print('total training Azizah images:', len(os.listdir(train_Azizah_dir)))
print('total training Dwi images:', len(os.listdir(train_Dwi_dir)))
print('total training Dymend images:', len(os.listdir(train_Dymend_dir)))
print('total training Erel images:', len(os.listdir(train_Erel_dir)))
print('total training Mr  Nawawi images:', len(os.listdir(train_Nawawi_dir)))
print('total training Pak Iyan images:', len(os.listdir(train_Iyan_dir)))
print('total training Pak John images:', len(os.listdir(train_John_dir)))
print('total training Pak Nugraha images:', len(os.listdir(train_Nugraha_dir)))
print('total training Pak Sopiyan images:', len(os.listdir(train_Sopiyan_dir)))
print()
print('total validation Afifah images:', len(os.listdir(test_Afifah_dir)))
print('total validation Agnes images:', len(os.listdir(test_Agnes_dir)))
print('total validation Arridha images:', len(os.listdir(test_Arridha_dir)))
print('total validation Arya images:', len(os.listdir(test_Arya_dir)))
print('total validation Azizah images:', len(os.listdir(test_Azizah_dir)))
print('total validation Dwi images:', len(os.listdir(test_Dwi_dir)))
print('total validation Dymend images:', len(os.listdir(test_Dymend_dir)))
print('total validation Erel images:', len(os.listdir(test_Erel_dir)))
print('total validation Pak Nawawi images:', len(os.listdir(test_Nawawi_dir)))
print('total validation Pak Iyan images:', len(os.listdir(test_Iyan_dir)))
print('total validation Pak John images:', len(os.listdir(test_John_dir)))
print('total validation Pak Nugraha images:', len(os.listdir(test_Nugraha_dir)))
print('total validation Pak Sopiyan images:', len(os.listdir(test_Sopiyan_dir)))

"""# Data Preprocessing"""

from tensorflow.keras.preprocessing.image import ImageDataGenerator #data ugmentasi

# All images will be rescaled by 1./255
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2, #
        zoom_range=0.2, #untuk zoom 
        horizontal_flip=True,
        validation_split=0.2)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        '/content/drive/MyDrive/NexusProject/dataset/Train',
        classes=["Afifah","Agnes","Arridha","Arya","Azizah","Dwi","Dymend","Erel","Mr Nawawi","Pak Iyan","Pak John","Pak Nugraha","Pak Sopiyan"],
        target_size=(200, 200),
        class_mode='categorical') 

validation_generator = test_datagen.flow_from_directory(
        '/content/drive/MyDrive/NexusProject/dataset/Test',
        classes=["Afifah","Agnes","Arridha","Arya","Azizah","Dwi","Dymend","Erel","Mr Nawawi","Pak Iyan","Pak John","Pak Nugraha","Pak Sopiyan"],
        target_size=(200, 200),
        class_mode='categorical')

# Tampilkan training images class #endconding
print(train_generator.num_classes) #awalan 0 karena kode biner
print(train_generator.class_indices)
print(train_generator.classes)

# Tampilkan validation images class
print(validation_generator.num_classes)
print(validation_generator.class_indices)
print(validation_generator.classes)

"""# Modeling: CNN"""

model = tf.keras.models.Sequential([
# Layer Konvolusi Pertama
tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(200, 200, 3)),
tf.keras.layers.MaxPooling2D(2, 2),
tf.keras.layers.Dropout(0.25),
# Layer Konvolusi Kedua
tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
tf.keras.layers.MaxPooling2D(2, 2),
tf.keras.layers.Dropout(0.25),

# Layer Konvolusi Ketiga
tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
tf.keras.layers.MaxPooling2D(2, 2),
tf.keras.layers.Dropout(0.25),

# Layer Konvolusi Keempat
tf.keras.layers.Conv2D(128, (3,3), activation='relu'),
tf.keras.layers.MaxPooling2D(2, 2),
tf.keras.layers.Dropout(0.25),

# Layer Konvolusi Kelima
tf.keras.layers.Conv2D(256, (3,3), activation='relu'),
tf.keras.layers.MaxPooling2D(2, 2),
tf.keras.layers.Dropout(0.25),

# Lakukan Flatten
tf.keras.layers.Flatten(),

# Lakukan fully connected layer
tf.keras.layers.Dense(512, activation='relu'),
tf.keras.layers.Dropout(0.5),
tf.keras.layers.Dense(13, activation='softmax') # jumlah dense sesuai dengan jumlah class
])

"""# Modeling: VGG"""

model.summary()

import tensorflow as tf
from tensorflow.keras.models import Sequential

# Layer NN
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization

# Layer khusus CNN
from tensorflow.keras.layers import Flatten, Conv2D, MaxPool2D

# Pretrained Model
from tensorflow.keras.layers import Input
from tensorflow.keras.applications.vgg16 import VGG16

model = Sequential([
  # Pretrained Model
  VGG16(weights='imagenet', include_top=False,  input_tensor=Input(shape=(200, 200,3))), # pre-trained model (sejatinya butuh image ukuran 224*224)
  
  Flatten(),

  # Fully-Connected layer
  Dense(512, activation='relu'),
  BatchNormalization(),
  Dropout(0.5),
  
  Dense(13, activation='softmax') # 3 class
])

model.layers[0].trainable = False; # layer VGG tidak di-training ulang

"""# Training Model"""

model.compile(optimizer = tf.optimizers.Adam(),
              loss = 'categorical_crossentropy',
              metrics=['accuracy']) #1

hist = model.fit(train_generator,
                 epochs=20,
                 validation_data=validation_generator)

model.save("/content/drive/MyDrive/NexusProject/face_recegnition_Ve2.h5")

"""# Evaluasi Model"""

score = model.evaluate(train_generator)

print('Loss: {:.4f}'.format(score[0]))
print('Accuracy: {:.4f}'.format(score[1]))

score = model.evaluate(validation_generator)

print('loss: {:.4f}'.format(score[0]))
print('Accuracy: {:.4f}'.format(score[1]))

"""# Plot Kurva Data Train dan Validasi"""

acc = hist.history['accuracy']
val_acc = hist.history['val_accuracy']

loss = hist.history['loss']
val_loss = hist.history['val_loss']

epochs_range = range(20)

plt.figure(figsize=(14, 5))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

"""# Confusion Matrix"""

from sklearn.metrics import classification_report, confusion_matrix
import sklearn.metrics

Y_pred = model.predict(validation_generator, validation_generator.num_classes // 32+1)
y_pred = np.argmax(Y_pred, axis=1)

print('Confusion Matrix')
print(confusion_matrix(validation_generator.classes, y_pred))
confusion_array = sklearn.metrics.confusion_matrix(validation_generator.classes, y_pred)

print('True Negative = ', confusion_array[0,0])
print('False Negative = ', confusion_array[1,0])
print('True Positive = ', confusion_array[1,1])
print('False Positive = ', confusion_array[0,1])

"""# Prediksi Model Data dengan Upload Gambar"""

# Commented out IPython magic to ensure Python compatibility.
from google.colab import files
from keras.preprocessing import image
# %matplotlib inline
 
uploaded = files.upload()
 
for fn in uploaded.keys():
 
  # prediksi data gambar
  path = fn
  img = image.load_img(path, target_size=(200,200))
  imgplot = plt.imshow(img)
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
 
  images = np.vstack([x])
  classes = model.predict(images, batch_size=32)
  
  print(fn)
  if classes[0,0] == 1.0:
    print('Afifah')
  elif classes[0,1] == 1.0:
    print('Agnes')
  elif classes[0,2] == 1.0:
    print('Arridha')
  elif classes[0,3] == 1.0:
    print('Arya')
  elif classes[0,4] == 1.0:
    print('Azizah')
  elif classes[0,5] == 1.0:
    print('Dwi')
  elif classes[0,6] == 1.0:
    print('Dymend')
  elif classes[0,7] == 1.0:
    print('Erel')
  elif classes[0,8] == 1.0:
    print('Pak Iyan')
  elif classes[0,9] == 1.0:
    print('Pak Nawawi')
  elif classes[0,10] == 1.0:
    print('Pak John')
  elif classes[0,11] == 1.0:
    print('Pak Nugraha')
  else:
    print('Pak Sopiyan')