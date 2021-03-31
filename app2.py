import streamlit as st
import requests
from PIL import Image
from FruitClassTL import pre_trained_model
import validators

def get_classification (image) :
    st.image(image,caption='Uploaded image.',use_column_width=True)
    st.write ("")
    st.write("Classifying...")
    label = pre_trained_model(image)
    st.dataframe(label,width=1500,height=2000)
    st.write(label)
   

st.title ("Image classification with mobilenet transfert learning")
st.header("De quel fruit s'agit-il ?")
st.text ("Téléchargez une photo")

#button_pc =st.button('Image depuis votre PC')
#button_url=st.button('Image depuis internet')

uploaded_file = st.file_uploader("Chose a fruit image",type="jpeg")
if uploaded_file is not None :
   image = Image.open(uploaded_file)
   st.write ("")
   get_classification (image) 

#if button_url :
#    url_path = st.text_input('Enter image url')
#    valid = validators.url(url_path)
#    if valid == True :
#        st.write ('Importing URL',url_path)
#        image=Image.open(requests.get(url_path,stream=True).raw)
#        st.image(image,caption='Uploaded image.',use_column_width=True)
#        st.write ("")
#        st.write("Classifying...")
#        label = pre_trained_model(image)
#        st.dataframe(label)
#    else :
#        st.write("Not a url !")
