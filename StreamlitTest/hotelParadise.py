import streamlit as st
from PIL import Image
from datetime import date
import os

st.title("Welcome to Paradise Hotel")
image = Image.open(os.path.join(os.getcwd(), "ParadiseHotel.jpg"))
st.image(image, caption="Paradise Hotel", use_container_width=True)
st.write("Enjoy your stay with us!")

st.header("Select Your Stay Dates")
start_date = st.date_input("Select Check-in Date", value=date.today())
end_date = st.date_input("Select Check-out Date", value=None)
if end_date is None:
    st.stop()
if end_date > start_date:
    days = (end_date - start_date).days
    st.success("Your stay has been selected!")
    st.write(f"Check-in date: {start_date}")
    st.write(f"Check-out date: {end_date}")
    st.write(f"Total Stay: {days} night(s)")
else:
    st.error("Check-out date must be after check-in date")