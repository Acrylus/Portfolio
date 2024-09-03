import streamlit as st

pages = {
    "About Me": [
        st.Page("views/pages/Profile.py", title="Profile", icon=":material/person:"),
        st.Page("views/pages/Repository.py", title="Repository", icon=":material/home_storage:"),
        st.Page("views/pages/Persona.py", title="Persona", icon=":material/stadia_controller:"),
    ],
    "Streamlit": [
        st.Page("views/pages/Image.py", title="Image", icon=":material/image:"),
        st.Page("views/pages/Video.py", title="Video", icon=":material/video_library:"),
        st.Page("views/pages/Chat.py", title="Chat", icon=":material/chat:"),
        st.Page("views/pages/Celebration.py", title="Celebration", icon=":material/celebration:"),
        st.Page("views/pages/Code.py", title="Code", icon=":material/code:"),
        st.Page("views/pages/Color.py", title="Color", icon=":material/format_color_fill:"),
    ],
}

st.sidebar.write('Background Music')
st.sidebar.audio("views/sounds/PlutoProjector.mp3", format="audio/mpeg", loop=True, autoplay=True)
st.sidebar.image("views/images/Logo&Name.png")

pg = st.navigation(pages)
pg.run()