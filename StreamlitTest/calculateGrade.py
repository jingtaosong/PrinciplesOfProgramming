import streamlit as st


st.title("Calculate Grade")
st.header("Personal information")
name = st.text_input("name", placeholder="Enter your name")
student_id = st.text_input("Student ID", placeholder="Enter your student ID")

st.header("Grade")
st.subheader("Enter your grade (out of 100)")
math = st.number_input("math", min_value=0.0, max_value=100.00, step=1.0)
english = st.number_input("english", min_value=0.0, max_value=100.00, step=1.0)
history = st.number_input("history", min_value=0.0, max_value=100.00, step=1.0)

st.divider()
if st.button("Grade", help="Calculate Grade"):
    if not name or not student_id:
        # st.error("Please enter your name and student ID")
        st.markdown("<span style='color:red'>❌ Error: Name/Student ID cannot be empty</span>", unsafe_allow_html=True)
        st.stop()
    avg = sum([math, english, history]) / 3
    if avg >= 80:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "D"
    st.write(f"Hello: {name}({student_id}), Your average score is: {avg:.2f}")
    if grade == "A":
        st.success(f"Grade: {grade} - Excellent！")
    elif grade in ["B", "C"]:
        st.warning(f"Grade: {grade} - Keep it up！")
    else:
        st.error(f"Grade：{grade} - Failed！")