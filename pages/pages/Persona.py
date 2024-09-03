import streamlit as st
import base64

st.logo(
    "images/Acrylus.png",
    link="https://streamlit.io/gallery",
    icon_image="images/Acrylus.png",
)

st.markdown(
    """
    <style>
    .reportview-container {
        display: flex;
        justify-content: center;
    }
    
    .profile {
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 50%;
        border: 5px solid orange;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def ImageData(ImagePath):
    with open(ImagePath, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

Profile_Steam = ImageData("images/games/Zairen.jpg")
Profile_Roblox = ImageData("images/games/Roblox.png")

st.title('Online Persona')
st.subheader('Acrylus')

st.write('---')

st.subheader('Adventure Quest Worlds Profile:')

st.image("images/AQW.png")

st.write('---')

st.subheader('Game profiles:')

Left, Right = st.columns(2)

with Left:
    with st.expander("Steam"):
        st.markdown(f'<img src="data:image/png;base64, {Profile_Steam}" class="profile">', unsafe_allow_html=True)
        st.link_button("Steam", "https://steamcommunity.com/profiles/76561198451592328/")
    
with Right:
    with st.expander("Roblox"):
        st.markdown(f'<img src="data:image/png;base64, {Profile_Roblox}" class="profile">', unsafe_allow_html=True)
        st.link_button("Roblox", "https://www.roblox.com/users/4898548456/profile")



    


