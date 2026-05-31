import streamlit as st
import os


st.title("File Uploader")
st.divider()

st.header("Upload Image")
img_files = st.file_uploader("Upload Image", type=["jpg","gif","png"], accept_multiple_files=True)
if img_files is not None and len(img_files) > 0:
    os.makedirs("UploadImages", exist_ok=True)
    for img_file in img_files:
        st.image(img_file, caption=f"Uploaded image: {img_file.name}", use_container_width=False)
        with open(os.path.join("UploadImages", img_file.name), "wb") as f:
            f.write(img_file.getbuffer())
    st.success(f"Successfully uploaded image: {(',').join([i.name for i in img_files])}")

st.header("Upload Files")
files = st.file_uploader("Upload Files", accept_multiple_files=True)
if files:
    os.makedirs("Attachments", exist_ok=True)
    st.info(f"files information: ")
    for file in files:
        with open(os.path.join("Attachments", file.name), "wb") as f:
            f.write(file.getbuffer())
        # 提取后缀名，代替file.type，因为file.type显示的不是文件后缀，而是浏览器识别的 MIME 类型
        ext = os.path.splitext(file.name)[1]
        # ext = file.name.split(".")[1] # 缺失"."
        st.write(f"**{file.name}**，Size: {file.size / 1024:.2f} KB，Type: {ext}")
    st.success(f"Successfully uploaded files：{(','.join([f.name for f in files]))}")