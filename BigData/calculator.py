from unittest import result

import streamlit as st


st.title("Calculator")
number1 = st.number_input("Enter first number", step=1)
number2 = st.number_input("Enter second number", step=1)
op = st.selectbox("selectbox",["+","-","x","/"], index=None)
result = 0.0
if st.button("Calculate"):
    if op is None:
        st.error("Selection options first")
        st.stop()

    if op == "+":
        result = number1 + number2
    elif op == "-":
        result = number1 - number2
    elif op == "x":
        result = number1 * number2
    elif op == "/":
        if number2 == 0:
            st.error("You can't divide by zero")
            st.stop()
        result = number1 / number2
    st.success(result)