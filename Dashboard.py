import streamlit as st

pages = {
    "About Me": [
        st.Page("pages/Profile.py", title="Profile", icon=":material/person:"),
        st.Page("pages/Repository.py", title="Repository", icon=":material/home_storage:"),
        st.Page("pages/Persona.py", title="Persona", icon=":material/stadia_controller:"),
    ],
    "Streamlit": [
        st.Page("pages/Image.py", title="Image", icon=":material/image:"),
        st.Page("pages/Video.py", title="Video", icon=":material/video_library:"),
        st.Page("pages/Chat.py", title="Chat", icon=":material/chat:"),
        st.Page("pages/Celebration.py", title="Celebration", icon=":material/celebration:"),
        st.Page("pages/Code.py", title="Code", icon=":material/code:"),
        st.Page("pages/Color.py", title="Color", icon=":material/format_color_fill:"),
    ],
}

st.sidebar.write('Background Music')
st.sidebar.audio("sounds/PlutoProjector.mp3", format="audio/mpeg", loop=True, autoplay=True)
st.sidebar.image("images/Logo&Name.png")

pg = st.navigation(pages)
pg.run()