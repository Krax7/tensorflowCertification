# Cómo reducir el tiempo de entrenamiento de un modelo de aprendizaje profundo utilizando tf.data

Consulta el artículo original en inglés [aquí](https://towardsdatascience.com/how-to-reduce-training-time-for-a-deep-learning-model-using-tf-data-43e1989d2961)

Aprende a cread un proceso de entrada de imágenes para eficientar el uso de los recursos de las CPU y GPU para procesar
un dataset de imágenes y reducir el tiempo de entrenamiento de un modelo de aprendizaje profundo.

En este artículo aprenderás:

- Cómo son utilizados los recurso de la CPU y la GPU para el pre-procesamiento de datos y entrenamiento.
- Cómo utilizar eficientemente los recursos de la CPU y la GPU para el pre procesaiento y entrenamiento.
- Cómo utilizar tf.data para construir un pipeline de entrada eficiente.
- Cómo construir un pipeline de entrada eficiente para imágenes utilizando tf.data

## ¿Cuál es la aproximación ingenua para construir el pipeline de entrada y el entrenamiento del modelo?
Al crear un canal de entrada de datos, normalmente realizamos el proceso ETL (Extraer, Transformar y Cargar).
![img.png](img.png)

- Extracción, extrae los datos de diferentes fuentes de datos como fuentes de datos locales, que pueden ser de un disco
  duro o extraer datos de fuentes de datos remotas como el almacenamiento en la nube.

# Descarga de datos
En este punto ese necesario que sepas que existe una Kaggle API (¡yo tampoco lo podía creer!), gracias a ella podemos
obtener datasets de Kaggle sin mayor esfuerzo, incluyendo el dataset para este ejercicio.
- [Instrucciones para instalar la API y crear tu credenciales](https://github.com/Kaggle/kaggle-api)
- Descarga al dataset con el siguiente comando: `kaggle competitions download -c dogs-vs-cats`
