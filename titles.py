

# Title with horizontal center alignment
def maintitle():
    import streamlit as st
    st.empty()
    st.divider()
    st.markdown(
        """
        <style>
        .centered-subheader {
            text-align: center;
        }
        </style>
        <h2 class="centered-subheader">HEALTHCOMPASS</h2>
        """, 
        unsafe_allow_html=True)
    st.divider()

# Eredmények title

def eredmenyek_title():
    import streamlit as st
    st.empty()
    
    st.divider()
    st.markdown(
        """
        <style>
        .centered-subheader {
            text-align: center;
        }
        </style>
        <h3 class="centered-subheader">EREDMÉNYEK</h3>
        """, 
        unsafe_allow_html=True)
    st.divider()