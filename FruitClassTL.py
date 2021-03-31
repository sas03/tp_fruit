
import tensorflow as tf
from tensorflow import keras
import numpy as np
import os
import pandas as pd
from PIL import Image, ImageOps
import PIL
from numpy import asarray


def pre_trained_model (img) :
    #os.chdir('/Users/francois/Desktop/YNOV/MJDL/DLENV/')
    trained_model = tf.keras.models.load_model ('MobileFruits')
    labels = pd.read_csv("Fruits_acc.csv").iloc[0:131,0].values

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1,224,224,3),dtype=np.float32)
    image = img
    #image sizing
    size = (224,224)
    image = ImageOps.fit(image,size,Image.ANTIALIAS)

    #turn image into numpy img_array
    img_array = np.asarray(image)
    img_array_expanded_dims = np.expand_dims(img_array,axis=0)

    #normalize the image_array
    normalized_image_pred=tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

    #predictions
    predictions = trained_model.predict(normalized_image_pred)

    tf_pred_dataframe = pd.DataFrame(predictions).T
    tf_pred_dataframe ['Labels'] = labels
    tf_pred_dataframe.columns = ["Proba","Labels"]
    probas = tf_pred_dataframe.sort_values("Proba",ascending=False).head(3).reset_index(drop=True,inplace=False)

    return (probas)
