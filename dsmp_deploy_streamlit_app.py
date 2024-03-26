# -*- coding: utf-8 -*-
"""DSMP_Deploy_StreamLit_App.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qsg_cAY8Bwa8rzNXc5LZOQjbAjWCNN13
"""

#!pip install -q streamlit

# Commented out IPython magic to ensure Python compatibility.
# # Create a streamlit app example
# %%writefile app.py
# import streamlit as st
# st.write('Hello, *World!* :sunglasses:')

# Install localtunnel to serve the Streamlit app
!npm install localtunnel

#Run the Streamlit app in the background
!streamlit run app.py &>/content/logs.txt &

"""import urllib
print("Password/Enpoint IP for localtunnel is:",urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("\n"))

# Expose the Streamlit app on port 8501
# Then just click in the url showed.

!npx localtunnel --port 8501
"""