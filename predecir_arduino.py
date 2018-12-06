import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from keras.utils import CustomObjectScope ##
from keras.models import model_from_json ##
from keras import losses##
from tensorflow import keras
import h5py

import serial # you need to install the pySerial :pyserial.sourceforge.net
import time
import tkinter
import os
# your Serial port should be different!
arduino = serial.Serial('/dev/ttyACM0', 9600)

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
		    time.sleep(1) 
		    arduino.write(b'A')
  if answer == 0:
        print("pred: Circulo") ##
        print ("The LED is on...")
  if answer == 1:
		    time.sleep(1) 
		    arduino.write(b'B')
  if answer == 1:
        print("pred: Cuadrado") ##
        print ("The LED is off...")

  if answer == 2:
		    time.sleep(1) 
		    arduino.write(b'C')
  if answer == 2:
        print("pred: Triangulo") ##



  return answer
#######################
##predict("1.png") ##cuadrado
##predict("") ##
##predict("") ##
#########################
predict("4.jpg") ##triangulo
##predict("") ##
##predict() ##
#########################
##predict("7.jpg") ##circulo
##predict("") ##
##predict("") ##
#########################
