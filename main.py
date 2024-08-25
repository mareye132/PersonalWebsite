import streamlit as st

# Page configuration
st.set_page_config(page_title="Mareye's Personal Website", layout="wide")

# Page navigation
PAGES = {
    "Home": "pages/home.py",
    "About": "pages/about.py",
    "Contact": "pages/contact.py"
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Load the selected page
page = PAGES[selection]
exec(open(page).read())
