import streamlit as st

pages = {
    "About Me": [
        st.Page("pages/pages/Profile.py", title="Profile", icon=":material/person:"),
        st.Page("pages/pages/Repository.py", title="Repository", icon=":material/home_storage:"),
        st.Page("pages/pages/Persona.py", title="Persona", icon=":material/stadia_controller:"),
    ],
    "Streamlit": [
        st.Page("pages/pages/Image.py", title="Image", icon=":material/image:"),
        st.Page("pages/pages/Video.py", title="Video", icon=":material/video_library:"),
        st.Page("pages/pages/Chat.py", title="Chat", icon=":material/chat:"),
        st.Page("pages/pages/Celebration.py", title="Celebration", icon=":material/celebration:"),
        st.Page("pages/pages/Code.py", title="Code", icon=":material/code:"),
        st.Page("pages/pages/Color.py", title="Color", icon=":material/format_color_fill:"),
    ],
}

st.sidebar.write('Background Music')
st.sidebar.audio("pages/sounds/PlutoProjector.mp3", format="audio/mpeg", loop=True, autoplay=True)
st.sidebar.image("pages/images/Logo&Name.png")

pg = st.navigation(pages)
pg.run()