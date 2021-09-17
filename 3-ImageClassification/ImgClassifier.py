# Imports components from Keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Inicializando un modelo secuencial
model = Sequential()

# Primera capa
"""
La forma de la entrada (input_shape) es un arreglo unidimensional de 784 posiciones
Cada valor es un píxel cuya intensidad oscila entre el 0 y el 255
Sería más o menos así: [[0.], [16.], [255.], [128.], ..., [254.]]
A pesar de no estar en dos dimensiones, el conjunto de valores para los píxeles podría decirse
que es único para cada imagen
"""
model.add(Dense(10, activation='relu', input_shape=(784,)))

# Segunda capa
model.add(Dense(10, activation='relu'))

# Capa de salida
model.add(Dense(3, activation='softmax'))

# Compilando el modelo
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'] #  Opcional: podemos indicar una lista de métricas a seguir por el modelo
)

# Transformamos la forma de los datos entrenamiento
"""
Se pretende obtener una matriz con 50 imágenes (filas)
y sus respectivos 784 píxeles (columnas)
"""
train_data = train_data.reshape((50, 784))

# Entrenamos el modelo
model.fit(train_data, train_labels, validation_split=0.2, epochs=3)

# Transformamos la forma de los datos de prueba
test_data = test_data.reshape((10, 784))

# Evaluamos el modelo
model.evaluate(test_data, test_labels)