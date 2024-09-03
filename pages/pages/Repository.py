import streamlit as st
import base64
import math
import requests

st.markdown(
    """
    <style>
    .icons {
        width: 50px;
        height: 50px;
        position: relative;
    }

    .icon-container{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        position: relative;
        padding-bottom: 2rem; 
        padding-top: 2rem; 
    }

    .progress-circle {
        position: absolute;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 100%;
        pointer-events: none;
        transform: rotate(-90deg);
    }

    .icon-name {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .icon-percentage {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    h6 {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    
LanguageIcons = {
    "HTML": "pages/images/languages/Html.png",
    "CSS": "pages/images/languages/CSS.png",
    "SCSS": "pages/images/languages/SCSS.png",
    "JavaScript": "pages/images/languages/JavaScript.png",
    "TypeScript": "pages/images/languages/TypeScript.png",
    "Java": "pages/images/languages/Java.png",
    "Dockerfile": "pages/images/languages/Docker.png",
    "Python": "pages/images/languages/Python.png",
    "PHP": "pages/images/languages/Php.png",
    "C": "pages/images/languages/C.png",
    "C++": "pages/images/languages/C++.png",
    "C#": "pages/images/languages/C#.png",
    "Spring Boot": "pages/images/languages/SpringBoot.png",
    "Django": "pages/images/languages/Django.png",
    "Jupyter Notebook": "pages/images/languages/Jupyter.png",
    "MySQL": "pages/images/languages/MySQL.png",
    "SQLite": "pages/images/languages/SQLite.png"
}

# Frontend
Frontends = [
    {"name": "HTML", "path": "pages/images/languages/Html.png", "url": "", "percentage": 70, "language": "HTML"},
    {"name": "CSS", "path": "pages/images/languages/CSS.png", "url": "", "percentage": 70, "language": "CSS"},
    {"name": "SCSS", "path": "pages/images/languages/SCSS.png", "url": "", "percentage": 70, "language": "SCSS"},
    {"name": "JavaScript", "path": "pages/images/languages/JavaScript.png", "url": "", "percentage": 30, "language": "JavaScript"},
    {"name": "TypeScript", "path": "pages/images/languages/TypeScript.png", "url": "", "percentage": 10, "language": "TypeScript"},
    {"name": "Next.js", "path": "pages/images/languages/Next.png", "url": "", "percentage": 20, "language": "JavaScript"},
    {"name": "React", "path": "pages/images/languages/React.png", "url": "", "percentage": 60, "language": "JavaScript"}
]

# Backend
Backends = [
    {"name": "C", "path": "pages/images/languages/C.png", "url": "", "percentage": 70, "language": "C"},
    {"name": "C++", "path": "pages/images/languages/C++.png", "url": "", "percentage": 80, "language": "C++"},
    {"name": "C#", "path": "pages/images/languages/C#.png", "url": "", "percentage": 10, "language": "C#"},
    {"name": "Java", "path": "pages/images/languages/Java.png", "url": "", "percentage": 90, "language": "Java"},
    {"name": "Spring Boot", "path": "pages/images/languages/SpringBoot.png", "url": "", "percentage": 70, "language": "Java"},
    {"name": "PHP", "path": "pages/images/languages/Php.png", "url": "", "percentage": 50, "language": "PHP"},
    {"name": "Python", "path": "pages/images/languages/Python.png", "url": "", "percentage": 50, "language": "Python"},
    {"name": "Django", "path": "pages/images/languages/Django.png", "url": "", "percentage": 50, "language": "Python"},
    {"name": "Jupyter", "path": "pages/images/languages/Jupyter.png", "url": "", "percentage": 50, "language": "Python"},
    {"name": "MySQL", "path": "pages/images/languages/MySQL.png", "url": "", "percentage": 60, "language": "SQL"},
    {"name": "SQLite", "path": "pages/images/languages/SQLite.png", "url": "", "percentage": 60, "language": "SQL"}
]

Contributor = [
    "https://api.github.com/repos/satou0419/typecasters-restAPI",
    "https://api.github.com/repos/satou0419/api-typecasters-tow",
    "https://api.github.com/repos/satou0419/v3-tower-of-words_frontend",
    "https://api.github.com/repos/satou0419/tower-of-words",
    "https://api.github.com/repos/satou0419/typecasters-frontend"
]
    
def CircularProgressBar(percentage):
    radius = 200
    stroke_width = 20
    stroke_color = '#1B81E0FF'
    background_color = '#e0e0e0'
    
    circumference = 2 * math.pi * radius
    stroke_dasharray = circumference
    stroke_dashoffset = circumference * (1 - percentage / 100)

    return f"""
    <svg
        class="progress-circle"
        width="{2 * (radius + stroke_width)}"
        height="{2 * (radius + stroke_width)}"
        viewBox="0 0 {2 * (radius + stroke_width)} {2 * (radius + stroke_width)}"
        xmlns="http://www.w3.org/2000/svg">
        <circle
            cx="{radius + stroke_width}"
            cy="{radius + stroke_width}"
            r="{radius}"
            stroke="{background_color}"
            stroke-width="{stroke_width}"
            fill="none" />
        <circle
            cx="{radius + stroke_width}"
            cy="{radius + stroke_width}"
            r="{radius}"
            stroke="{stroke_color}"
            stroke-width="{stroke_width}"
            stroke-dasharray="{stroke_dasharray}"
            stroke-dashoffset="{stroke_dashoffset}"
            fill="none"
            transform="rotate(-90 {radius + stroke_width} {radius + stroke_width})" />
    </svg>
    """

def LanguageIcon(language):
    return LanguageIcons.get(language, "")

def ImageData(ImagePath):
    with open(ImagePath, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def GithubRepos(username):
    response = requests.get(f"https://api.github.com/users/{username}/repos")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("API rate limit exceeded")
        return []
    
def RepoContributor(Contributor):
    response = requests.get(Contributor)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API rate limit exceeded")
        return None

# Function to fetch languages used in a repository
def RepoLanguages(repo_url):
    response = requests.get(repo_url)
    if response.status_code == 200:
        languages = response.json()
        return languages
    else:
        st.error(f"Failed to fetch languages: {response.status_code}")
        return {}

FrontendPaths = [ImageData(Path['path']) for Path in Frontends]
BackendPaths = [ImageData(Path['path']) for Path in Backends]

Left, Right = st.columns([4, 1])

with Left:
    st.title('Github Projects:')
    repos = GithubRepos("Acrylus")

    st.subheader("GitHub Repositories")
    if repos:
        for repo in repos:
            with st.expander(repo['name'], expanded=True):
                repo_name = repo['name']
                repo_url = repo['html_url']
                repo_description = repo['description'] or "No description provided."
                
                # Fetch languages used in the repository
                languages_url = repo['languages_url']
                languages = RepoLanguages(languages_url)
                languages_used = ", ".join(languages.keys()) if languages else "No languages specified."
                
                st.subheader(repo_name)
                st.write(f"**Description:** {repo_description}")
            
                Icon, Button = st.columns(2)

                with Icon: 
                    st.write("Languages used:")
                        
                    for Language, Percent in languages.items():
                        IconPath = LanguageIcon(Language)
                        if IconPath:
                            st.image(IconPath, width=30)
                        else:
                            st.write(Language)

                with Button: 
                    st.link_button("Github", repo_url, type="primary")


            st.write("---")  # Separator between repositories
    else:
        st.write("No repositories found.")

    st.subheader("GitHub Contribution")
    
    for repo_url in Contributor:
        repo_data = RepoContributor(repo_url)
        if repo_data:
            with st.expander(repo_data['name'], expanded=True):
                repo_name = repo_data['name']
                repo_url = repo_data['html_url']
                repo_description = repo_data['description'] or "No description provided."
                    
                # Fetch languages used in the repository
                languages_url = repo_data['languages_url']
                languages = RepoContributor(languages_url)
                languages_used = ", ".join(languages.keys()) if languages else "No languages specified."
                    
                st.markdown(repo_name)
                st.write(f"**Description:** {repo_description}")

                Icon, Button = st.columns(2)

                with Icon: 
                    st.write("Languages used:")
                        
                    for Language, Percent in languages.items():
                        IconPath = LanguageIcon(Language)
                        if IconPath:
                            st.image(IconPath, width=30)
                        else:
                            st.write(Language)

                with Button: 
                    st.link_button("Github", repo_url, type="primary")

            st.write("---")
  
with Right:
    with st.container(border=True):
        st.html("<h6 style='text-align: center;'>Frontend</h6>")
        for Frontend, FrontendPath in zip(Frontends, FrontendPaths):
            st.markdown(
                f'<div class="icon-container">'
                f'<img src="data:image/png;base64,{FrontendPath}" class="icons">'
                f'{CircularProgressBar(Frontend["percentage"])}'
                f'</div>'
                f'<span class="icon-percentage">Proficiency: {Frontend["percentage"]}%</span>'
                f'<span class="icon-name">{Frontend["name"]}</span>'
                , 
                unsafe_allow_html=True)
            
    with st.container(border=True):
        st.html("<h6 style='text-align: center;'>Backend</h6>")
        for Backend, BackendPath in zip(Backends, BackendPaths):
            st.markdown(
                f'<div class="icon-container">'
                f'<img src="data:image/png;base64,{BackendPath}" class="icons">'
                f'{CircularProgressBar(Backend["percentage"])}'
                f'</div>'
                f'<span class="icon-percentage">Proficiency: {Backend["percentage"]}%</span>'
                f'<span class="icon-name">{Backend["name"]}</span>'
                , 
                unsafe_allow_html=True)
