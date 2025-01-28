import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

def main():
    # App title
    st.title("Streamlit App Demo")

    # Sidebar
    st.sidebar.title("Sidebar")
    st.sidebar.markdown("Use the sidebar to navigate and adjust settings.")

    # Text Input
    st.header("1. Text Input")
    name = st.text_input("What's your name?", "John Doe")
    st.write(f"Hello, {name}!")

    # Slider
    st.header("2. Slider")
    age = st.slider("How old are you?", 0, 100, 25)
    st.write(f"You are {age} years old.")

    # Date Input
    st.header("3. Date Input")
    today = st.date_input("Pick a date:", date.today())
    st.write(f"You picked {today}.")

    # Checkbox
    st.header("4. Checkbox")
    agree = st.checkbox("I agree")
    if agree:
        st.write("Thank you for agreeing!")

    # Radio Button
    st.header("5. Radio Button")
    option = st.radio("Choose one:", ["Option 1", "Option 2", "Option 3"])
    st.write(f"You selected: {option}")

    # Selectbox
    st.header("6. Selectbox")
    select_option = st.selectbox("Choose a number:", [1, 2, 3, 4, 5])
    st.write(f"You selected: {select_option}")

    # Multiselect
    st.header("7. Multiselect")
    multi_options = st.multiselect("Pick multiple numbers:", [1, 2, 3, 4, 5], [1, 3])
    st.write(f"You selected: {multi_options}")

    # File Upload
    st.header("8. File Upload")
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:")
        st.dataframe(data)

    # Charts
    st.header("9. Charts")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.line_chart(chart_data)
    st.bar_chart(chart_data)

    # Dataframe
    st.header("10. Dataframe")
    df = pd.DataFrame(
        {
            'Column 1': [1, 2, 3, 4],
            'Column 2': ['A', 'B', 'C', 'D']
        }
    )
    st.dataframe(df)

    # Progress Bar
    st.header("11. Progress Bar")
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)

    # Markdown
    st.header("12. Markdown")
    st.markdown("**This is bold text.**")
    st.markdown("_This is italic text._")

    # Code
    st.header("13. Code")
    st.code("print('Hello, Streamlit!')")

    # Balloons
    st.header("14. Balloons")
    if st.button("Celebrate"):
        st.balloons()

    # Image
    st.header("15. Image")
    st.image("https://www.streamlit.io/images/brand/streamlit-mark-light.png", caption="Streamlit Logo")

    # Sidebar Interaction
    st.sidebar.header("Sidebar Interaction")
    sidebar_choice = st.sidebar.selectbox("Choose a section:", ["Introduction", "Charts", "Widgets"])
    st.sidebar.write(f"You selected {sidebar_choice}.")

if __name__ == "__main__":
    main()
