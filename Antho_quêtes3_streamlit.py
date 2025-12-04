import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth


credentials = {
    "usernames": {
        "utilisateur": {
            "name": "utilisateur",
            "password": "utilisateurMDP",
            "email": "utilisateur@gmail.com",
            "failed_login_attempts": 0,
            "logged_in": False,
            "role": "utilisateur"
        },
        "Bob": {
            "name": "Bob",
            "password": "éponge",
            "email": "admin@gmail.com",
            "failed_login_attempts": 0,
            "logged_in": False,
            "role": "administrateur"
        }
    }
}

# --- Authentification ---
authenticator = stauth.Authenticate(
    credentials,
    "cookie_name",      
    "signature_key",   
    cookie_expiry_days=1
)

# --- Login ---
name, authentication_status, username = authenticator.login(
    name="Connexion", 
    location="sidebar"
)

# --- Logout ---
if authentication_status:
    authenticator.logout("Déconnexion", "sidebar")
    st.sidebar.write("Bienvenue!")

# --- Contenu de l'application après login ---
if authentication_status:
    # Menu sidebar
    with st.sidebar:
        selection = option_menu(
            menu_title=None,
            options=["Accueil", "🐱 Les photos de mon chat"],)

    if selection == "Accueil":
        st.title("Page d'accueil")
        st.write("Bienvenue sur ma page Streamlit !")
        st.image("Bienvenue.jpg")

    elif selection == "🐱 Les photos de mon chat":
        st.title("Album de mon chat")
        # Création de 3 colonnes pour les images
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("Cat1.jpg")
        with col2:
            st.image("Cat2.jpg")
        with col3:
            st.image("Cat3.jpg")

elif authentication_status is False:
    st.error("NC'est pas bon recommence")
elif authentication_status is None:
    st.warning("Entrer les identifiants")
