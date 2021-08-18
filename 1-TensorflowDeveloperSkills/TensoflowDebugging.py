"""
El siguiente código muestra cómo debuggear un modelo creado con tensorflow
para clasificar las imágenes de escritura manuscrita MNIST
"""

"""
Un programa base en tensorflow consta de dos secciones discretas:
1. Construir la gráfica computacional (un tf.Graph)
2. Correr la gráfica computacional (usando tf.Session)

El cálculo actualmente se lleva a cabi con session.run(), lo que significa
que necesitamos encontrar una manera de inspeccionar los valores dentro de
esta función
"""

