import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from keras.utils import CustomObjectScope ##
from keras.models import model_from_json ##
from keras import losses##
from tensorflow import keras
import h5py

longitud, altura = 100, 100
modelo= './modelo/modelo.h5'
pesos= './modelo/pesos.h5'
cnn=keras.models.load_model('./modelo/modelo.h5')
##cnn=load_model(modelo)
cnn.load_weights(pesos)

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    print("pred: Circulo") ##
  elif answer == 1:
    print("pred: Cuadrado") ##
  elif answer == 2:
    print("pred: Triangulo") ##

  return answer
#######################
##predict("1.png") ##cuadrado->triangulo
##predict("") ##
##predict("") ##
#########################
##predict("4.jpg") ##triangulo->circulo
##predict("") ##
##predict() ##
#########################
predict("CIRCULO.jpg") ##circulo->cuadrado
##predict("") ##
##predict("") ##
#########################
