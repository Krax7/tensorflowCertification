import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Establecemos la cantidad de épocas
epochs = 10
# Establecemos el tamaño del batch
batch_size = 64

# Importamos los datos para entrenar el modelo con Tensorflow
(x_trainTF_, y_trainTF_), _ = tf.keras.datasets.mnist.load_data()
x_trainTF = x_trainTF_.reshape(60000, 784).astype('float32')/255
y_trainTF = tf.keras.utils.to_categorical(y_trainTF_, num_classes=10)

#
fig = plt.figure()