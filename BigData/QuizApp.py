import streamlit as st


st.title("🧠 Mini Quiz App")
st.write("Answer the following multiple choice questions.")

st.subheader("Question 1")
q1 = st.radio(
    "What is the capital city of Malaysia?",
    ["Penang", "Johor Bahru", "Kuala Lumpur", "Ipoh"],
    index=None
)
st.divider()

st.subheader("Question 2")
q2 = st.radio(
    "Which language is mainly used for Streamlit apps?",
    ["Java", "Python", "C++", "PHP"],
    index=None
)
st.divider()

st.subheader("Question 3")
q3 = st.radio(
    "Which function is used to create a button in Streamlit?",
    ["st.text()", "st.write()", "st.button()", "st.radio()"],
    index=None
)
st.divider()

if st.button("Submit Quiz"):
    score = 0
    # Question 1 Checking
    if q1 == "Kuala Lumpur":
        st.success("Question 1: Correct!")
        score += 1
    else:
        st.error("Question 1: Wrong! Correct answer is Kuala Lumpur.")

    # Question 2 Checking
    if q2 == "Python":
        st.success("Question 2: Correct!")
        score += 1
    else:
        st.error("Question 2: Wrong! Correct answer is Python.")

    # Question 3 Checking
    if q3 == "st.button()":
        st.success("Question 3: Correct!")
        score += 1
    else:
        st.error("Question 3: Wrong! Correct answer is st.button().")

    # Final Score
    st.divider()
    st.header(f"🎯 Your Total Score: {score} / 3")

    # Optional message
    if score == 3:
        st.success("Excellent! You got all questions correct.")
        st.balloons()
    elif score == 2:
        st.info("Good job! Almost perfect.")
    else:
        st.warning("Keep practicing and try again!")