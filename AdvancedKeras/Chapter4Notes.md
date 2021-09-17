# Apunte Single model for classification and regression
## Chapter 4 - Advanced Deep Learning with Keras

Video: Modelo de regresión y clasificación.
- El modelo de regresión va a predecir la diferencia de puntaje entre los dos equipos de acuerdo a su diferencia en seed (la puntuación dada por el comité a cada equipo de acuerdo a su "fortaleza").
- El peso calculado para ese modelo es igual a la diferencia en puntaje que tiene que haber entre los dos equipos para predecir por cuánto va a ganar el equipo 1 (siempre que esa diferencia sea a favor del equipo 1)
- Con lo que predijo el modelo de regresión, se clasifica si el equipo va a ganar o perder según su puntaje mediante una función sigmoidal.
- Ahora, podemos predecir la probabilidad de ganar para el equipo 1 si enfrentamos a dos equipos donde se predijo que la diferencia entre sus puntajes iba a ser de 1.
- Se usó lo siguiente:
from scipy.special import expit as sigmoid
print(sigmoid(1 * 0.13870609(peso) + 0.00734114(bias)))
Resulta en ~0.54. Esto quiere decir que el modelo aprendió que para dos equipos donde se predijo que su diferencia de puntaje sería 1, entonces probailidad de que gane el equipo 1 es del 54%
- Cuando evaluamos el modelo, tenemos que pasar la entrada y las dos columnas de salidas como listas.
- El resultado es una lista de 3 elementos que representan las pérdidas. El primer número es la pérdida general del modelo, es decir, la suma de las pérdidas de la capa de regresión y la capa de clasificación. Los otros dos números son las pérdidas para los dos modelos en orden de aparición, respectivamente.
- Nota interesante: Si tus entradas y salidas tienen promedios muy cercanos a cero, entonces no es necesario implementar el bias para que el modelo se ajuste bien a los datos.