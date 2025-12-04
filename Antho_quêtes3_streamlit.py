import streamlit as st
import pandas as pd

import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu


credentials = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'Bob': {
            'name': 'Bob',
            'password': 'éponge',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

authenticator = stauth.Authenticate(
    credentials,
    "cookie_name",       # nom du cookie
    "signature_key",     # clé secrète
    cookie_expiry_days=1
)

authenticator.logout("Déconnexion", "sidebar")


 # --- Login box ---
authenticator.login()




# Création du menu qui va afficher les choix qui se trouvent dans la variable options

with st.sidebar:
    
    st.write("Bienvenue root")
    selection = option_menu(
        menu_title=None,
        options = ["Accueil", "🐱Les photos de mon chat"]
    
    )


if selection == "Accueil":
    st.write("Bienvenue sur ma page Streamlit !")
    st.image("Bienvenue.jpg")

elif selection == "🐱Les photos de mon chat":
    st.write("Bienvenue dans l'album de mon chat")
        # Création de 3 colonnes 
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("Cat1.jpg")

    with col2:
        st.image("Cat2.jpg")

    with col3:
        st.image("Cat3.jpg")


name, authentication_status, username = authenticator.login("Connexion", "Menu")

if authentication_status:
    st.write("Bienvenue !")

elif authentication_status is False:
    st.error("C'est pas bon, recommence")
elif authentication_status is None:
    st.warning("Identifiants à renseigner")


