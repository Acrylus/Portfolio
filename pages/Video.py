import streamlit as st

st.title('Youtube Stream')
st.write('Stream your favorite youtube video here!')

st.write('---')

videos = {
   "Starting Over Again - Natalie Cole": "https://www.youtube.com/watch?v=cIYGhA26Gjc", 
    "Bite Me - Enhypen": "https://www.youtube.com/watch?v=wXFLzODIdUI",
    "Baggages - Zeke Abella": "https://www.youtube.com/watch?v=BVxnfKAKCGg",
}

selected_video = st.selectbox("Choose a video", list(videos.keys()))

if selected_video:
    st.video(videos[selected_video])

st.write('---')

url = st.text_input('Enter video URL')

if url:
    st.video(url)