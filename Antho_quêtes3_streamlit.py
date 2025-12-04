import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'Stranger': {
            'name': 'Stranger',
            'password': 'things',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}


# -------------------------------------------------------
# AUTHENTIFICATION
# -------------------------------------------------------
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()

   # Menu sidebar
with st.sidebar:
    st.button("Déconnexion")
    selection = option_menu(
        menu_title=None,
        options=["Accueil", "🐱 Les photos de mon chat"]
        )


    # ------------------------
if selection == "Accueil":
        st.title("Page d'accueil")
        st.write("Bienvenue sur ma page Streamlit !")
        st.image("Bienvenue.jpg")  

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

elif st.session_state["authentication_status"] is False:
    st.error("C'est pas bon recommence")

elif st.session_state["authentication_status"] is None:
    st.warning("Les champs username et mot de passe doivent être remplis")
