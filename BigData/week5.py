import streamlit as st
import os

st.title("SONG JINGTAO")
st.header("My first app")
# st.image("test_image.jpg", width=500)
# 获取当前py文件所在目录
base_path = os.path.dirname(__file__)
img_path = os.path.join(base_path, "test_image.jpg")
st.image(img_path, width=500)
st.text("My first text")
st.text("My second text")
st.text("My third text")
st.success("Welcome to my first Streamlit app!")
