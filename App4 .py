import tensorflow as tf
import streamlit as st
from keras.models import load_model
from keras.preprocessing import image
import requests
from io import BytesIO
from PIL import Image, ImageOps
import numpy as np
import os

st.set_option("deprecation.showfileUploaderEncoding", False)
@st.cache(allow_output_mutation=True)

def load_model():
    model = tf.keras.models.load_model('model.h5')
    return model
with st.spinner("Loading model into memory..."):
  model1 = load_model()
# setting the title
st.title('Pneumonia classifier')
st.header('Please upload a chest X-ray image')
file = st.file_uploader("Please upload an x-ray image", type=["jpeg", "jpg", "png"])
def import_and_predict(image_data, model):
  size= (224, 224)
  image= ImageOps.fit(image_data, size, Image.ANTIALIAS)
  img = np.asarray(image)
  img_reshape= np.expand_dims(img, axis=0)
  prediction = model1.predict(img_reshape)
  return prediction
if file is None:
  st.text("Please upload the x-ray image file")
else:
  image = Image.open(file)
  st.image(image, use_column_width= True)
  predictions = import_and_predict(image, model1)
  class_names= ["PNEUMONIA", "NORMAL"]
  string= class_names[np.argmax(predictions)]
  st.success(string)
