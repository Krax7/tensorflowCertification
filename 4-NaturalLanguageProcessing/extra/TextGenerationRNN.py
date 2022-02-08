import tensorflow as tf
print(tf.test.gpu_device_name())
print(tf.config.list_physical_devices('GPU'))
import numpy as np
import os
import time

def read_describe_file():
    # path_to_file devuelve C:\Users\omard\.keras\datasets\shakespeare.txt
    path_to_file = tf.keras.utils.get_file('shakespeare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
    # Leer y decodificar para py2 compat
    text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
    print(f'Logitud del texto: {len(text)} caracteres')
    # Veamos los primeros 250 caracteres en el texto
    print(text[:250])
    # Obtener los caracteres únicos en el archivo
    vocab = sorted(set(text)) # sorted retorna una lista de los elementos de un iterable en orden ascendente por
                              # defecto. Se le puede pasar una función custom y tiene una bandera reverse=False
    print(f'{len(vocab)} caracteres únicos')
    return vocab

def process_text(vocab):
    """
    Convierte texto a una representación numérica.

    La capa tf.keras.layers.StringLookup convierte cada caracter en un ID numérico. Solo necesita que el texto sea
    dividido en tokens primero.
    :return:
    """
    # example_texts = ['abcdefg', 'xyz']
    chars = tf.strings.unicode_split(example_texts, input_encoding='UTF-8')
    # print('Ejemplo de segmentación de caracteres: ', chars)

    # Creamos la capa tf.keras.layers.StringLookup
    ids_from_chars = tf.keras.layers.StringLookup(
        vocabulary=list(vocab),
        mask_token=None
    )

    # Convertimos de tokens a IDs de caracteres
    ids = ids_from_chars(chars)

    """
    Dado que el objetivo de este tutorial es generar texto, también será importante invertir esta representación y
    recuperar cadenas legibles por humanos a partir de ella. Para esto, puede usar: tf.keras.layers.StringLookup(..., invert=True)
    """
    chars_from_ids = tf.keras.layers.StringLookup(
        vocabulary=ids_from_chars.get_vocabulary(),
        invert=True, mask_token=None
    )

    # Esta capa recupera los caracteres de vectores de IDs, y los retorna como tf.RaggedTensor de caracteres
    chars = chars_from_ids(ids)
    print(chars)
    return chars

def text_from_ids(chars):
    # Puedes usar tf.strings.reduce_join para unir los caracteres y devolverlos a su forma de cadena
    tf.strings.reduce_join(chars, axis=-1).numpy()

def process_text_split():
    # path_to_file devuelve C:\Users\omard\.keras\datasets\shakespeare.txt
    path_to_file = tf.keras.utils.get_file('shakespeare.txt',
                                           'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
    # Leer y decodificar para py2 compat
    text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
    print(f'Logitud del texto: {len(text)} caracteres')
    # Veamos los primeros 250 caracteres en el texto
    print(text[:250])

    ids_from_chars = tf.keras.layers.StringLookup(
        vocabulary=list(vocab),
        mask_token=None
    )

    chars_from_ids = tf.keras.layers.StringLookup(
        vocabulary=ids_from_chars.get_vocabulary(),
        invert=True, mask_token=None
    )

    all_ids = ids_from_chars(tf.strings.unicode_split(text, 'UTF-8'))
    print(all_ids)

    ids_dataset = tf.data.Dataset.from_tensor_slices(all_ids)

    for ids in ids_dataset.take(10):
        print(chars_from_ids(ids).numpy().decode('utf-8'))

    """
    Break the text into chunks of seq_length+1. For example, say seq_length is 4 and our text is "Hello".
    The input sequence would be "Hell", and the target sequence "ello".
    """
    seq_length = 100
    examples_per_epoch = len(text) // (seq_length+1)

    # El método de batch permite convertir fácilmente de caracteres individuales a secuencias de un tamaño
    # determinado.
    sequences = ids_dataset.batch(seq_length+1, drop_remainder=True)

    for seq in sequences.take(1)

vocab = read_describe_file()
chars = process_text(vocab)
text_from_ids(chars)

