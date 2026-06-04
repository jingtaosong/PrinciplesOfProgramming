import datetime
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import os
import random
import sys
import time
import streamlit as st

# st.title("Practice Programming")
st.set_page_config(page_title="Practice Programming", layout="wide")
st.markdown("""
<style>
:target {
    scroll-margin-top: 75px;
}
</style>
""", unsafe_allow_html=True)
st.title("Practice Programming")

nav_items = {
    1: "lambda function called square",
    2: "Convert Celsius temperature to Fahrenheit",
    3: "Passing scores",
    4: "Students information",
    5: "Even numbers",
    6: "Comprehension & Upper",
    7: "3×3 multiplication table",
    8: "Dictionary & Dictionary Comprehension",
    9: "logger decorator",
    10: "timer decorator",
    11: "validate_positive decorator",
    12: "generator function countdown",
    13: "generator function fibonacci",
    14: "Sensor",
    15: "Function safe_divide(a, b)",
    16: "File operation",
    17: "Write CSV file",
    # 17_1: "Write CSV file(Process data with Pandas)",
    18: "Log Manger",
    19: "NumPy",
    20: "DataFrame",
    21: "DataFrame Operation",
    22: "Matplotlib"
}

with st.sidebar:
    st.subheader("📌 Quick Navigation")
    for idx, title in nav_items.items():
        # 生成锚点ID（去除特殊字符，保证唯一性）
        anchor_id = f"section-{idx}"
        # 生成点击跳转的链接
        # nav_link = f'<a href="#{anchor_id}" style="text-decoration: none; color: inherit;">{idx}. {title}</a>'
        nav_link = f'<a href="#{anchor_id}">{idx}. {title}</a>'
        # 在侧边栏显示导航项（按钮样式）
        st.markdown(
            f'''
            <div style="background-color: #f0f2f6;">
                {nav_link}
            </div>
            ''',
            unsafe_allow_html=True
        )

# 1.lamdba function called square
# st.subheader("1.lamdba function called square")
st.markdown(f'<span id="section-1"><h3>1.{nav_items[1]}</h3></span>', unsafe_allow_html=True)
code_text = """
square_lamdba = lambda x: x ** 2
st.markdown(f"5 square: {square_lamdba(5)}")
st.markdown(f"12 square: {square_lamdba(12)}")
st.markdown(f"100 square: {square_lamdba(100)}")
"""
with st.expander("View Code"):
    st.code(code_text, language="python")
with st.container(height='content', border=True):
    square_lamdba = lambda x: x ** 2
    st.markdown(f"5 square: {square_lamdba(5)}")
    st.markdown(f"12 square: {square_lamdba(12)}")
    st.markdown(f"100 square: {square_lamdba(100)}")

# 2.Convert Celsius temperature to Fahrenheit
# st.subheader("2.Convert Celsius temperature to Fahrenheit")
st.markdown(f'<span id="section-2"><h3>2.{nav_items[2]}</h3></span>', unsafe_allow_html=True)
temps = [36.6, 38.1, 37.0, 39.4, 36.9]
fahrenheit = list(map(lambda x: round(x * 9 / 5, 1) + 32, temps))
code_text2 = """
fahrenheit = list(map(lambda x: round(x * 9/5, 1) + 32, temps))
"""
with st.expander("View Code"):
    st.code(code_text2, language="python")
with st.container(height='content', border=True):
    st.markdown(f"Celsius temperature: {temps}")
    st.markdown(f"Convert Celsius temperature to Fahrenheit: {fahrenheit}")

# 3.Passing scores
# st.subheader("3.Passing scores")
st.markdown(f'<span id="section-3"><h3>3.{nav_items[3]}</h3></span>', unsafe_allow_html=True)
scores = [45, 78, 62, 90, 33, 55, 81, 29]
filter_scores = list(filter(lambda x: x >= 60, scores))
code_text3 = """
filter_scores = list(filter(lambda x: x >= 60, scores))
"""
with st.expander("View Code"):
    st.code(code_text3, language="python")
with st.container(height='content', border=True):
    st.markdown(f"scores: {scores}")
    st.markdown(f"filter_scores: {filter_scores}")

# 4.Students information
# st.subheader("4.Students information")
st.markdown(f'<span id="section-4"><h3>4.{nav_items[4]}</h3></span>', unsafe_allow_html=True)
students = [('Aisha', 88), ('Ben', 73), ('Chen', 91), ('Diana', 65), ('Ethan', 55)]
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
pass_score = list(filter(lambda x: x[1] >= 70, students_sorted))
students_format = list(map(lambda x: f"{x[0]}:{x[1]}/100", students_sorted))
code_text4 = """
students_sorted = sorted(students, key=lambda x: x[1], reverse=True)
pass_score = list(filter(lambda x: x[1] >= 70, students_sorted))
students_format = list(map(lambda x: f"{x[0]}:{x[1]}/100", students_sorted))
"""
with st.expander("View Code"):
    st.code(code_text4, language="python")
with st.container(height='content', border=True):
    st.markdown(f"Students information: {students_sorted}")
    st.markdown(f"Sorted Students by Score (Descending): {students_sorted}")
    st.markdown(f"Students Score >= 70: {pass_score}")
    st.markdown(f"Students formatted strings: {students_format}")

# 5.Even numbers
# st.subheader("5.Even numbers")
st.markdown(f'<span id="section-5"><h3>5.{nav_items[5]}</h3></span>', unsafe_allow_html=True)
even_numbers = [i for i in range(1, 51) if i % 2 == 0]
code_text5 = """
even_numbers = [i for i in range(1, 51) if i % 2 == 0]
"""
with st.expander("View Code"):
    st.code(code_text5, language="python")
with st.container(height='content', border=True):
    st.markdown(f"Even numbers: {even_numbers}")

# 6.Comprehension & Upper
# st.subheader("6.Comprehension & Upper")
st.markdown(f'<span id="section-6"><h3>6.{nav_items[6]}</h3></span>', unsafe_allow_html=True)
words = ['python', 'data', 'science', 'ai', 'cloud', 'iot']
new_words = [word.upper() for word in words if len(word) > 3]
code_text6 = """
new_words = [word.upper() for word in words if len(word) > 3]
"""
with st.expander("View Code"):
    st.code(code_text6, language="python")
with st.container(height='content', border=True):
    st.markdown(f"Old words: {words}")
    st.markdown(f"New words: {new_words}")

# 7. 3×3 multiplication table
# st.subheader("7.3×3 multiplication table")
st.markdown(f'<span id="section-7"><h3>7.{nav_items[7]}</h3></span>', unsafe_allow_html=True)
multi_table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
code_text7 = """
multi_table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
"""
with st.expander("View Code"):
    st.code(code_text7, language="python")
with st.container(height='content', border=True):
    st.markdown("multi table: ")
    for row in multi_table:
        c1, c2, c3, c4 = st.columns([2, 2, 2, 20])
        with c1.container(border=False):
            st.markdown(f"<div style='text-align:center; font-size:20px'>{row[0]}</div>", unsafe_allow_html=True)
        with c2.container(border=False):
            st.markdown(f"<div style='text-align:center; font-size:20px'>{row[1]}</div>", unsafe_allow_html=True)
        with c3.container(border=False):
            st.markdown(f"<div style='text-align:center; font-size:20px'>{row[2]}</div>", unsafe_allow_html=True)

# 8.Dictionary & Dictionary Comprehension
# st.subheader("8.Dictionary & Dictionary Comprehension")
st.markdown(f'<span id="section-8"><h3>8.{nav_items[8]}</h3></span>', unsafe_allow_html=True)
products = [
    {'name': 'Laptop', 'price': 4200},
    {'name': 'Phone', 'price': 1800},
    {'name': 'Tablet', 'price': 950},
    {'name': 'Monitor', 'price': 1100}
]
product_names = [product["name"] for product in products if product["price"] > 1000]
product_discount = {product["name"]: product["price"] * 0.9 for product in products}
code_text8 = """
product_names = [product["name"] for product in products if product["price"] > 1000]
product_discount = {product["name"]: product["price"] * 0.9 for product in products}
"""
with st.expander("View Code"):
    st.code(code_text8, language="python")
with st.container(height='content', border=True):
    st.markdown(f"Original Products: {products}")
    st.markdown(f"Product names with price more than 1000: {product_names}")
    st.markdown(f"Product discount(90%): {product_discount}")

# 9.Write a decorator called logger
# st.subheader("9.logger decorator")
st.markdown(f'<span id="section-9"><h3>9.{nav_items[9]}</h3></span>', unsafe_allow_html=True)


def logger(func):
    def wrapper(*args, **kwargs):
        st.markdown(f"Colling {func.__name__}")
        func(*args, **kwargs)
        st.markdown(f"Done")

    return wrapper


@logger
def greet(name):
    st.markdown(f"Hello {name}!")


code_text9 = """
def logger(func):
    def wrapper(*args, **kwargs):
        st.markdown(f"Colling {func.__name__}")
        func(*args, **kwargs)
        st.markdown(f"Done")
    return wrapper

@logger
def greet(name):
    st.markdown(f"Hello {name}!")
"""
with st.expander("View Code"):
    st.code(code_text9, language="python")
with st.container(height='content', border=True):
    greet("SONG JINGTAO")

# 10.Write a decorator called timer
# st.subheader("10.timer decorator", anchor="select10")
st.markdown(f'<span id="section-10"><h3>10.{nav_items[10]}</h3></span>', unsafe_allow_html=True)


def timer(func):
    def wrapper(*args, **kwargs):
        begin_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        st.markdown(f"Elapsed time: {(end_time - begin_time) * 1000:.3f} ms")
        return result

    return wrapper


@timer
def sum_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum


code_text10 = """
def timer(func):
    def wrapper(*args, **kwargs):
        begin_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        st.markdown(f"Elapsed time: {(end_time - begin_time)*1000} ms")
        return result
    return wrapper

@timer
def sum_squares(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum
"""
with st.expander("View Code"):
    st.code(code_text10, language="python")
with st.container(height='content', border=True):
    st.markdown(f"The sum of squares from 1 to 1,000,000 is: {sum_squares(1000000):,}")

# 11.Build a decorator called validate_positive
st.subheader("11.validate_positive decorator")
st.markdown(f'<span id="section-11"><h3>11.{nav_items[11]}</h3></span>', unsafe_allow_html=True)


def validate_positive(func):
    def wrapper(*args, **kwargs):
        for idx, arg in enumerate(args):
            if not isinstance(args[idx], (int, float)):
                raise ValueError(f"Argument {idx}={arg} invalid, must be number")
            if arg <= 0:
                raise ValueError(f"Argument {idx}={arg} invalid, must be positive")
        return func(*args, **kwargs)

    return wrapper


@validate_positive
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


code_text11 = """
def validate_positive(func):
    def wrapper(*args, **kwargs):
        for idx, arg in enumerate(args):
            if isinstance(args[idx], (int, float)):
                raise ValueError(f"Argument {idx}={arg} invalid, must be number")
            if arg <= 0:
                raise ValueError(f"Argument {idx}={arg} invalid, must be positive")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)
"""
with st.expander("View Code"):
    st.code(code_text11, language="python")
col1, col2, col3 = st.columns([2, 2, 6])
with col1:
    if st.button("Valid Value"):
        st.info(f"Valid Value weight=70, height=1.75：{calculate_bmi(70, 1.75)}")
with col2:
    if st.button("Invalid Value"):
        st.markdown(f"Invalid Value weight=70, height=-1.75：{calculate_bmi(70, -1.75)}")

# 12.Write a generator function countdown
# st.subheader("12.generator function countdown")
st.markdown(f'<span id="section-12"><h3>12.{nav_items[12]}</h3></span>', unsafe_allow_html=True)


def count_down(n):
    while n >= 1:
        yield n
        n -= 1


code_text12 = """
def count_down(n):
    while n >=1 :
        yield n
        n -= 1
for n in count_down(10):
    st.markdown(f"{n}")    
"""
with st.expander("View Code"):
    st.code(code_text12, language="python")
with st.container(height='content', border=True):
    with st.popover("View Result"):
        for n in count_down(10):
            st.markdown(f"{n}")

# 13.Write a generator function fibonacci
# st.subheader("13.generator function fibonacci")
st.markdown(f'<span id="section-13"><h3>13.{nav_items[13]}</h3></span>', unsafe_allow_html=True)


def fibonacci(limit):
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b


code_text13 = """
def fibonacci(limit):
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a+b
st.markdown(f"Fibonacci numbers below 500: {[n for n in fibonacci(500)]}")
"""
with st.expander("View Code"):
    st.code(code_text13, language="python")
with st.container(height='content', border=True):
    st.markdown(f"Fibonacci numbers below 500: {[n for n in fibonacci(500)]}")

# 14.Sensor
# st.subheader("14.Sensor")
st.markdown(f'<span id="section-14"><h3>14.{nav_items[14]}</h3></span>', unsafe_allow_html=True)


def read_sensor(data):
    for n in data:
        yield n


def flag_critical(readings, threshold=40.0):
    for reading in readings:
        if reading > threshold:
            yield reading


data_list = [round(random.uniform(30.0, 45.0), 1) for i in range(1000)]
count = 0
max_value = 0
code_text14 = """
def read_sensor(data):
    for n in data:
        yield n

def flag_critical(readings, threshold=40.0):
    for reading in readings:
        if reading > threshold:
            yield reading

data_list = [random.uniform(30.0,45.0) for i in range(1000)]
with st.expander("View Code", expanded=False):
    st.code(code_text14, language="python")
with st.container(height='content', border=True):
    with st.popover("View 1000 random numbers"):
        st.markdown(f"Reading sensor value: {data_list}")

    col_list, col_chain = st.columns(2)
    with col_list:
        if st.button("View list"):
            critical_list = list(flag_critical(read_sensor(data_list)))
            st.markdown(f"Type: {type(critical_list)}")
            st.markdown(f"Occupy memory: {sys.getsizeof(critical_list)} Bytes")
            st.markdown(f"The count of critical readings: {len(critical_list)}")
            st.markdown(f"The highest value : {max(critical_list)}")
    with col_chain:
        if st.button("View chain"):
            count = 0
            max_value = 0
            critical_gen = flag_critical(read_sensor(data_list))
            for n in critical_gen:
                count += 1
                if n > max_value:
                    max_value = n
            st.markdown(f"Type: {type(critical_gen)}")
            st.markdown(f"Occupy memory: {sys.getsizeof(critical_gen)} Bytes")
            st.markdown(f"The count of critical readings: {count}")
            st.markdown(f"The highest value : {max_value}")
"""
with st.expander("View Code", expanded=False):
    st.code(code_text14, language="python")
with st.container(height='content', border=True):
    with st.popover("View 1000 random numbers"):
        st.markdown(f"Reading sensor value: {data_list}")

    col_list, col_chain = st.columns(2)
    with col_list:
        if st.button("View list"):
            critical_list = list(flag_critical(read_sensor(data_list)))
            st.markdown(f"Type: {type(critical_list)}")
            st.markdown(f"Occupy memory: {sys.getsizeof(critical_list)} Bytes")
            st.markdown(f"The count of critical readings: {len(critical_list)}")
            st.markdown(f"The highest value : {max(critical_list)}")
    with col_chain:
        if st.button("View chain"):
            count = 0
            max_value = 0
            critical_gen = flag_critical(read_sensor(data_list))
            for n in critical_gen:
                count += 1
                if n > max_value:
                    max_value = n
            st.markdown(f"Type: {type(critical_gen)}")
            st.markdown(f"Occupy memory: {sys.getsizeof(critical_gen)} Bytes")
            st.markdown(f"The count of critical readings: {count}")
            st.markdown(f"The highest value : {max_value}")

# 15.Write a function safe_divide
# st.subheader("Function safe_divide(a, b)")
st.markdown(f'<span id="section-15"><h3>15.{nav_items[15]}</h3></span>', unsafe_allow_html=True)


def safe_divide(a, b):
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        st.error("Error: Cannot divide by zero")
    except TypeError:
        st.error("Error: Inputs must be numbers")


with st.expander("View Code", expanded=False):
    code_text15 = """
    def safe_divide(a, b):
    try:
        return round(a / b, 2)
    except ZeroDivisionError:
        st.error("Error: Cannot divide by zero")
    except TypeError:
        st.error("Error: Inputs must be numbers")
    """
    st.code(code_text15, language="python")
with st.container(height='content', border=True):
    st.markdown(f"Test1(10,3): {safe_divide(10, 3)}")
    st.markdown(f"Test2(10,0): ")
    safe_divide(10, 0)
    st.markdown(f"Test3('ten',2): ")
    safe_divide('ten', 2)

BASE_PATH = os.path.dirname(__file__)

# 16.File operation
# st.subheader("16.File operation")
st.markdown(f'<span id="section-16"><h3>16.{nav_items[16]}</h3></span>', unsafe_allow_html=True)


def write_report(filename, data):
    with open(filename, "w") as f:
        # [f.write(d + "\n") for d in data]
        for d in data:
            f.write(d + "\n")


def read_report(filename):
    with open(filename, "r") as f:
        for idx, line in enumerate(f.readlines()):
            st.markdown(f"{idx}: {line}")


with st.expander("View Code", expanded=False):
    code_text16 = """
    def write_report(filename, data):
    with open(filename, "w") as f:
        [f.write(d + "\\n") for d in data]

    def read_report(filename):
        with open(filename, "r") as f:
            for idx, line in enumerate(f.readlines()):
                st.markdown(f"{idx}: {line}")
    """
    st.code(code_text16, language="python")
with st.container(height='content', border=True):
    data = ['Python', 'Data Science', 'Machine Learning', 'Cloud Computing']
    write_report(os.path.join(BASE_PATH, 'report.txt'), data)
    read_report(os.path.join(BASE_PATH, 'report.txt'))

# 17.Write CSV file
# st.subheader("17.Write CSV file")
st.markdown(f'<span id="section-17"><h3>17.{nav_items[17]}</h3></span>', unsafe_allow_html=True)


def create_sorce_csv(filename, header, data):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)


def read_score_csv(filename):
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)


def calculate_score(filename):
    subject_data = {}
    total_data = {}
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            subject = row["Subject"]
            score = int(row["Score"])
            name = row["Name"]

            # 如果科目不在字典里，初始化
            if subject not in subject_data:
                subject_data[subject] = [0, 0]  # [总分, 人数]
            # 累加分数和人数
            subject_data[subject][0] += score
            subject_data[subject][1] += 1

            if name not in total_data:
                total_data[name] = 0
            total_data[name] += score

        st.markdown(f"# The average score per subject:")
        for subject, (total, count) in subject_data.items():
            st.markdown(f"{subject} average: {total / count:.2f}")

        total_name, total_score = max(total_data.items(), key=lambda x: x[1])
        st.markdown(f"# The top score overall:{total_score}, Winner:{total_name}")


with st.expander("View Code", expanded=False):
    code_text17 = """
def create_sorce_csv(filename, header, data):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

def read_score_csv(filename):
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)

def calculate_score(filename):
    subject_data = {}
    total_data = {}
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            subject = row["Subject"]
            score = int(row["Score"])
            name = row["Name"]

            # 如果科目不在字典里，初始化
            if subject not in subject_data:
                subject_data[subject] = [0, 0]  # [总分, 人数]
            # 累加分数和人数
            subject_data[subject][0] += score
            subject_data[subject][1] += 1

            if name not in total_data:
                total_data[name] = 0
            total_data[name] += score

        st.markdown(f"# The average score per subject:")
        for subject, (total, count) in subject_data.items():
            st.markdown(f"{subject} average: {total / count:.2f}")

        total_name, total_score = max(total_data.items(), key=lambda x: x[1])
        st.markdown(f"# The top score overall:{total_score}, Winner:{total_name}")

with st.container(height='content', border=True):
    header = ["Name", "Subject", "Score"]
    data = [
        ["S1", "Math", 90],
        ["S1", "English", 88],
        ["S2", "Math", 98],
        ["S2", "English", 95],
        ["S3", "English", 99],
        ["S3", "English", 92]
    ]
    create_sorce_csv(os.path.join(BASE_PATH, 'score.csv'), header, data)
    st.markdown(f"# The CSV file data: ")
    st.table(read_score_csv(os.path.join(BASE_PATH, 'score.csv')))
    calculate_score(os.path.join(BASE_PATH, 'score.csv'))
    """
    st.code(code_text17, language="python")
with st.container(height='content', border=True):
    header = ["Name", "Subject", "Score"]
    data = [
        ["S1", "Math", 90],
        ["S1", "English", 88],
        ["S2", "Math", 98],
        ["S2", "English", 95],
        ["S3", "English", 99],
        ["S3", "English", 92]
    ]
    create_sorce_csv(os.path.join(BASE_PATH, 'score.csv'), header, data)
    st.markdown(f"# The CSV file data: ")
    st.table(
        read_score_csv(os.path.join(BASE_PATH, 'score.csv')),
        width="content",
        height="content"
    )
    calculate_score(os.path.join(BASE_PATH, 'score.csv'))

# 17_1.Write CSV file(Pandas)
st.subheader("17_1.Write CSV file(Process data with Pandas)")
with st.expander("View Code", expanded=False):
    code_text17_1 = """
df = pd.read_csv(os.path.join(BASE_PATH, 'score.csv'), encoding="utf-8")

st.markdown(f"#  The CSV file data: ")
st.dataframe(df, width="content", height="content")

subject_data = df.groupby("Subject")["Score"].mean()
st.markdown(f"# The average score per subject:")
st.dataframe(subject_data, width="content", height="content")

total_date = df.groupby("Name")["Score"].sum().to_dict()
total_name, total_score = max(total_date.items(), key=lambda x: x[1])
st.markdown(f'''
# 🏆 Top Score: <span style='color:red'>{total_score}</span> | Winner: <span style='color:blue'>{total_name}</span>
''', unsafe_allow_html=True)  
    """
    st.code(code_text17_1, language="python")
with st.container(height='content', border=True):
    df = pd.read_csv(os.path.join(BASE_PATH, 'score.csv'), encoding="utf-8")

    st.markdown(f"#  The CSV file data: ")
    st.dataframe(df, width="content", height="content")

    subject_data = df.groupby("Subject")["Score"].mean()
    st.markdown(f"# The average score per subject:")
    st.dataframe(subject_data, width="content", height="content")

    total_date = df.groupby("Name")["Score"].sum().to_dict()
    total_name, total_score = max(total_date.items(), key=lambda x: x[1])
    st.markdown(f"""
    # 🏆 Top Score: <span style='color:red'>{total_score}</span> | Winner: <span style='color:blue'>{total_name}</span>
    """, unsafe_allow_html=True)

# 18.Log Manger
# st.subheader("18.Log Manger")
st.markdown(f'<span id="section-18"><h3>18.{nav_items[18]}</h3></span>', unsafe_allow_html=True)


def append_log(filename, level, message):
    with open(filename, 'a') as f:
        f.write(f"[{datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")}][{level}]: {message}\n")


def filter_log(filename, level):
    with open(filename, 'r') as f:
        for line in f.readlines():
            if level == line.split('][')[1].split(']')[0]:
                yield line


code_text18 = """
def append_log(filename, level,message):
    with open(filename, 'a') as f:
        f.write(f"[{datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")}][{level}]: {message}\n")

def filter_log(filename, level):
    with open(filename, 'r') as f:
        for line in f.readlines():
            if level == line.split('][')[1].split(']')[0]:
                yield line

filename_log = os.path.join(BASE_PATH, 'log.txt')
append_log(filename_log,"INFO","test message1")
append_log(filename_log,"INFO","test message2")
append_log(filename_log,"WARNING","test message3")
append_log(filename_log,"ERROR","test message4")
append_log(filename_log,"ERROR","test message5")
for msg in filter_log(filename_log, "INFO"):
    st.markdown(msg)
"""
with st.expander("View Code", expanded=False):
    st.code(code_text18, language="python")
with st.container(height='content', border=True):
    if st.button("test"):
        filename_log = os.path.join(BASE_PATH, 'log.txt')
        append_log(filename_log, "INFO", "test message1")
        append_log(filename_log, "INFO", "test message2")
        append_log(filename_log, "WARNING", "test message3")
        append_log(filename_log, "ERROR", "test message4")
        append_log(filename_log, "ERROR", "test message5")
        for msg in filter_log(filename_log, "INFO"):
            st.markdown(msg)

# 19.NumPy
# st.subheader("19.NumPy")
st.markdown(f'<span id="section-19"><h3>19.{nav_items[19]}</h3></span>', unsafe_allow_html=True)
code_text19 = """
# i.10 evenly spaced values between 0 and 1
arr_linespace = np.linspace(0,1,10)
st.markdown("# 10 evenly spaced values between 0 and 1")
st.markdown(f"Shape: {arr_linespace.shape}")
st.markdown(f"Dtype: {arr_linespace.dtype}")
st.markdown(f"Values:\n {arr_linespace}")
# ii.a 3x3 identity matrix
matrix = np.eye(3)
st.markdown("# 3x3 identity matrix")
st.markdown(f"Shape: {matrix.shape}")
st.markdown(f"Dtype: {matrix.dtype}")
st.markdown(f"Values:\n {matrix}")
# iii.a 4x4 array of random integers between 1 and 100
arr_4d = np.random.randint(1, 101, size=(4,4))
st.markdown("# 4x4 array of random integers between 1 and 100")
st.markdown(f"Shape: {arr_4d.shape}")
st.markdown(f"Dtype: {arr_4d.dtype}")
st.markdown(f"Values:\n {arr_4d}")
"""
with st.expander("View Code", expanded=False):
    st.code(code_text19, language="python")
with st.container(height='content', border=True):
    # i.10 evenly spaced values between 0 and 1
    arr_linespace = np.linspace(0, 1, 10)
    st.markdown("# 10 evenly spaced values between 0 and 1")
    st.markdown(f"Shape: {arr_linespace.shape}")
    st.markdown(f"Dtype: {arr_linespace.dtype}")
    st.markdown(f"Values:\n {arr_linespace}")
    # ii.a 3x3 identity matrix
    matrix = np.eye(3)
    st.markdown("# 3x3 identity matrix")
    st.markdown(f"Shape: {matrix.shape}")
    st.markdown(f"Dtype: {matrix.dtype}")
    st.markdown(f"Values:\n {matrix}")
    # iii.a 4x4 array of random integers between 1 and 100
    arr_4d = np.random.randint(1, 101, size=(4, 4))
    st.markdown("# 4x4 array of random integers between 1 and 100")
    st.markdown(f"Shape: {arr_4d.shape}")
    st.markdown(f"Dtype: {arr_4d.dtype}")
    st.markdown(f"Values:\n {arr_4d}")

# 20.DataFrame
# st.subheader("20.DataFrame")
st.markdown(f'<span id="section-20"><h3>20.{nav_items[20]}</h3></span>', unsafe_allow_html=True)
dic_employee = {
    "Name": ["Employee1", "Employee2", "Employee3", "Employee4", "Employee5", "Employee6"],
    "Department": ["HR", "IT", "OM", "HR", "IT", "Finance"],
    "Salary": [4000, 5000, 6000, 4500, 8000, 9000],
    "Years": [1, 2, 3, 2, 4, 5]
}
df_dic = pd.DataFrame(dic_employee)
code_text20 = """
st.subheader("20.DataFrame")
dic_employee = {
    "Name": ["Employee1", "Employee2", "Employee3", "Employee4", "Employee5", "Employee6"],
    "Department": ["HR", "IT", "OM", "HR", "IT", "Finance"],
    "Salary": [4000, 5000, 6000, 4500, 8000, 9000],
    "Years": [1, 2, 3, 2, 4, 5]
}
df_dic = pd.DataFrame(dic_employee)
st.markdown(f"The DataFrame:")
st.dataframe(df_dic, width="content", height="content")
st.markdown(f"The DataFrame info:")
buffer = StringIO()
df_dic.info(buf=buffer)
st.text(buffer.getvalue())
"""
with st.expander("View Code", expanded=False):
    st.code(code_text20, language="python")
with st.container(height='content', border=True):
    st.markdown(f"The DataFrame:")
    st.dataframe(df_dic, width="content", height="content")
    st.markdown(f"The DataFrame info:")
    buffer = StringIO()
    df_dic.info(buf=buffer)
    st.text(buffer.getvalue())

# 21.DataFrame Operation
# st.subheader("21.DataFrame Operation")
st.markdown(f'<span id="section-21"><h3>21.{nav_items[21]}</h3></span>', unsafe_allow_html=True)
code_text21 = """
# i.Mean salary per department
avg_department = df_dic.groupby("Department")["Salary"].mean()
st.markdown(f"Mean salary per department: ")
st.dataframe(avg_department, width="content", height="content")
# ii.Total salary cost per department
total_salary = df_dic.groupby("Department")["Salary"].sum()
st.markdown(f"Total salary per department: ")
st.dataframe(total_salary, width="content", height="content")
# iii.Count of employees per department
count_employees = df_dic.groupby("Department").size().reset_index(name="Count")
st.markdown(f"Count of employees per department: ")
st.dataframe(count_employees, width="content", height="content", hide_index=True)
# iv.Add a new column 'Bonus' = 10% of salary for Engineering staff and 5% for others
df_dic["Bonus"] = (df_dic["Salary"]*0.1).where(
    df_dic["Department"] == "IT",
    df_dic["Salary"]*0.05
)
st.markdown(f"Bonus: ")
st.dataframe(df_dic, width="content", height="content", hide_index=True)
"""
with st.expander("View Code", expanded=False):
    st.code(code_text21, language="python")
with st.container(height='content', border=True):
    # i.Mean salary per department
    avg_department = df_dic.groupby("Department")["Salary"].mean()
    st.markdown(f"Mean salary per department: ")
    st.dataframe(avg_department, width="content", height="content")
    # ii.Total salary cost per department
    total_salary = df_dic.groupby("Department")["Salary"].sum()
    st.markdown(f"Total salary per department: ")
    st.dataframe(total_salary, width="content", height="content")
    # iii.Count of employees per department
    count_employees = df_dic.groupby("Department").size().reset_index(name="Count")
    st.markdown(f"Count of employees per department: ")
    st.dataframe(count_employees, width="content", height="content", hide_index=True)
    # iv.Add a new column 'Bonus' = 10% of salary for Engineering staff and 5% for others
    df_dic["Bonus"] = (df_dic["Salary"] * 0.1).where(
        df_dic["Department"] == "IT",
        df_dic["Salary"] * 0.05
    )
    st.markdown(f"Bonus: ")
    st.dataframe(df_dic, width="content", height="content", hide_index=True)

# 22.Matplotlit
# st.subheader("22.Matplotlit")
st.markdown(f'<span id="section-22"><h3>22.{nav_items[22]}</h3></span>', unsafe_allow_html=True)
code_text22 = """
x_axis = np.linspace(0, 4 * np.pi, 100)
sin = np.sin(x_axis)
cos = np.cos(x_axis)

# create the figure
plt.figure(figsize=(8, 5))
plt.plot(x_axis, sin, color='blue', linestyle='-', linewidth=2, label='Sine Wave')
plt.plot(x_axis, cos, color='red', linestyle='--', linewidth=2, label='Cosine Wave')
plt.title('Sine and Cosine Wave')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.grid(True)

plt.savefig('waves.png')

# plt.show()
st.pyplot(plt, width=500)
"""
with st.expander("View Code", expanded=False):
    st.code(code_text22, language="python")
x_axis = np.linspace(0, 4 * np.pi, 100)
sin = np.sin(x_axis)
cos = np.cos(x_axis)

# create the figure
plt.figure(figsize=(8, 5))
plt.plot(x_axis, sin, color='blue', linestyle='-', linewidth=2, label='Sine Wave')
plt.plot(x_axis, cos, color='red', linestyle='--', linewidth=2, label='Cosine Wave')
plt.title('Sine and Cosine Wave')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.grid(True)

plt.savefig('waves.png')

# plt.show()
st.pyplot(plt, width=500)
