import smtplib
import streamlit as st
from email.message import EmailMessage
import base64

st.markdown(
    """
    <style>
    .profile {
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 50%;
        border: 5px solid orange;
    }

    .social-icons {
        display: flex;
        justify-content: start;
        gap: 10px; /* Adjust spacing between icons */
    }

    .icon-socials {
        width: 20px;
        height: 20px;
        filter: invert(100%);
    }
    </style>
    """,
    unsafe_allow_html=True
)

Social = [
    {"name": "Facebook", "path": "views/images/socials/Facebook.png", "url": "https://www.facebook.com/acrylus"},
    {"name": "Instagram", "path": "views/images/socials/Instagram.png", "url": "https://www.instagram.com/acryluscrz"},
    {"name": "GitHub", "path": "views/images/socials/Github.png", "url": "https://github.com/Acrylus"},
    {"name": "Threads", "path": "views/images/socials/Threads.png", "url": "https://www.threads.net/acryluscrz"},
    {"name": "LinkedIn", "path": "views/images/socials/LinkedIn.png", "url": "https://www.linkedin.com/in/anton-joseph-cruz-8b13a42b0"},
    {"name": "Discord", "path": "views/images/socials/Discord.png", "url": "https://discordapp.com/users/867040281365970984"},
]

academics = [
    {
        "school": "Cebu Institute of Technology - University",
        "date": "August 2024 - Present",
        "course": "Capstone and Research 2",
        "role": "Leader | Full-Stack Developer | UI/UX Designer",
        "image": "views/images/TOW.png",
        "link": "https://www.cit.edu",
        "project": "Tower of Words",
        "github_link": "https://github.com/satou0419/tower-of-words_repository",
        "web_link": "https://tower-of-words.vercel.app/"
    },
    {
        "school": "Cebu Institute of Technology - University",
        "date": "January 2024 - May 2024",
        "course": "Capstone and Research 1",
        "role": "Leader | Full-Stack Developer | UI/UX Designer",
        "image": "views/images/TOW.png",
        "link": "https://www.cit.edu",
        "project": "Tower of Words",
        "github_link": "https://github.com/satou0419/tower-of-words_repository",
        "web_link": "https://tower-of-words.vercel.app/"
    },
    {
        "school": "Cebu Institute of Technology - University",
        "date": "January 2024 - May 2024",
        "course": "Systems Integration and Architecture",
        "role": "Backend Developer | UI/UX Designer",
        "image": "views/images/TOW.png",
        "link": "https://www.cit.edu",
        "project": "Tower of Words",
        "github_link": "https://github.com/satou0419/tower-of-words_repository",
        "web_link": "https://tower-of-words.vercel.app/"
    },
    {
        "school": "Cebu Institute of Technology - University",
        "date": "August 2023 - December 2023",
        "course": "Application Development",
        "role": "Full-Stack Developer | UI/UX Designer",
        "image": "views/images/TOW.png",
        "link": "https://www.cit.edu",
        "project": "Tower of Words",
        "github_link": "https://github.com/satou0419/tower-of-words_repository",
        "web_link": "https://tower-of-words.vercel.app/"
    }
]

def ImageData(ImagePath):
    with open(ImagePath, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

SocialPaths = [ImageData(social['path']) for social in Social]

Profile = ImageData("views/images/Profile.jpg")

Left, Right = st.columns(2)

with Left:
    st.markdown(f'<img src="data:image/png;base64, {Profile}" class="profile">', unsafe_allow_html=True)

with Right:
    st.title(':orange[Anton Joseph Cruz]')
    st.subheader('IT Student')
    
    st.write('Passionate IT student exploring the world of technology.')

    Icon, Resume  = st.columns([3, 1])

    with Icon:
        st.write('Social Media')
        st.markdown(
            '<div class="social-icons">' +
            ''.join(
                f'<a href="{social["url"]}" target="_blank">'
                f'<img src="data:image/png;base64,{socialPath}" alt="{social["name"]}" class="icon-socials">'
                f'</a>'
                for social, socialPath in zip(Social, SocialPaths)
            ) +
            '</div>',
            unsafe_allow_html=True
        )

    with Resume:  
        st.write('Resume')
        with open("views/files/Resume.pdf", "rb") as pdf_file:
            document = pdf_file.read()

        st.download_button(
            label=":material/download:",
            data=document,
            file_name="Resume.pdf",
            mime="application/pdf"
        )

st.write('---')

st.subheader('Academic Roles & Achievements')

st.write('---')

tabs = ["Capstone and Research 2", "Capstone and Research 1", "Systems Integration and Architecture", "Application Development"]
diatabs = st.tabs(tabs)


for i, tab in enumerate(diatabs):
    with tab:
        with st.container(border=True):
            Tab_Left, Tab_Rigth = st.columns([1, 3])

            with Tab_Left:
                st.image(academics[i]['image'])

            with Tab_Rigth:    
                st.subheader(academics[i]['project'])
                st.write(academics[i]['school'])
                st.write(academics[i]['role'])

                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    st.write(academics[i]['date'])
                with col2:
                    st.link_button("Github", academics[i]['github_link'], type="primary")
                with col3:
                    st.link_button("Website", academics[i]['web_link'], type="secondary")

st.write('---')

# st.subheader('Support :material/favorite:')

# Inspiration = ImageData("images/games/Zairen.jpg")

# image, description = st.columns([1, 3])

# with image:
#     st.markdown(f'<img src="data:image/png;base64, {Inspiration}" class="profile">', unsafe_allow_html=True)

# with description:
#     st.subheader('Zairen Mae Niñofranco')
#     st.link_button("Profile", "https://www.facebook.com/danderexzai", type="primary")

# st.write('---')

def send_email(name, email, message):
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = f"New Contact Form Submission from {name} Email: {email}"
    user = "smsalertprac@gmail.com"
    msg['To'] = "theantonjoseph@gmail.com"
    msg["From"] = user
    password = "nuescnvuiwlhhlqi"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(user, password)
            server.send_message(msg)
        return True
    except smtplib.SMTPAuthenticationError:
        st.error("Authentication failed. Check your email and password.")
    except smtplib.SMTPRecipientsRefused:
        st.error("Recipient address refused. Check the recipient email address.")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

@st.dialog("Contact Me", width="large")
def contact_form():
    st.write("### Contact Form")
    name = st.text_input('Name')
    email = st.text_input('Email')
    message = st.text_area('Message')
    if st.button('Send'):
        if send_email(name, email, message):
            st.session_state.message_sent = True
            st.session_state.contact_info = {
                'Name': name,
                'Email': email,
                'Message': message
            }
            st.rerun()
        else:
            st.error("There was an error sending your message. Please try again later.")

if 'message_sent' in st.session_state and st.session_state.message_sent:
    contact_info = st.session_state.contact_info
    st.write("Thank you for contacting me!")

else:
    if st.button('Contact Me'):
        contact_form()

