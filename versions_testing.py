import sys
import tensorflow
import tensorflow_datasets
import PIL
import pandas
import numpy
import scipy

def check_packages_versions():
    print('Estas son las versiones de tus paquetes:')
    print('Python version {}'.format(sys.version))
    print('TensorFlow version {}'.format(tensorflow.__version__))
    print('TensorFlow Datasets {}'.format(tensorflow_datasets.__version__))
    print('Pillow {}'.format(PIL.__version__))
    print('Pandas {}'.format(pandas.__version__))
    print('Numpy {}'.format(numpy.__version__))
    print('Scipy {}'.format(scipy.__version__))

if __name__ == '__main__':
    check_packages_versions()