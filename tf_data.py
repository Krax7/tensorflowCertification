# Este ejercicio es sobre los fundamentos en el uso de tf.data, en particular, en la obtención de imágenes desde
# memoria o desde el disco
# Puedes encontrar el tutorial en su idioma original aquí: https://towardsdatascience.com/how-to-reduce-training-time-for-a-deep-learning-model-using-tf-data-43e1989d2961

## Ejemplo 1: tf.data para imágenes que son demasiado grandes como para caber en la RAM (las separararemos
# en batches)
# Dataset de frutas y verduras de Kaggle

import tensorflow as tf
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)
import numpy as np
import pandas as pd
import pathlib
import os
from os import getcwd
import pandas as pd
from glob import glob
import multiprocessing
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

train_dir=r'\dogs-vs-cats\train_data'
val_dir=r'\dogs-vs-cats\validation_data'

train_files = tf.data.Dataset.list_files(str(train_dir + '\\*\\*'), shuffle=False)
val_files = tf.data.Dataset.list_files(str(val_dir + '\\*\\*'), shuffle=False)
#getting the number of files in train and val dataset
train_num_files=len([file for file in glob(str(train_dir + '\\*\\*'))])
val_num_files=len([file for file in glob(str(val_dir + '\\*\\*'))])
print("No. of files in Train folder: ",train_num_files)
print("No. of files in Val folder: ",val_num_files)