import streamlit as st

st.title("Color Picker")

st.write('---')

selected_color = st.color_picker("Pick a color")

st.markdown(
    f"""
    <div style="background-color:{selected_color}; padding:20px; border-radius:25px">
        {selected_color}
    </div>
    """,
    unsafe_allow_html=True
)