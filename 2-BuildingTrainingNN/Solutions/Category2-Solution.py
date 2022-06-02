# ## Exercise 2
# In the course you learned how to do classificaiton using Fashion MNIST, a data set containing items of clothing. There's another, similar dataset called MNIST which has items of handwriting -- the digits 0 through 9.
#
# Write an MNIST classifier that trains to 99% accuracy or above, and does it without a fixed number of epochs -- i.e. you should stop training once you reach that level of accuracy.
#
# Some notes:
# 1. It should succeed in less than 10 epochs, so it is okay to change epochs= to 10, but nothing larger
# 2. When it reaches 99% or greater it should print out the string "Reached 99% accuracy so cancelling training!"
# 3. If you add any additional variables, make sure you use the same names as the ones used in the class
#
# I've started the code for you below -- how would you finish it?

import tensorflow as tf
import tensorflow_datasets as tfds


# from os import path, getcwd, chdir

# DO NOT CHANGE THE LINE BELOW. If you are developing in a local
# environment, then grab mnist.npz from the Coursera Jupyter Notebook
# and place it inside a local folder and edit the path to that location
# path = f"{getcwd()}/../tmp2/mnist.npz"

# GRADED FUNCTION: train_mnist

def train_mnist():
    # Please write your code only where you are indicated.
    # please do not remove # model fitting inline comments.

    # Create a class to build the required callback to stop training
    # YOUR CODE SHOULD START HERE
    class MyTrainer(tf.keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs={}):
            if(logs.get('accuracy')>0.99):
                print('¡Felicidades! Lograste el 99% de presición')
                self.model.stop_training = True

    # YOUR CODE SHOULD END HERE

    # Load MNIST dataset with TensorFlow Datasets (or with Keras,
    # it's your choice)
    # REMEMBER: You need to normalize your images to 0 to 1 scale

    # YOUR CODE SHOULD START HERE
    # Importamos los datos. Intentamos lograr ese 99% con fashion MNIST
    # ---- Forma con Keras ----
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

    x_train = x_train / 255.0
    x_test = x_test / 255.0

    # ---- Forma con TensorFlow Datasets ----
    # Más info en: https://www.tensorflow.org/datasets/keras_example
    """(ds_train, ds_test), ds_info = tfds.load('mnist',
                                             split=['train', 'test'],
                                             shuffle_files=True,
                                             as_supervised=True,
                                             with_info=True)

    # Build a training pipeline
    def normalize_img(image, label):
        # Normalizes images: `uint8` -> `float32`.
        return tf.cast(image, tf.float32) / 255., label

    ds_train = ds_train.map(
        normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
    ds_train = ds_train.cache()
    ds_train = ds_train.shuffle(ds_info.splits['train'].num_examples)
    ds_train = ds_train.batch(128)
    ds_train = ds_train.prefetch(tf.data.AUTOTUNE)

    # Build an evaluation pipeline
    ds_test = ds_test.map(
        normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
    ds_test = ds_test.batch(128)
    ds_test = ds_test.cache()
    ds_test = ds_test.prefetch(tf.data.AUTOTUNE)"""
    # YOUR CODE SHOULD END HERE

    # Create an instance of your callback
    # YOUR CODE SHOULD START HERE
    callbacks = MyTrainer()
    # YOUR CODE SHOULD END HERE

    model = tf.keras.models.Sequential([
        # YOUR CODE SHOULD START HERE
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
        # YOUR CODE SHOULD END HERE
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # model fitting
    history = model.fit(  # YOUR CODE SHOULD START HERE
        # ---- Forma con TensorFlow Datasets ----
        #ds_train,
        #validation_data=ds_test,
        # ---- Forma con Keras: ----
        x_train,
        y_train,
        validation_data=(x_test, y_test),
        epochs=10,
        callbacks=[callbacks]
        # YOUR CODE SHOULD END HERE
    )
    model.save("mymodel.h5")
    return history.epoch, history.history['accuracy'][-1]

if __name__ == '__main__':
    model = train_mnist()