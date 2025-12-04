import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth

# --- Hasher les mots de passe ---
passwords = ["utilisateurMDP", "éponge"]
hashed_passwords = stauth.Hasher(passwords).generate()

# --- Données utilisateurs ---
credentials = {
    "usernames": {
        "utilisateur": {
            "name": "utilisateur",
            "password": hashed_passwords[0],
            "email": "utilisateur@gmail.com",
            "role": "utilisateur"
        },
        "Bob": {
            "name": "Bob",
            "password": hashed_passwords[1],
            "email": "admin@gmail.com",
            "role": "administrateur"
        }
    }
}

# --- Authentification ---
authenticator = stauth.Authenticate(
    credentials,
    "cookie_name",      # Nom du cookie
    "signature_key",    # Clé secrète pour signer le cookie
    cookie_expiry_days=1
)

# --- Login ---
name, authentication_status, username = authenticator.login(
    "Connexion",
    location="sidebar"
)

# --- Logout ---
if authentication_status:
    authenticator.logout("Déconnexion", "sidebar")
    st.sidebar.write(f"Bienvenue {name} !")

# --- Contenu principal ---
if authentication_status:
    # Menu sidebar
    with st.sidebar:
        selection = option_menu(
            menu_title=None,
            options=["Accueil", "🐱 Les photos de mon chat"]
        )

    if selection == "Accueil":
        st.title("Page d'accueil")
        st.write("Bienvenue sur ma page Streamlit !")
        st.image("Bienvenue.jpg")

    elif selection == "🐱 Les photos de mon chat":
        st.title("Album de mon chat")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("Cat1.jpg")
        with col2:
            st.image("Cat2.jpg")
        with col3:
            st.image("Cat3.jpg")

elif authentication_status is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect")
elif authentication_status is None:
    st.warning("Veuillez entrer vos identifiants pour vous connecter")
