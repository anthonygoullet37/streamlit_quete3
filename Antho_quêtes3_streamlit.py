import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth

# -------------------------------------------------------
# CREDENTIALS AVEC MOTS DE PASSE HASHÉS (fonctionnels)
# -------------------------------------------------------
# mots de passe : "utilisateurMDP" et "éponge"
credentials = {
    "usernames": {
        "utilisateur": {
            "name": "utilisateur",
            "password": "$2b$12$RiqZK8/tAaZyKsRLj8g9Uu4l4.hbppo4dYVzxNdGlyhAHwpmACqJq",
            "email": "utilisateur@gmail.com",
            "role": "utilisateur"
        },
        "Bob": {
            "name": "Bob",
            "password": "$2b$12$zJIXogq5nyS.HSi3Ta8DKevxUtUC312t3vB3YofC/a73t1uTUCWvm",
            "email": "admin@gmail.com",
            "role": "administrateur"
        }
    }
}

# -------------------------------------------------------
# AUTHENTIFICATION
# -------------------------------------------------------
authenticator = stauth.Authenticate(
    credentials,
    cookie_name="cookie_name",
    key="signature_key",
    cookie_expiry_days=1
)

# -------------------------------------------------------
# LOGIN
# -------------------------------------------------------
login_info = authenticator.login("Connexion", "sidebar")

# -------------------------------------------------------
# LOGOUT
# -------------------------------------------------------
if login_info["authentication_status"]:
    st.sidebar.write(f"Bienvenue {login_info['name']} !")
    authenticator.logout("Déconnexion", "sidebar")

# -------------------------------------------------------
# CONTENU PRINCIPAL
# -------------------------------------------------------
if login_info["authentication_status"]:

    # Menu sidebar
    with st.sidebar:
        selection = option_menu(
            menu_title=None,
            options=["Accueil", "🐱 Les photos de mon chat"]
        )

    # ------------------------
    # Page d'accueil
    # ------------------------
    if selection == "Accueil":
        st.title("Page d'accueil")
        st.write("Bienvenue sur ma page Streamlit !")
        st.image("Bienvenue.jpg")  # vérifier le chemin de l'image

    # ------------------------
    # Album du chat
    # ------------------------
    elif selection == "🐱 Les photos de mon chat":
        st.title("Album de mon chat")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("Cat1.jpg")
        with col2:
            st.image("Cat2.jpg")
        with col3:
            st.image("Cat3.jpg")

# -------------------------------------------------------
# MESSAGES D'ERREUR / ATTENTE
# -------------------------------------------------------
elif login_info["authentication_status"] is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect")

elif login_info["authentication_status"] is None:
    st.warning("Veuillez entrer vos identifiants pour vous connecter")
