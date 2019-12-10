# Import flask which will handle our communication with the frontend
# references: https://www.youtube.com/watch?v=f6Bf3gl4hWY
from flask import Flask, render_template, request
# Outdated version of Scipy used
from scipy.misc import imread, imresize, imsave
import numpy as np
import re
import sys
import base64
import tensorflow as tf
from keras.models import load_model

# Initialize flask app
app = Flask(__name__)

# initialize variables
global model, graph

#graph 
graph = tf.get_default_graph()

# model 
model = load_model('model.h5')

#convert the image to base64
def convertImage(imgData1):
  imgstr = re.search(r'base64,(.*)', str(imgData1)).group(1)
  with open('output.png', 'wb') as output:
    output.write(base64.b64decode(imgstr))
 
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/predict/', methods=['GET', 'POST'])
def predict():

  # Predict method is called when predict button is clicked
  # on the webpage. The image drawn on the webpage will be
  # fed to the model, and return its label
  imgData = request.get_data()
  convertImage(imgData)
  # read the image into memory
  x = imread('output.png', mode='L')
  # make it the right size
  x = imresize(x, (28, 28))/255
  #Saving the image
  imsave('final_image.jpg', x)
  x = x.reshape(1, 28, 28, 1)
  with graph.as_default():
    out = model.predict(x)
    response = np.argmax(out, axis=1)
    return str(response[0])

if __name__ == "__main__":
# run the app locally on the given port
	app.run(host='0.0.0.0', port=5000, threaded=False)